#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from __future__ import annotations

import re
import uuid
from datetime import date, datetime, timezone
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

from holidays.calendars.gregorian import _timedelta
from holidays.version import __version__

if TYPE_CHECKING:
    from collections.abc import Iterable

    from holidays.holiday_base import HolidayBase

# iCal-specific constants
CONTENT_LINE_MAX_LENGTH = 75
CONTENT_LINE_DELIMITER = "\r\n"
CONTENT_LINE_DELIMITER_WRAP = f"{CONTENT_LINE_DELIMITER} "
UID_DOMAIN = "holidays.vacanza.dev"
UID_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, UID_DOMAIN)

# RFC 5545 `dur-value` without the optional sign.
DURATION_PATTERN = re.compile(
    r"^P(?:\d+W|\d+D(?:T(?:\d+H(?:\d+M(?:\d+S)?)?|\d+M(?:\d+S)?|\d+S))?"
    r"|T(?:\d+H(?:\d+M(?:\d+S)?)?|\d+M(?:\d+S)?|\d+S))$"
)


class ICalExporter:
    def __init__(
        self,
        instance: HolidayBase,
        show_language: bool = False,
        *,
        refresh_interval: str | None = None,
    ) -> None:
        """Initialize iCalendar exporter.

        Args:
            instance:
                [`HolidayBase`][holidays.holiday_base.HolidayBase] object
                containing holiday data.

            show_language:
                Determines whether to include the `;LANGUAGE=` attribute in the
                `SUMMARY` field. Defaults to `False`.

                If the [`HolidayBase`][holidays.holiday_base.HolidayBase] object
                has a `language` attribute, it will be used. Otherwise,
                `default_language` will be used if available.

                If neither attribute exists and `show_language=True`, an
                exception will be raised.

            refresh_interval:
                Suggested refresh interval for calendar clients subscribed to
                the published calendar, as an
                [RFC 5545](https://web.archive.org/web/20260815171151/https://datatracker.ietf.org/doc/html/rfc5545)
                duration (e.g. `P1W` for one week). Emits the `REFRESH-INTERVAL`
                ([RFC 7986](https://web.archive.org/web/20260611035104/https://datatracker.ietf.org/doc/html/rfc7986))
                and `X-PUBLISHED-TTL` properties. Defaults to `None` (not emitted).
        """
        self.holidays = instance
        self.show_language = show_language
        self.refresh_interval = (
            self._validate_refresh_interval(refresh_interval)
            if refresh_interval is not None
            else None
        )
        self.ical_timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.holidays_version = __version__
        language = getattr(self.holidays, "language", None) or getattr(
            self.holidays, "default_language", None
        )
        self.language = (
            self._validate_language(language)
            if isinstance(language, str)
            and language in getattr(self.holidays, "supported_languages", [])
            else None
        )

        if self.show_language and self.language is None:
            raise ValueError("LANGUAGE cannot be included because the language code is missing.")

    def _validate_language(self, language: str) -> str:
        """Validate the language code to ensure it complies with
        [RFC 5646](https://web.archive.org/web/20261001095044/https://datatracker.ietf.org/doc/html/rfc5646).

        In the current implementation, all languages must comply with
        either [ISO 639-1 or ISO 639-2](https://web.archive.org/web/20261003082739/https://www.loc.gov/standards/iso639-2/php/code_list.php)
        if specified (part of [RFC 5646](https://web.archive.org/web/20261001095044/https://datatracker.ietf.org/doc/html/rfc5646)).

        Args:
            language:
                The language code to validate.

        Returns:
            Validated language code.
        """
        # Remove whitespace (if any), transforms HolidaysBase default to RFC 5646 compliant
        # i.e. `en_US` to `en-US`.
        language = language.strip().replace("_", "-")

        # ISO 639-1 and ISO 639-2 patterns, in compliance with RFC 5646.
        iso639_pattern = re.compile(r"^[a-z]{2,3}(?:-[A-Z]{2})?$")

        if not iso639_pattern.fullmatch(language):
            raise ValueError(
                f"Invalid language tag: '{language}'. Expected format follows "
                "ISO 639-1 or ISO 639-2, e.g., 'en', 'en-US'. For more details, "
                "refer to: https://www.loc.gov/standards/iso639-2/php/code_list.php."
            )
        return language

    def _validate_refresh_interval(self, refresh_interval: str) -> str:
        """Validate the refresh interval to ensure it is a positive
        [RFC 5545](https://web.archive.org/web/20260815171151/https://datatracker.ietf.org/doc/html/rfc5545)
        duration.

        Args:
            refresh_interval:
                The duration to validate.

        Returns:
            Validated duration.
        """
        refresh_interval = refresh_interval.strip().upper()

        if not DURATION_PATTERN.fullmatch(refresh_interval):
            raise ValueError(
                f"Invalid refresh interval: '{refresh_interval}'. Expected an RFC 5545 "
                "duration, e.g., 'P1W' or 'P1D'."
            )
        return refresh_interval

    @cached_property
    def entity_name(self) -> str:
        """Human-readable name of the exported entity.

        Taken from the entity docstring (e.g. `Belgium holidays.`), falling back to
        the entity code(s) for combined or custom holiday objects.
        """
        for cls in type(self.holidays).__mro__:
            match = re.fullmatch(r"(.+) holidays\.", (cls.__doc__ or "").strip().split("\n")[0])
            if match:
                return match.group(1)

        codes = getattr(self.holidays, "country", None) or getattr(self.holidays, "market", None)
        return ", ".join(codes) if isinstance(codes, list) else codes or ""

    @cached_property
    def calendar_name(self) -> str:
        """Calendar display name used for the `X-WR-CALNAME` property.

        Examples: `Thailand Holidays`, `Israel School Holidays`,
        `Belgium Holidays [en-US]`.
        """
        parts = [self.entity_name] if self.entity_name else []

        subdiv = self.holidays.subdiv
        if subdiv:
            parts.append(f"({', '.join(subdiv) if isinstance(subdiv, list) else subdiv})")

        categories = sorted(self.holidays.categories)
        if categories != [self.holidays.default_category]:
            parts.append(", ".join(category.replace("_", " ").title() for category in categories))

        parts.append("Holidays")

        language = self.holidays.language
        if language and language != getattr(self.holidays, "default_language", None):
            parts.append(f"[{self.language or language}]")

        return " ".join(parts)

    @cached_property
    def _uid_prefix(self) -> str:
        """Entity-specific part of the event UID key."""
        codes = getattr(self.holidays, "country", None) or getattr(self.holidays, "market", None)
        subdiv = self.holidays.subdiv
        return "|".join(
            (
                ",".join(codes) if isinstance(codes, list) else codes or "",
                ",".join(subdiv) if isinstance(subdiv, list) else subdiv or "",
                self.language or "",
                ",".join(sorted(self.holidays.categories)),
            )
        )

    def _generate_uid(self, dt: date, holiday_name: str) -> str:
        """Generate a deterministic event UID.

        The UID is a UUID5 of the entity, subdivision, language, categories, holiday
        name and start date, so it stays the same across runs and library versions.
        Calendar clients rely on this to update subscribed events in place.

        Args:
            dt:
                Holiday start date.

            holiday_name:
                Holiday name.

        Returns:
            The event UID.
        """
        key = f"{self._uid_prefix}|{holiday_name}|{dt.isoformat()}"
        return f"{uuid.uuid5(UID_NAMESPACE, key)}@{UID_DOMAIN}"

    def _escape_text(self, text: str) -> str:
        """Escape special characters in a `TEXT` value per
        [RFC 5545](https://web.archive.org/web/20260815171151/https://datatracker.ietf.org/doc/html/rfc5545).

        Args:
            text:
                The text to escape.

        Returns:
            The escaped text.
        """
        return text.replace("\\", "\\\\").replace(",", "\\,").replace(":", "\\:")

    def _fold_line(self, line: str) -> str:
        """Fold long lines according to
        [RFC 5545](https://web.archive.org/web/20260815171151/https://datatracker.ietf.org/doc/html/rfc5545).

        Content lines SHOULD NOT exceed 75 octets. If a line is too long,
        it must be split into multiple lines, with each continuation line
        starting with a space.

        Args:
            line:
                The content line to be folded.

        Returns:
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

    def _generate_event(
        self, dt: date, holiday_name: str, holiday_length: int = 1
    ) -> Iterable[str]:
        """Generate a single holiday event.

        Args:
            dt:
                Holiday date.

            holiday_name:
                Holiday name.

            holiday_length:
                Holiday length in days, default to 1.

        Returns:
            Iterable of iCalendar format event lines.
        """
        # SEMICOLON is used as a delimiter in HolidayBase (HOLIDAY_NAME_DELIMITER = "; "),
        # so a name with a semicolon gets split into two separate `VEVENT`s.
        language_tag = f";LANGUAGE={self.language}" if self.show_language else ""

        yield "BEGIN:VEVENT"
        yield f"DTSTAMP:{self.ical_timestamp}"
        yield f"UID:{self._generate_uid(dt, holiday_name)}"
        yield self._fold_line(f"SUMMARY{language_tag}:{self._escape_text(holiday_name)}")
        yield f"DTSTART;VALUE=DATE:{dt:%Y%m%d}"
        yield f"DURATION:P{holiday_length}D"
        if len(self.holidays.categories) == 1:
            yield f"CATEGORIES:{next(iter(self.holidays.categories)).upper()}"
        yield "END:VEVENT"

    def generate(self, return_bytes: bool = False) -> str | bytes:
        """Generate iCalendar data.

        Args:
            return_bytes:
                If `True`, return bytes instead of string.

        Returns:
            The complete iCalendar data
            (string or UTF-8 bytes depending on return_bytes).
        """
        lines = [
            "BEGIN:VCALENDAR",
            f"PRODID:-//Vacanza//Open World Holidays Framework v{self.holidays_version}//EN",
            "VERSION:2.0",
            "CALSCALE:GREGORIAN",
            self._fold_line(f"X-WR-CALNAME:{self._escape_text(self.calendar_name)}"),
        ]
        if self.refresh_interval:
            lines.append(f"REFRESH-INTERVAL;VALUE=DURATION:{self.refresh_interval}")
            lines.append(f"X-PUBLISHED-TTL:{self.refresh_interval}")

        # Merged continuous holiday with the same name and use `DURATION` instead.
        holiday_sequences: dict[str, list[date]] = {}
        for dt in sorted(self.holidays.keys()):
            for name in self.holidays.get_list(dt):
                holiday_sequences.setdefault(name, []).append(dt)

        events: list[tuple[date, str, int]] = []
        for name, dates in holiday_sequences.items():
            start_date = dates[0]
            days = 1
            for next_date in dates[1:]:
                if next_date == _timedelta(start_date, days) and next_date.year == start_date.year:
                    days += 1
                else:
                    events.append((start_date, name, days))
                    start_date = next_date
                    days = 1
            events.append((start_date, name, days))

        for event in sorted(events):
            lines.extend(self._generate_event(*event))

        lines.append("END:VCALENDAR")
        lines.append("")

        output = CONTENT_LINE_DELIMITER.join(lines)
        return output.encode() if return_bytes else output

    def save_ics(self, file_path: str | Path) -> None:
        """Export the calendar data to a `.ics` file.

        While [RFC 5545](https://web.archive.org/web/20260815171151/https://datatracker.ietf.org/doc/html/rfc5545)
        does not explicitly restrict filenames for `.ics` files, it is still advisable to follow
        general filesystem conventions and avoid problematic characters.

        Args:
            file_path:
                Path to save the `.ics` file, including the filename (with extension).
        """
        # Generate and write out content (always in bytes for .ics)
        content = self.generate(return_bytes=True)
        if not content:
            raise ValueError("Generated content is empty or invalid.")

        Path(file_path).write_bytes(content)  # type: ignore[arg-type]
