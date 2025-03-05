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

import datetime

# Generate the build date values
year = datetime.datetime.now().year
build_date = datetime.datetime.now().strftime("%b %d, %Y")

copyright_text = f"© Copyright {year}. Last updated on {build_date}."

# Generate the JS code that sets the copyright text and updates the footer
js_code = f"""// This file is generated at build time
var copyrightText = "{copyright_text}";
document.addEventListener("DOMContentLoaded", function () {{
    var contentInfo = document.querySelector("footer div[role='contentinfo']");
    if (contentInfo) {{
        contentInfo.insertAdjacentHTML("beforebegin", `<p>${{copyrightText}}</p>`);
    }}
}});
"""

with open("docs/js/copyright.js", "w", encoding="utf-8") as f:
    f.write(js_code)
