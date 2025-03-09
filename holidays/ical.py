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


class ICalExporter:
    def __init__(self, holidays_object, return_bytes=False):
        """Initialize iCalendar exporter

        Args:
        - holidays_object: Holidays object containing holiday data
        - return_bytes(bool): If True, return bytes instead of string
        """
        self.holidays = holidays_object
        self.return_bytes = return_bytes

    def _fold_line(self, line):
        """Fold long lines according to RFC 5545.

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

    def generate_event(self, date, holiday_name):
        """Generate a single holiday event
        Args:
        - date: Holiday date
        - holiday_name: Holiday name

        Returns:
        - list[str]: List of iCalender format event lines
        """
        formatted_date = date.strftime("%Y%m%d")

        lines = [
            "BEGIN:VEVENT",
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
        """Generate iCalendar data

        Yields:
        - Union[str, bytes]: Each line of iCalendar format
            (string or bytes depending on return_bytes)
        """
        lines = []
        lines.append("BEGIN:VCALENDAR")
        lines.append("VERSION:2.0")
        lines.append("PRODID:-//holidays Framework//NONSGML v1.9//EN")

        for date, name in self.holidays.items():
            lines.extend(self.generate_event(date, name))

        lines.append("END:VCALENDAR")

        for line in lines:
            yield line.encode("utf-8") if self.return_bytes else line
