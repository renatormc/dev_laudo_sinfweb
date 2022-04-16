import os
from pathlib import Path
import subprocess
import sys
import shutil

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
gitdir = Path("fastdoc/.git")
python_exe = Path(sys.executable)


if gitdir.exists() and gitdir.is_dir():
    os.chdir("fastdoc")
    subprocess.check_output(['git', 'reset', '--hard'])
    subprocess.check_output(['git', 'checkout', 'master'])
    subprocess.check_output(['git', 'pull','origin', 'master'])
else:
    subprocess.check_output(['git', 'clone', 'https://github.com/renatormc/fastdoc.git'])
    os.chdir("fastdoc")

subprocess.check_output([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_output([str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"])

path = Path("./fastdoc.bat")
try:
    path.unlink()
except FileNotFoundError:
    pass
shutil.copy(Path("./fastdoc/updater/fastdoc.bat", path))

#copy models folder
models_example = Path("./fastdoc/models_example")
models_folder = Path("./models")
if not models_folder.exists():
    shutil.copytree(models_example, models_folder)
