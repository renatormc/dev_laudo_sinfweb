import os
from pathlib import Path
import subprocess
import sys

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))
python_exe = Path(sys.executable)
python_folder = python_exe.parent
git_bin =  (app_dir / "../../extras/GitPortable/App/Git/bin").absolute()
current_path = os.getenv("PATH")

new_path = f"{python_folder};{python_folder / 'Scripts'};{git_bin};{current_path}"
os.environ['PATH'] = new_path

subprocess.check_output(['git', 'reset', '--hard'])
subprocess.check_output(['git', 'checkout', 'master'])
subprocess.check_output(['git', 'pull','origin', 'master'])

subprocess.check_output(['python', "-m", "pip", "install", "-r", "requirements.txt"])
subprocess.check_output(['python', "manage.py", "db_upgrade"])
subprocess.check_output(['python', "main.py", "analise-models-folder"])

print("Aplicativo atualizado com sucesso!")


