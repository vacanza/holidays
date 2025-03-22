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

    def _fold_line(self, line):
        """
        Fold long lines according to RFC 5545.

        Lines of text SHOULD NOT be longer than 75 octets.
        """
        if len(line.encode("utf-8")) <= 75:
            return [line]

        result = [line]
        while len(result[-1].encode("utf-8")) > 75:
            current = result.pop()
            pos = 74
            while len(current[:pos].encode("utf-8")) > 74:
                pos -= 1
            result.append(current[:pos])
            result.append(f" {current[pos:]}")

        return result

    def _generate_event(self, date, holiday_name, holiday_length: int = 1):
        """
        Generate a single holiday event.

        Args:
        - date: Holiday date.
        - holiday_name: Holiday name.
        - holiday_length: Holiday length in days, default to 1.

        Returns:
        - list[str]: List of iCalender format event lines.
        """
        formatted_date = date.strftime("%Y%m%d")
        event_uid = f"{uuid.uuid4()}@{self.holidays_version}.holidays.local"

        lines = [
            "BEGIN:VEVENT",
            f"DTSTAMP:{self.ical_timestamp}",
            f"UID:{event_uid}",
            f"SUMMARY:{holiday_name}",
            f"DTSTART;VALUE=DATE:{formatted_date}",
            f"DURATION:P{holiday_length}D",
            "END:VEVENT",
        ]

        folded_lines = []
        for line in lines:
            folded_lines.extend(self._fold_line(line))

        return folded_lines

    def generate(self, return_bytes: bool = False):
        """
        Generate iCalendar data.

        Args:
        - return_bytes(bool): If True, return bytes instead of string.

        Returns:
        - str or bytes: The complete iCalendar data
            (string or UTF-8 bytes depending on return_bytes).
        """
        lines = []
        lines.append("BEGIN:VCALENDAR")
        lines.append(
            f"PRODID:-//Vacanza//Open World Holidays Framework v{self.holidays_version}//"
            f"{self.language}//EN"
        )
        lines.append("VERSION:2.0")

        sorted_dates = sorted(self.holidays.keys())
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

        output = "\r\n".join(lines) + "\r\n"
        return output.encode("utf-8") if return_bytes else output
