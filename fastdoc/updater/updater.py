import os
from pathlib import Path
import subprocess
import sys

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
gitdir = Path("fastdoc/.git")
python_exe = Path(sys.executable)
git_exe =  (app_dir / "../../extras/GitPortable/App/Git/bin/git.exe").absolute()

if gitdir.exists() and gitdir.is_dir():
    os.chdir("fastdoc")
    subprocess.check_output([str(git_exe), 'reset', '--hard'])
    subprocess.check_output([str(git_exe), 'checkout', 'master'])
    subprocess.check_output([str(git_exe), 'pull','origin', 'master'])
else:
    subprocess.check_output([str(git_exe), 'clone', 'https://github.com/renatormc/fastdoc.git'])
    os.chdir("fastdoc")

subprocess.check_output([str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"])


