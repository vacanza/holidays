"""Returns True if the year is leap. Returns False otherwise."""
        return isleap(self._year)

    def _add_holiday(self, name: str, *args) -> date | None:
        """Add a holiday."""
        if not args:
            raise TypeError("Incorrect number of arguments.")

        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)

        if dt.year != self._year:
            return None
        if getattr(self,"only_observed",False) and getattr(self,"observed_label","")not in name:
            return None
        self[dt] = self.tr(name)
        return dt

    def _add_multiday_holiday(
        self, start_date: date, duration_days: int, *, name: str | None = None
    ) -> set[date]:
        """Add a multi-day holiday.

        Args: