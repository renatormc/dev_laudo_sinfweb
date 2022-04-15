import argparse
import shutil
import os
from pathlib import Path
import subprocess

def copy_item(from_: Path, to: Path):
    if from_.is_dir():
        try:
            shutil.rmtree(to)
        except FileNotFoundError:
            pass
        shutil.copytree(from_, to)
    else:
        try:
           to.unlink()
        except FileNotFoundError:
            pass
        shutil.copy(from_, to)

script_dir = Path(os.path.dirname(os.path.realpath(__file__))).absolute()
app_dir = script_dir.parent

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode")
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_prepare = subparsers.add_parser("prepare")
p_prepare.add_argument("direction", choices=("up", "down"), help="Direction up or down")

p_dist = subparsers.add_parser("dist")

p_copy_libs = subparsers.add_parser("copy-libs")

args = parser.parse_args()

if args.command == "prepare":
    if args.direction == "up":
        shutil.rmtree(app_dir / "fastdoc/models_example")
        shutil.copytree(app_dir / "models", app_dir / "fastdoc/models_example")
    elif args.direction == "down":
        shutil.rmtree(app_dir / "models")
        shutil.copytree(app_dir / "fastdoc/models_example", app_dir / "models")
elif args.command == "dist":
    path_to = app_dir.parent / "dist"
    itens = ['models', 'fastdoc', 'main.py']
    for item in itens:
        path = app_dir / item
        copy_item(path, path_to / item)

    requirement_to = path_to / 'requirements.txt'
    subprocess.run(["poetry", 'export', '-f', 'requirements.txt', '--output', str(requirement_to)], shell=True)
    python = path_to / "programs/Python/python.exe"
    subprocess.run([str(python), '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run([str(python), '-m', 'pip', 'install', '-r',str(requirement_to)])
elif args.command == "copy-libs":
    aux = os.getenv("PYTHON_LOCAL_LIBS_FOLDER")
    if not aux:
        raise Exception("Env variable PYTHON_LOCAL_LIBS_FOLDER not set.")
    libs_folder = Path(aux)
    to_folder = Path("./libs/report_writer")
    print(libs_folder)
    print("Copying report_writer")
    args_ = ['rclone', '--filter-from', str(script_dir / 'rclone_filter.txt'),
                   'sync', str(libs_folder / "report_writer"), str(to_folder)]
    if args.verbose:
        args_.append("-v")
    subprocess.run(args_)
