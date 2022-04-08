import argparse
import shutil
import os
from pathlib import Path
import subprocess
import report_writer

app_dir = Path(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_prepare = subparsers.add_parser("prepare")
p_prepare.add_argument("direction", choices=("up", "down"), help="Direction up or down")

p_to_sinftools = subparsers.add_parser("to-sinftools")

args = parser.parse_args()

if args.command == "prepare":
    if args.direction == "down":
        shutil.rmtree(app_dir / "fastdoc/models_example")
        shutil.copytree(app_dir / "models", app_dir / "fastdoc/models_example")
    elif args.direction == "up":
        shutil.rmtree(app_dir / "models")
        shutil.copytree(app_dir / "fastdoc/models_example", app_dir / "models")
elif args.command == "to-sinftools":
    aux = os.getenv("SINFTOOLS")
    if not aux:
        raise Exception("SINFTOOLS variable not found")
    sinftools_dir = Path(aux)
    path_to = sinftools_dir / "tools/fastdoc"
    itens = ['models', 'fastdoc', 'main.py']
    try:
        shutil.rmtree(path_to)
    except FileNotFoundError:
        pass
    path_to.mkdir()
    for item in itens:
        path = app_dir / item
        if path.is_dir():
            shutil.copytree(path, path_to / item)
        else:
            shutil.copy(path, path_to / item)
    path_from = Path(report_writer.__file__).parent
    shutil.copytree(path_from, path_to / "report_writer")