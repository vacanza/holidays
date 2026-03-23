content = open('tests/countries/test_india.py', encoding='utf-8').read()

old = '            ("2018-02-20", "Mizoram State Day"),'
new = '            ("2018-02-20", "Arunachal Pradesh Statehood Day; Mizoram State Day"),'

if old in content:
    content = content.replace(old, new)
    open('tests/countries/test_india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')