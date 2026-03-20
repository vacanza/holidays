from pathlib import Path
import polib

for po_path in Path('holidays/locale').rglob('*.po'):
    mo_path = po_path.with_suffix('.mo')
    po_file = polib.pofile(str(po_path))
    po_file.save_as_mofile(str(mo_path))
print('compiled', sum(1 for _ in Path('holidays/locale').rglob('*.mo')), 'mo files')
