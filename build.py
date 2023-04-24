from os import system as osSystem
# Just add or remove values to this list based on the imports you don't want : )
excluded_modules = [
    'PySide6',
    'PIL',
    'tk',
    'tcl',
    'tcl8'
]

append_string = ''
for mod in excluded_modules:
    append_string += f' --exclude-module {mod}'

# Run the shell command with all the exclude module parameters
osSystem(f'pyinstaller main.py --name=ScreenRecorder_Lite --console --onefile --noconfirm {append_string}')