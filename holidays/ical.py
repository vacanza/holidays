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
    def __init__(self, holidays_object, language="en", return_bytes=False):
        """Initialize iCalendar exporter

        Args:
        - holidays_object: Holidays object containing holiday data
        - language (str) Output language code (default: 'en')
        - return_bytes(bool): If True, return bytes instead of string
        """
        self.holidays = holidays_object
        self.language = language
        self.return_bytes = return_bytes

    def generate_event(self, date, holiday_name):
        """Generate a single holiday event
        Args:
        - date: Holiday date
        - holiday_name: Holiday name

        Returns:
        - list[str]: List of iCalender format event lines
        """
        formatted_date = date.strftime("%Y%m%d")
        # TODO:implement proper translation logic
        name = holiday_name

        return [
            "BEGIN:VEVENT",
            f"SUMMARY:{name}",
            f"DTSTART;VALUE=DATE:{formatted_date}",
            "DURATION:P1D",
            "END:VEVENT",
        ]

    def generate(self):
        """Generate iCalendar data

        Yields:
        - str: Each line of iCalendar format
        """
        yield "BEGIN:VCALENDAR"
        yield "VERSION:2.0"
        yield f"PRODID:-//holidays Framework//NONSGML v1.9//{self.language.upper()}"

        for date, name in self.holidays.items():
            yield from self.generate_event(date, name)

        yield "END:VCALENDAR"
