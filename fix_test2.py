content = open('tests/countries/test_india.py', encoding='utf-8').read()

# Add Bohag Bihu in Apr 15
old1 = '            ("2018-04-15",'
new1 = '            ("2018-04-15", "Bohag Bihu; Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh"),'

# Add Indigenous Faith Day in Dec 1
old2 = '            ("2018-12-01", "Nagaland State Inauguration Day"),'
new2 = '            ("2018-12-01", "Indigenous Faith Day; Nagaland State Inauguration Day"),'

if old2 in content:
    content = content.replace(old2, new2)
    open('tests/countries/test_india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')