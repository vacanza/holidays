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
from datetime import date, datetime, timedelta, timezone
from typing import Optional, Union

from holidays.holiday_base import HolidayBase
from holidays.version import __version__

# iCal-specific constants
CONTENT_LINE_MAX_LENGTH = 75
CONTENT_LINE_DELIMITER = "\r\n"
CONTENT_LINE_DELIMITER_WRAP = CONTENT_LINE_DELIMITER + " "


class ICalExporter:
    def __init__(self, holidays_object: HolidayBase, ical_timestamp: Optional[str] = None) -> None:
        """
        Initialize iCalendar exporter

        :param holidays_object:
            Holidays object containing holiday data.

        :param ical_timestamp:
            Optional override for the iCal "DTSTAMP" parameter.
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

    def _validate_language(self, language: str) -> str:
        """
        Validates the language code. Ensures it's a two-letter ISO 639-1 code
        as iCal only supports that at the moment.

        :param language:
            The language code to validate.

        :return:
            Valid two-letter language code in uppercase.
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

    def _fold_line(self, line: str) -> str:
        """
        Fold long lines according to RFC 5545.

        Content lines SHOULD NOT exceed 75 octets. If a line is too long,
        it must be split into multiple lines, with each continuation line
        starting with a space.

        :param line:
            The content line to be folded.

        :return:
            The folded content line.
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

    def _generate_event(self, dt: date, holiday_name: str, holiday_length: int = 1) -> list[str]:
        """
        Generate a single holiday event.

        :param date:
            Holiday date.

        :param holiday_name:
            Holiday name.

        :param holiday_length:
            Holiday length in days, default to 1.

        :return:
            List of iCalendar format event lines.
        """
        # Escape special characters per RFC 5545.
        sanitized_holiday_name = (
            holiday_name.replace("\\", "\\\\").replace(",", "\\,").replace(":", "\\:")
        )
        event_uid = f"{uuid.uuid4()}@{self.holidays_version}.holidays.local"

        lines = [
            "BEGIN:VEVENT",
            f"DTSTAMP:{self.ical_timestamp}",
            f"UID:{event_uid}",
            self._fold_line(f"SUMMARY:{sanitized_holiday_name}"),
            f"DTSTART;VALUE=DATE:{dt:%Y%m%d}",
            f"DURATION:P{holiday_length}D",
            "END:VEVENT",
        ]

        return lines

    def generate(self, return_bytes: bool = False) -> Union[str, bytes]:
        """
        Generate iCalendar data.

        :param return_bytes:
            If True, return bytes instead of string.

        :return:
            The complete iCalendar data
            (string or UTF-8 bytes depending on return_bytes).
        """
        lines = [
            "BEGIN:VCALENDAR",
            f"PRODID:-//Vacanza//Open World Holidays Framework v{self.holidays_version}//"
            f"{self.language}",
            "VERSION:2.0",
            "CALSCALE:GREGORIAN",
        ]

        sorted_dates = sorted(self.holidays.keys())
        # Merged continuous holiday with the same name and use `DURATION` instead.
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

    def export_ics(self, file_path: str) -> None:
        """
        Export the calendar data to a .ics file.

        While RFC 5545 does not specifically forbid filenames for .ics files, but it’s advisable
        to follow general filesystem conventions and avoid using problematic characters.

        :param file_path:
            Path to save the .ics file, including the filename (with extension).
        """
        # Generate and write out content (always in bytes for .ics)
        content = self.generate(return_bytes=True)
        if not content:
            raise ValueError("Generated content is empty or invalid.")

        with open(file_path, "wb") as file:
            file.write(content)  # type: ignore  # this is always bytes, ignoring mypy error.
