import subprocess
from pathlib import Path
import os
import shutil
import zipfile
import sys

script_dir = Path(os.path.dirname(os.path.realpath(__file__))).absolute()

def zip_folder(folder_path: str, output_path: str) -> None:
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(folder_path + os.sep, '')
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(folder_path + os.sep, '')

                zip_file.write(absolute_path, relative_path)
    finally:
        zip_file.close()


folder = Path(sys.argv[1])
folders = [folder / ".local", folder / ".vscode", folder / "models"]
for f in folders:
    try:
        shutil.rmtree(f)
    except FileNotFoundError:
        pass
files = [folder / "db.db"]
for f in files:
    try:
        f.unlink()
    except FileNotFoundError:
        pass


shutil.copytree(folder / "fastdoc/models_example", folder / "models")

zip_folder(str(folder), str(folder.parent / "fastdoc.zip"))