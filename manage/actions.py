from . import config
from .helpers import copy_item
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
    itens = ['models', 'fastdoc', 'main.py']
    for item in itens:
        path = config.app_dir / item
        copy_item(path, path_to / item)

    requirement_to = path_to / 'requirements.txt'
    subprocess.run(["poetry", 'export', '-f', 'requirements.txt', '--output', str(requirement_to)], shell=True)
    python = path_to / "programs/Python/python.exe"
    subprocess.run([str(python), '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run([str(python), '-m', 'pip', 'install', '-r',str(requirement_to)])
