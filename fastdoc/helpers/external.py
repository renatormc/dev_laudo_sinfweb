from pathlib import Path
import subprocess
import os

def open_in_filemanager(path: str|Path) -> None:
    filemanagers = ['explorer'] if os.name == "nt" else ['nautilus', 'nemo','dolphin']
    for item in filemanagers:
        try:
            subprocess.Popen([item, str(path)])
            break
        except FileNotFoundError:
            pass

def open_in_text_editor(path: str|Path) -> None:
    items = ['notepad++', 'notepad'] if os.name == 'nt' else ['gedit', 'kate', 'xed']
    for item in items:
        try:
            subprocess.run([item, str(path)])
            break
        except FileNotFoundError:
            pass