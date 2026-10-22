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

from pathlib import Path

import polib

ta_po_path = (
    Path(__file__).parent.parent / "holidays" / "locale" / "ta_LK" / "LC_MESSAGES" / "XCOL.po"
)
ta_po = polib.pofile(str(ta_po_path))

translations = {
    "Special Bank Holiday": "விசேட வங்கி விடுமுறை",
    "Vesak Holiday": "வெசாக் விடுமுறை",
    "CSE Customary Holiday": "CSE சாதாரண விடுமுறை",
    "Customary Holiday": "சாதாரண விடுமுறை",
    "Day prior to Sinhala & Tamil New Year day": "சித்திரை புத்தாண்டுக்கு முந்தைய தினம்",
    "Market closure due to COVID-19": "கோவிட்-19 காரணமாக சந்தை மூடல்",
    "Additional holiday in lieu of May Day falling on Sunday": (
        "ஞாயிற்றுக்கிழமையில் வரும் மே தினத்திற்கான கூடுதல் விடுமுறை"
    ),
    "Additional holiday in lieu of Christmas Day falling on Sunday": (
        "ஞாயிற்றுக்கிழமையில் வரும் நத்தார் தினத்திற்கான கூடுதல் விடுமுறை"
    ),
    "Additional holiday in lieu of Tamil Thai Pongal Day falling on Sunday": (
        "ஞாயிற்றுக்கிழமையில் வரும் தைப்பொங்கல் தினத்திற்கான கூடுதல் விடுமுறை"
    ),
    "Additional holiday in lieu of Independence Day falling on Sunday": (
        "ஞாயிற்றுக்கிழமையில் வரும் சுதந்திர தினத்திற்கான கூடுதல் விடுமுறை"
    ),
    ("Additional holiday in lieu of Milad-Un-Nabi (Holy Prophet's Birthday) falling on Sunday"): (
        "ஞாயிற்றுக்கிழமையில் வரும் மீலாதுன் நபி (நபிகள் நாயகத்தின் பிறந்த நாள்) தினத்திற்கான கூடுதல் விடுமுறை"
    ),
    ("Special Bank Holiday on account of Sinhala & Tamil New Year Day falling on a Sunday"): (
        "ஞாயிற்றுக்கிழமையில் வரும் சித்திரை புத்தாண்டு தினத்திற்கான விசேட வங்கி விடுமுறை"
    ),
    (
        "Special Bank Holiday on account of Day Following Vesak Full Moon Poya Day"
        " falling on a Sunday"
    ): ("ஞாயிற்றுக்கிழமையில் வரும் வெசாக் பௌர்ணமி தினத்திற்கு மறுநாளான விசேட வங்கி விடுமுறை"),
    ("Special Bank Holiday on account of Holy Prophet's Birthday falling on a Sunday"): (
        "ஞாயிற்றுக்கிழமையில் வரும் நபிகள் நாயகத்தின் பிறந்த தினத்திற்கான விசேட வங்கி விடுமுறை"
    ),
    (
        "Special Bank Holiday on account of the Day prior to Sinhala & Tamil New Year Day"
        " falling on a Sunday"
    ): ("ஞாயிற்றுக்கிழமையில் வரும் சித்திரை புத்தாண்டுக்கு முந்தைய தினத்திற்கான விசேட வங்கி விடுமுறை"),
    (
        "Special Bank Half-holiday on account of Day prior to Sinhala & Tamil New Year Day"
        " falling on a Saturday"
    ): ("சனிக்கிழமையில் வரும் சித்திரை புத்தாண்டுக்கு முந்தைய தினத்திற்கான விசேட வங்கி அரை நாள் விடுமுறை"),
    "Additional half-holiday on account of the May Day falling on a Saturday": (
        "சனிக்கிழமையில் வரும் மே தினத்திற்கான கூடுதல் அரை நாள் விடுமுறை"
    ),
    "Additional half-holiday on account of the Christmas Day falling on a Saturday": (
        "சனிக்கிழமையில் வரும் நத்தார் தினத்திற்கான கூடுதல் அரை நாள் விடுமுறை"
    ),
    "Additional half holiday in lieu of the Independence Day falling on Saturday": (
        "சனிக்கிழமையில் வரும் சுதந்திர தினத்திற்கான கூடுதல் அரை நாள் விடுமுறை"
    ),
    (
        "Additional half holiday in lieu of Day Following Vesak Full Moon Poya Day"
        " falling on Saturday"
    ): ("சனிக்கிழமையில் வரும் வெசாக் பௌர்ணமி தினத்திற்கு மறுநாளான கூடுதல் அரை நாள் விடுமுறை"),
    ("Additional half holiday in lieu of Sinhala & Tamil New Year Day falling on Saturday"): (
        "சனிக்கிழமையில் வரும் சித்திரை புத்தாண்டு தினத்திற்கான கூடுதல் அரை நாள் விடுமுறை"
    ),
}

count = 0
for entry in ta_po:
    # If the current msgstr is an English string, replace it
    if entry.msgstr in translations:
        entry.msgstr = translations[entry.msgstr]  # type: ignore[index]
        count += 1

ta_po.save(str(ta_po_path))
