content = open('tests/countries/test_india.py', encoding='utf-8').read()

old = '"Bohag Bihu; Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh"'
new = '"Bohag Bihu; Himachal Day; "\n                "Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh"'

new_content = content.replace(old, new)
open('tests/countries/test_india.py', 'w', encoding='utf-8').write(new_content)
print("Done! Replacements made:", content.count(old))