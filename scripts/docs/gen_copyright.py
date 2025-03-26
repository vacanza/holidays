#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

"""Generate the JS code that sets the copyright text and updates the footer."""

from datetime import datetime, timezone

import mkdocs_gen_files


def main():
    now = datetime.now(tz=timezone.utc)
    copyright_text = f"© Copyright {now.year}. Last updated on {now:%b %d, %Y}."

    js_code = f"""// This file is generated at build time.
    document.addEventListener("DOMContentLoaded", function () {{
        const contentInfo = document.querySelector("footer div[role='contentinfo']");
        if (contentInfo) {{
            contentInfo.insertAdjacentHTML("beforebegin", "<p>{copyright_text}</p>");
        }}
    }});
    """

    with mkdocs_gen_files.open("js/copyright.js", "w", encoding="utf-8", newline="\n") as f:
        f.write(js_code)


if __name__ in {"__main__", "<run_path>"}:
    main()
