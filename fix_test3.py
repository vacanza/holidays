content = open('tests/countries/test_india.py', encoding='utf-8').read()

old = '                "Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",'
new = '                "Bohag Bihu; Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",'

if old in content:
    content = content.replace(old, new)
    open('tests/countries/test_india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')