from pathlib import Path
from . import config
import shutil
from fastdoc.helpers.zip import zip_folder
from fastdoc.helpers.update import get_local_version_info


def prepare(direction: str):
    if direction == "up":
        shutil.rmtree(config.app_dir / "fastdoc/models_example")
        shutil.copytree(config.app_dir / "models", config.app_dir / "fastdoc/models_example")
    elif direction == "down":
        shutil.rmtree(config.app_dir / "models")
        shutil.copytree(config.app_dir / "fastdoc/models_example", config.app_dir / "models")


def dist():
    path_to = config.app_dir.parent / "dist"
    # subprocess.run(["poetry", 'export', '-f', 'requirements.txt', '--output', 'requirements.txt'], shell=True)
    shutil.copy(config.app_dir / "fastdoc/updater/updater.py", path_to / "programs/updater.py")
    shutil.copy(config.app_dir / "fastdoc/updater/fastdoc_update.bat", path_to / "fastdoc_update.bat")
    # path_original_python = path_to.parent / "original_python"
    # subprocess.check_output(['rclone', 'sync', '-v', str(path_original_python), path_to / "programs/Python"])
    try:
        shutil.rmtree(path_to / "fastdoc")
    except FileNotFoundError:
        pass
    info = get_local_version_info()
    v = info['version'] #.replace(".", "_")
    file_ = config.app_dir.parent / f"fastdoc v{v}.zip"
    zip_folder(str(path_to), str(file_))
    print(f"File generated: \"{file_}\"")
