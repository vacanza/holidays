content = open('holidays/countries/india.py', encoding='utf-8').read()

old = '        # Dr. B. R. Ambedkar Jayanti.\n        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar\'s Jayanti"))\n\n    # Assam.'

new = '        # Bohag Bihu.\n        self._add_holiday_apr_15(tr("Bohag Bihu"))\n        # Dr. B. R. Ambedkar Jayanti.\n        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar\'s Jayanti"))\n        # Indigenous Faith Day.\n        self._add_holiday_dec_1(tr("Indigenous Faith Day"))\n\n    # Assam.'

if old in content:
    content = content.replace(old, new)
    open('holidays/countries/india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Text not found!')