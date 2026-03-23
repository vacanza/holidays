content = open('tests/countries/test_india.py', encoding='utf-8').read()

# Find the last test method and add before class ends
old = '    def test_l10n_default(self):'
new = '''    def test_ar_statehood_day(self):
        name = "Arunachal Pradesh Statehood Day"
        self.assertNoHolidayName(name, India(subdiv="AR", years=1986))
        self.assertHolidayName(
            name, India(subdiv="AR"), "1987-02-20", "2018-02-20", "2025-02-20"
        )

    def test_l10n_default(self):'''

if old in content:
    content = content.replace(old, new)
    open('tests/countries/test_india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')