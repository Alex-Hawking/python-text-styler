import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('main.py', base=base, icon='icon.ico', targetName='Text Styler.exe', shortcutName="Text Styler",
            shortcutDir="DesktopFolder",)
]

includefiles = ["icon.ico", "textStuff.py"]

setup(
    name='TextStyler',
    package_data={
        'Text Styler': includefiles,
    },
    version='0.1',
    description='A Simple App That Styles Text',
    author = "Alex Hawking",
    options = {
        'build_exe': {'include_files':includefiles},
        'bdist_msi': {
            'install_icon': 'icon.ico',
            'target_name': 'Text Styler Installer'
        }
    },
    executables=executables
)

