from . import config
import subprocess
import shutil

def prepare(direction: str):
    if direction == "up":
        shutil.rmtree(config.app_dir / "fastdoc/models_example")
        shutil.copytree(config.app_dir / "models", config.app_dir / "fastdoc/models_example")
    elif direction == "down":
        shutil.rmtree(config.app_dir / "models")
        shutil.copytree(config.app_dir / "fastdoc/models_example", config.app_dir / "models")

def dist():
    path_to = config.app_dir.parent / "dist"
    subprocess.run(["poetry", 'export', '-f', 'requirements.txt', '--output', 'requirements.txt'], shell=True)
    shutil.copy(config.app_dir / "fastdoc/updater/updater.py", path_to / "programs/updater.py")
    shutil.copy(config.app_dir / "fastdoc/updater/fastdoc_update.bat", path_to / "fastdoc_update.bat")
    path_original_python = path_to.parent / "original_python"
    subprocess.check_output(['rclone', 'sync', '-v', str(path_original_python), path_to / "programs/Python"])
    try:
        shutil.rmtree(path_to / "fastdoc")
    except FileNotFoundError:
        pass
    



