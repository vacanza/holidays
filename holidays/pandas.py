from holidays.holiday_base import HolidayBase
import pandas as pd


def holidays_to_series(cls: HolidayBase, name: str = "holiday") -> pd.Series:
    """Get Pandas Series from HolidayBase object

    Example usage:
        >>> from holidays.pandas import holidays_to_series
        >>> holidays_to_series(holidays.US(years=[2022]))
            2022-01-01                                     New Year's Day
            2022-01-17                         Martin Luther King Jr. Day
            2022-02-21                              Washington's Birthday
            2022-05-30                                       Memorial Day
            2022-06-19               Juneteenth National Independence Day
            2022-06-20    Juneteenth National Independence Day (Observed)
            2022-07-04                                   Independence Day
            2022-09-05                                          Labor Day
            2022-10-10                                       Columbus Day
            2022-11-11                                       Veterans Day
            2022-11-24                                       Thanksgiving
            2022-12-25                                      Christmas Day
            2022-12-26                           Christmas Day (Observed)
            Name: holiday, dtype: object

    :param cls:
        The HolidaysBase object to convert to Pandas Series.
        Make sure the years parameter is not empty.

    :param name:
        The name to give to the Series.

    :return:
        A :pd.Series: object consisting of given holidays.
    """
    return pd.Series(index=cls.keys(), data=cls.values(), name=name)


def holidays_to_dataframe(cls: HolidayBase, name="holiday") -> pd.DataFrame:
    """Get Pandas DataFrame from HolidayBase object

    Example usage:
        >>> from holidays.pandas import holidays_to_dataframe
        >>> holidays_to_dataframe(holidays.US(years=[2022]))
                                                                holiday
            2022-01-01                                   New Year's Day
            2022-01-17                       Martin Luther King Jr. Day
            2022-02-21                            Washington's Birthday
            2022-05-30                                     Memorial Day
            2022-06-19             Juneteenth National Independence Day
            2022-06-20  Juneteenth National Independence Day (Observed)
            2022-07-04                                 Independence Day
            2022-09-05                                        Labor Day
            2022-10-10                                     Columbus Day
            2022-11-11                                     Veterans Day
            2022-11-24                                     Thanksgiving
            2022-12-25                                    Christmas Day
            2022-12-26                         Christmas Day (Observed)

    :param cls:
        The HolidaysBase object to convert to Pandas DataFrame.
        Make sure the years parameter is not empty.

    :param name:
        The name to give to the column.

    :return:
        A :pd.DataFrame: object consisting of given holidays.
    """
    return holidays_to_series(cls, name).to_frame()
