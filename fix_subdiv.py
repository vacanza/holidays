content = open('tests/countries/test_india.py', encoding='utf-8').read()

old = '            "AN": ("2018-04-14",),'
new = '''            "AN": ("2018-04-14",),
            "AR": (
                "2018-02-20",
                "2018-04-14",
                "2018-04-15",
                "2018-12-01",
            ),'''

if old in content:
    content = content.replace(old, new)
    open('tests/countries/test_india.py', 'w', encoding='utf-8').write(content)
    print('Done!')
else:
    print('Not found!')