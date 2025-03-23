#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import uuid
from datetime import datetime, timedelta, timezone

from holidays.version import __version__

# iCal-specific constants
CONTENT_LINE_MAX_LENGTH = 75
CONTENT_LINE_DELIMITER = "\r\n"
CONTENT_LINE_DELIMITER_BYTES = CONTENT_LINE_DELIMITER.encode()
CONTENT_LINE_DELIMITER_WRAP = CONTENT_LINE_DELIMITER + " "


class ICalExporter:
    def __init__(self, holidays_object, ical_timestamp=None):
        """
        Initialize iCalendar exporter

        Args:
        - holidays_object: Holidays object containing holiday data.
        - ical_timestamp: Optional override for the iCal "DTSTAMP" parameter.
            If not provided, current datetime (UTC timezone) will be used instead.
        """
        self.holidays = holidays_object
        self.ical_timestamp = ical_timestamp or datetime.now(timezone.utc).strftime(
            "%Y%m%dT%H%M%SZ"
        )
        self.holidays_version = __version__
        self.language = self._validate_language(
            getattr(self.holidays, "language", None)
            or getattr(self.holidays, "default_language", None)
            or "EN"
        )

    def _validate_language(self, language):
        """
        Validates the language code. Ensures it's a two-letter ISO 639-1 code
        as iCal only supports that at the moment.

        Args:
        - language: The language code to validate.

        Returns:
        - Valid two-letter language code in uppercase.
        """
        language = language.upper().split("_")[0]

        if len(language) != 2:
            raise ValueError(
                f"Invalid language code: {language}. "
                "Only two-letter ISO 639-1 codes are supported by iCal. "
                "Refer to the 'ISO 639-1 Code' column at "
                "https://www.loc.gov/standards/iso639-2/php/code_list.php for valid codes."
            )
        return language

    def _fold_line(self, line: str):
        """
        Fold long lines according to RFC 5545.

        Content lines SHOULD NOT exceed 75 octets. If a line is too long,
        it must be split into multiple lines, with each continuation line
        starting with a space.

        Args:
        - line (str): The content line to be folded.

        Returns:
        - str: The folded content line.
        """
        if line.isascii():
            # Simple split for ASCII: every (CONTENT_LINE_MAX_LENGTH - 1) chars,
            # as first char of the next line is space
            if len(line) > CONTENT_LINE_MAX_LENGTH:
                return CONTENT_LINE_DELIMITER_WRAP.join(
                    line[i : i + CONTENT_LINE_MAX_LENGTH - 1]
                    for i in range(0, len(line), CONTENT_LINE_MAX_LENGTH - 1)
                )

        elif len(line.encode()) > CONTENT_LINE_MAX_LENGTH:
            # Handle non-ASCII text while respecting byte length
            parts = []
            part_start = 0
            part_len = 0
            for i, char in enumerate(line):
                char_byte_len = len(char.encode())
                part_len += char_byte_len

                if part_len > CONTENT_LINE_MAX_LENGTH:
                    parts.append(line[part_start:i])
                    part_start = i
                    part_len = char_byte_len + 1  # line start with space

            parts.append(line[part_start:])
            return CONTENT_LINE_DELIMITER_WRAP.join(parts)

        # Return as-is if it doesn't exceed the limit
        return line

    def _generate_event(self, date, holiday_name: str, holiday_length: int = 1):
        """
        Generate a single holiday event.

        Args:
        - date: Holiday date.
        - holiday_name (str): Holiday name.
        - holiday_length (int): Holiday length in days, default to 1.

        Returns:
        - list[str]: List of iCalendar format event lines.
        """
        event_uid = f"{uuid.uuid4()}@{self.holidays_version}.holidays.local"

        lines = [
            "BEGIN:VEVENT",
            f"DTSTAMP:{self.ical_timestamp}",
            f"UID:{event_uid}",
            self._fold_line(f"SUMMARY:{holiday_name}"),
            f"DTSTART;VALUE=DATE:{date:%Y%m%d}",
            f"DURATION:P{holiday_length}D",
            "END:VEVENT",
        ]

        return lines

    def generate(self, return_bytes: bool = False):
        """
        Generate iCalendar data.

        Args:
        - return_bytes(bool): If True, return bytes instead of string.

        Returns:
        - str or bytes: The complete iCalendar data
            (string or UTF-8 bytes depending on return_bytes).
        """
        lines = [
            "BEGIN:VCALENDAR",
            f"PRODID:-//Vacanza//Open World Holidays Framework v{self.holidays_version}//"
            f"{self.language}",
            "VERSION:2.0",
        ]

        sorted_dates = sorted(self.holidays.keys())
        # For Continuous Holidays with exact same name, they are merged
        # together with increased DURATION
        i = 0
        while i < len(sorted_dates):
            dt = sorted_dates[i]
            names = self.holidays.get_list(dt)

            for name in names:
                days = 1
                while (
                    i + days < len(sorted_dates)
                    and sorted_dates[i + days] == sorted_dates[i] + timedelta(days=days)
                    and name in self.holidays.get_list(sorted_dates[i + days])
                ):
                    days += 1

                lines.extend(self._generate_event(dt, name, days))

            i += days

        lines.append("END:VCALENDAR")

        lines.append("")
        output = CONTENT_LINE_DELIMITER.join(lines)
        return output.encode() if return_bytes else output
