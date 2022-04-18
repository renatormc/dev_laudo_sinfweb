import os
from pathlib import Path
import subprocess
import sys

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
python_exe = Path(sys.executable)
git_exe =  (app_dir / "../../extras/GitPortable/App/Git/bin/git.exe").absolute()

subprocess.check_output([str(git_exe), 'reset', '--hard'])
subprocess.check_output([str(git_exe), 'checkout', 'master'])
subprocess.check_output([str(git_exe), 'pull','origin', 'master'])

subprocess.check_output([str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"])


