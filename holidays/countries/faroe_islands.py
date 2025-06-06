from gettext import gettext as tr

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class FaroeIslands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Faroe Islands holidays.

    References:
        - https://visitfaroeislands.com/en/plan-your-stay/before-you-arrive-in-the-faroe-islands/\
            public-holidays
        - https://en.wikipedia.org/wiki/Public_holidays_in_the_Faroe_Islands
    """

    country = "FO"
    default_language = "fo"
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("da", "en_US", "fo", "is", "no", "sv")
    start_year = 1948  # Year of home rule

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day(tr("Nýggjársdagur"))

        # Maundy Thursday
        self._add_holy_thursday(tr("Skírhósdagur"))

        # Good Friday
        self._add_good_friday(tr("Langifríggjadagur"))

        # Easter Sunday
        self._add_easter_sunday(tr("Páskadagur"))

        # Easter Monday
        self._add_easter_monday(tr("Annar páskadagur"))

        # National Flag Day - April 25
        self._add_holiday_apr_25(tr("Flaggdagur"))

        # General Prayer Day - 4th Friday after Easter
        self._add_holiday_26_days_past_easter(tr("Dýri biðidagur"))

        # Ascension Day
        self._add_ascension_thursday(tr("Kristi himmalsferðardagur"))

        # Whit Sunday
        self._add_whit_sunday(tr("Hvítusunnudagur"))

        # Whit Monday
        self._add_whit_monday(tr("Annar hvítusunnudagur"))

        # Constitution Day - June 5
        self._add_holiday_jun_5(tr("Grundlógardagur"))

        # St. Olaf's Eve - July 28 (half-day)
        self._add_holiday_jul_28(tr("Ólavsøkuaftan"))

        # St. Olaf's Day - July 29
        self._add_holiday_jul_29(tr("Ólavsøkudagur"))

        # Christmas Eve - December 24
        self._add_christmas_eve(tr("Jólaaftan"))

        # Christmas Day - December 25
        self._add_christmas_day(tr("Jóladagur"))

        # Boxing Day - December 26
        self._add_christmas_day_two(tr("Annar jóladagur"))

        # New Year's Eve - December 31
        self._add_new_years_eve(tr("Nýggjársaftan"))

    def _populate_optional_holidays(self):
        # Add optional holidays here if needed
        pass


class FO(FaroeIslands):
    pass


class FRO(FaroeIslands):
    pass
