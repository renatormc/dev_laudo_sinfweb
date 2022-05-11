import argparse
from pathlib import Path
import sys
from fastdoc import config
import shutil
from InquirerPy import inquirer
from dotenv import load_dotenv
import os
import stat

load_dotenv() 

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workdir', help='Work directory')
parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode")
parser.add_argument('--debug', action="store_true", help="Debug mode")
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')

p_start = subparsers.add_parser("start")

p_render = subparsers.add_parser("render")
p_render.add_argument("-m", "--model", default="choose", help="Model")

p_web = subparsers.add_parser("web")
p_web.add_argument("--qt", action="store_true", help="Open qt server intead of cli")

p_gui = subparsers.add_parser("gui")

p_new_model = subparsers.add_parser("new-model")

p_delete_model = subparsers.add_parser("delete-model")

p_install = subparsers.add_parser("install")


p_analise_models_folder = subparsers.add_parser("analise-models-folder")

p_version = subparsers.add_parser("version")

p_change_version = subparsers.add_parser("change-version")

args = parser.parse_args()
config.verbose = args.verbose
config.debug = args.debug

if args.command == "start":
    shutil.copytree(config.models_example_folder, config.models_folder)
    sys.exit()

from fastdoc.helpers import fix_imports, model_name_to_folder_name
fix_imports()

import fastdoc.helpers as hp
import models
from fastdoc.app_flask import app as app_flask
from fastdoc.app_flask.gui_server import run_server
from fastdoc.gui_app import run_gui_app
from database import db, repo
from fastdoc.helpers.update import get_local_version_info, get_remote_version_info, set_local_version
from fastdoc.helpers.models_manager import fix_old_models

if args.workdir:
    config.workdir = Path(args.workdir).absolute()
    if not config.workdir.exists():
        raise Exception(f"The directory \"{config.workdir}\" doesn't exist.")
    repo.save_last_workdir(config.workdir)
else:
    config.workdir = repo.get_last_workdir()

match args.command:
    case "render":
        if args.model == "choose":
            args.model = hp.choose_model()
        md = getattr(models, args.model)
        context = context = md.test_data.get_context()
        hp.render_doc(args.model, context, "compilado.docx")
        print("Renderizado arquivo compilado.docx")
    case "new-model":
        full_name = inquirer.text(message="Nome:").execute()
        folder_name = model_name_to_folder_name(full_name)
        folder_from = config.app_dir / "models_example/example"
        folder_to = config.models_folder / folder_name
        shutil.copytree(folder_from, folder_to)
        hp.update_model_meta(folder_name, {'full_name': full_name})
        hp.fix_imports()
    case "delete-model":
        model = hp.choose_model()
        try:
            path = config.models_folder / model
            shutil.rmtree(path)
        except FileNotFoundError:
            pass
        hp.fix_imports()
    case "web":
        if args.qt:
            run_server()
        else:
            app_flask.run(host='0.0.0.0', port=5000, debug=config.debug)
    case "gui":
        run_gui_app()
    case "install":
        if os.name == "nt":
            pythonexe = sys.executable
            scriptPath = Path("./main.py").absolute()
            # text = f"@echo off\n\"{path}\" %*"
            text = f"@echo off\n\"{pythonexe}\" \"{scriptPath}\" %*"
            dest_file = Path("C:\\Windows\\fastdoc.bat")
            dest_file.write_text(text)
        else:
            pythonexe = Path("./.venv/bin/python").absolute()
            scriptPath = Path("./main.py").absolute()
            path = Path().home() / ".local/bin/fastdoc"
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            text = f"#!/bin/bash\n\"{pythonexe}\" \"{scriptPath}\" $@"
            path.write_text(text)
            st = os.stat(path)
            os.chmod(path, st.st_mode | stat.S_IEXEC)
            print("Program installed.")
            print("Make sure the folder ~/.local/bin is in your PATH")
    case "analise-models-folder":
        fix_old_models()
    case "version":
        info_remote = get_remote_version_info()
        info_local = get_local_version_info()
        print(f"Current version: {info_local['version']}. Available version: {info_remote['version']}")
    case "change-version":
        info_local = get_local_version_info()
        print(f"Current version: {info_local['version']}")
        new_version = input("New version: ")
        set_local_version(new_version)
