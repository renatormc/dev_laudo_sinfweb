import subprocess
from pathlib import Path
import os
import shutil
import zipfile
import sys
import json

script_dir = Path(os.path.dirname(os.path.realpath(__file__))).absolute()
folder = Path(sys.argv[1]).absolute()
os.chdir(folder)
subprocess.check_output(['git', 'reset', '--hard'])
subprocess.check_output(['git', 'checkout', 'master'])
subprocess.check_output(['git', 'pull','origin', 'master'])

scripts_folder = folder / "extras/Python/Scripts"
os.environ['PATH'] = f"{scripts_folder};{os.getenv('PATH')}"

python_exe = folder / "extras/Python/python.exe"
print("Atualizando libs")
subprocess.check_output([str(python_exe), '-m', 'pip', 'install', '-r', 'requirements.txt'])

def get_current_version():
    with (folder / "fastdoc/current_release.json").open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data['version']

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

subprocess.check_output([str(python_exe), 'manage.py', 'db_upgrade'])

print("Gerando zip")
zip_folder(str(folder), str(folder.parent / f"fastdoc  {get_current_version()}.zip"))