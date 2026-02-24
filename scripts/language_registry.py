#!/usr/bin/env python3

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

LANGUAGES = {
    # --- Base Languages ---
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cnr": "Montenegrin",
    "cs": "Czech",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fil": "Filipino",
    "fo": "Faroese",
    "fr": "French",
    "fy": "Western Frisian",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "ht": "Haitian Creole",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "kl": "Kalaallisut (Greenlandic)",
    "km": "Khmer",
    "ko": "Korean",
    "lb": "Luxembourgish",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mk": "Macedonian",
    "mn": "Mongolian",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sq": "Albanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "tet": "Tetum",
    "tg": "Tajik",
    "th": "Thai",
    "tk": "Turkmen",
    "tkl": "Tokelauan",
    "to": "Tongan",
    "tr": "Turkish",
    "tvl": "Tuvaluan",
    "uk": "Ukrainian",
    "uz": "Uzbek",
    "vi": "Vietnamese",

    # --- Arabic Locales ---
    "ar_EG": "Arabic (Egypt)",
    "ar_QA": "Arabic (Qatar)",
    "ar_SD": "Arabic (Sudan)",

    # --- Cocos Islands ---
    "coa_CC": "Cocos Islands Malay",

    # --- English Locales ---
    "en_AI": "English (Anguilla)",
    "en_AU": "English (Australia)",
    "en_BM": "English (Bermuda)",
    "en_BQ": "English (Bonaire, Sint Eustatius and Saba)",
    "en_CA": "English (Canada)",
    "en_CC": "English (Cocos Islands)",
    "en_CI": "English (Ivory Coast)",
    "en_CK": "English (Cook Islands)",
    "en_CX": "English (Christmas Island)",
    "en_CY": "English (Cyprus)",
    "en_ET": "English (Ethiopia)",
    "en_FM": "English (Micronesia)",
    "en_GB": "English (United Kingdom)",
    "en_GD": "English (Grenada)",
    "en_GM": "English (Gambia)",
    "en_GS": "English (South Georgia & South Sandwich Islands)",
    "en_GY": "English (Guyana)",
    "en_HK": "English (Hong Kong)",
    "en_IN": "English (India)",
    "en_KE": "English (Kenya)",
    "en_LC": "English (Saint Lucia)",
    "en_MO": "English (Macau)",
    "en_MS": "English (Montserrat)",
    "en_MU": "English (Mauritius)",
    "en_NA": "English (Namibia)",
    "en_NF": "English (Norfolk Island)",
    "en_NG": "English (Nigeria)",
    "en_NR": "English (Nauru)",
    "en_NU": "English (Niue)",
    "en_PH": "English (Philippines)",
    "en_PK": "English (Pakistan)",
    "en_SC": "English (Seychelles)",
    "en_SG": "English (Singapore)",
    "en_SL": "English (Sierra Leone)",
    "en_TC": "English (Turks and Caicos Islands)",
    "en_TK": "English (Tokelau)",
    "en_TL": "English (Timor-Leste)",
    "en_TT": "English (Trinidad and Tobago)",
    "en_US": "English (United States)",
    "en_VC": "English (Saint Vincent and the Grenadines)",
    "en_VG": "English (British Virgin Islands)",

    # --- Persian / Pashto Locales ---
    "fa_AF": "Persian (Afghanistan)",
    "fa_IR": "Persian (Iran)",
    "ps_AF": "Pashto (Afghanistan)",

    # --- French Locales ---
    "fr_BI": "French (Burundi)",
    "fr_BJ": "French (Benin)",
    "fr_HT": "French (Haiti)",
    "fr_NE": "French (Niger)",
    "fr_SN": "French (Senegal)",

    # --- Italian Locales ---
    "it_IT": "Italian (Italy)",

    # --- Korean Locales ---
    "ko_KP": "Korean (North Korea)",

    # --- Malay Locales ---
    "ms_MY": "Malay (Malaysia)",

    # --- Papiamento Locales ---
    "pap_AW": "Papiamento (Aruba)",
    "pap_BQ": "Papiamento (Bonaire, Sint Eustatius and Saba)",
    "pap_CW": "Papiamento (Curaçao)",

    # --- Portuguese Locales ---
    "pt_AO": "Portuguese (Angola)",
    "pt_BR": "Portuguese (Brazil)",
    "pt_CV": "Portuguese (Cabo Verde)",
    "pt_GW": "Portuguese (Guinea-Bissau)",
    "pt_MO": "Portuguese (Macau)",
    "pt_MZ": "Portuguese (Mozambique)",
    "pt_PT": "Portuguese (Portugal)",
    "pt_ST": "Portuguese (Sao Tome and Principe)",
    "pt_TL": "Portuguese (Timor Leste)",

    # --- Sinhala / Tamil Locales ---
    "si_LK": "Sinhala (Sri Lanka)",
    "ta_LK": "Tamil (Sri Lanka)",

    # --- Swedish Locales ---
    "sv_FI": "Swedish (Finland)",

    # --- Urdu Locales ---
    "ur_PK": "Urdu (Pakistan)",

    # --- Chinese Locales ---
    "zh_CN": "Chinese (Simplified)",
    "zh_HK": "Chinese (Hong Kong)",
    "zh_MO": "Chinese (Macau)",
    "zh_TW": "Chinese (Traditional)",
}