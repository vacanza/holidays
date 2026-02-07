from holidays.ical import ICalExporter


def export_holiday_calendars(
    country_class,
    country_code,
    years,
    categories,
    language=None,
    output_dir="."
):
    """
    Export holiday calendars as .ics files for each category.
    """

    for category in categories:
        try:
            holidays_obj = country_class(
                years=years,
                categories=category,
                language=language,
            )
            # Note: include_sundays is not supported in all holidays versions


            # Prepare year label
            if isinstance(years, range):
                year_label = f"{years.start}_{years.stop - 1}"
            else:
                year_label = "_".join(map(str, years))

            file_name = f"{country_code}_{category.upper()}_{year_label}.ics"
            file_path = f"{output_dir}/{file_name}"

            exporter = ICalExporter(holidays_obj)
            exporter.save_ics(file_path)

            

        except Exception as error:
            
            continue

if __name__ == "__main__":
    from holidays.countries import US

export_holiday_calendars(
    country_class=US,
    country_code="US",
    years=range(2025, 2026),
    categories=US.supported_categories,
    language="en"
)
