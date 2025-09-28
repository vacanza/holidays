from holidays.countries.spain import Spain
from holidays.mixins.child_entity import ChildEntity

class HolidaysIC(ChildEntity, Spain):
    """Canary Islands holidays.

    Alias of a Spanish subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Spain>
        * <https://en.wikipedia.org/wiki/Canary_Islands>
    """

    country = "IC"
    parent_entity = Spain
    parent_entity_subdivision_code = "CN"
    start_year = 1983

class CanaryIslands(HolidaysIC):
    pass

class IC(CanaryIslands):
    pass