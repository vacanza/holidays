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
from datetime import datetime, timezone


class ICalExporter:
    def __init__(self, holidays_object, return_bytes=False, ical_timestamp=None):
        """
        Initialize iCalendar exporter

        Args:
        - holidays_object: Holidays object containing holiday data.
        - return_bytes(bool): If True, return bytes instead of string.
        - ical_timestamp: Optional override for the iCal "DTSTAMP" parameter.
            If not provided, current datetime (UTC timezone) will be used instead.
        """
        self.holidays = holidays_object
        self.return_bytes = return_bytes
        if ical_timestamp is None:
            self.ical_timestamp = datetime.now().astimezone(timezone.utc).strftime("%Y%m%dT%H%M%S")
        else:
            self.ical_timestamp = ical_timestamp

        try:
            with open("holidays/version.py") as file:
                for line in file:
                    if line.startswith("__version__"):
                        self.holidays_version = line.split("=")[1].strip().strip('"')
                        break
                else:
                    raise ValueError("Version not found in holidays/version.py")
        except FileNotFoundError:
            raise FileNotFoundError("The file 'holidays/version.py' was not found.")

        self.language = self._validate_language(getattr(self.holidays, "language", "EN"))

    def _validate_language(self, language):
        """
        Validates the language code. Ensures it's a two-letter ISO 639-1 code
        as iCal only supports that at the moment.

        Args:
        - language: The language code to validate.

        Returns:
        - Valid two-letter language code in uppercase.
        """
        language = (language or "EN").upper().split("_")[0]

        if len(language) != 2:
            raise ValueError(
                f"Invalid language code: {language}. "
                "Only two-letter ISO 639-1 codes supported by iCal"
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

    def _generate_event(self, date, holiday_name):
        """
        Generate a single holiday event.

        Args:
        - date: Holiday date.
        - holiday_name: Holiday name.

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
            "DURATION:P1D",
            "END:VEVENT",
        ]

        folded_lines = []
        for line in lines:
            folded_lines.extend(self._fold_line(line))

        return folded_lines

    def generate(self):
        """
        Generate iCalendar data.

        Yields:
        - Union[str, bytes]: Each line of iCalendar format
            (string or bytes depending on return_bytes).
        """
        lines = []
        lines.append("BEGIN:VCALENDAR")
        lines.append(
            f"PRODID:-//Vacanza//Open World Holidays Framework v{self.holidays_version}//"
            f"{self.language}//EN"
        )
        lines.append("VERSION:2.0")

        for date, name in self.holidays.items():
            lines.extend(self._generate_event(date, name))

        lines.append("END:VCALENDAR")

        for line in lines:
            yield line.encode("utf-8") if self.return_bytes else line
