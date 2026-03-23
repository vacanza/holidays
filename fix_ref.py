content = open('holidays/countries/india.py', encoding='utf-8').read()

old = '        * Tamil Nadu:'
new = '        * Arunachal Pradesh:\n            * <https://www.northeastjob.in/2025/04/arunachal-pradesh-holiday-list.html>\n        * Tamil Nadu:'

if old in content:
    content = content.replace(old, new)
    open('holidays/countries/india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')