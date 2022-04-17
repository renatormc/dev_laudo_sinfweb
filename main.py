import subprocess
import argparse
from pathlib import Path
import sys
from fastdoc import config
import shutil
from InquirerPy import inquirer

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workdir', default='.', help='Work directory')
parser.add_argument('-v', '--verbose', action="store_true",
                    help="Verbose mode")
parser.add_argument('--debug', action="store_true",
                    help="Debug mode")
subparsers = parser.add_subparsers(
    dest="command", required=True, help='Command to be used')

p_start = subparsers.add_parser("start")

p_render = subparsers.add_parser("render")
p_render.add_argument("-m", "--model", default="choose", help="Model")

p_web = subparsers.add_parser("web")
p_web.add_argument("--qt", action="store_true", help="Open qt server intead of cli")

p_gui = subparsers.add_parser("gui")

p_new_model = subparsers.add_parser("new-model")

p_delete_model = subparsers.add_parser("delete-model")

p_install = subparsers.add_parser("install")

p_update = subparsers.add_parser("update")

p_publish = subparsers.add_parser("publish")

args = parser.parse_args()
config.workdir = Path(args.workdir)
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
from database import db


db.init_db()

if args.command == "render":
    if args.model == "choose":
        args.model = hp.choose_model()
    md = getattr(models, args.model)
    context = context = md.test_data.get_context()
    hp.render_doc(args.model, context, "compilado.docx")
    print("Renderizado arquivo compilado.docx")
elif args.command == "new-model":
    full_name = inquirer.text(message="Nome:").execute()
    folder_name = model_name_to_folder_name(full_name)
    folder_from = config.app_dir / "models_example/example"
    folder_to = config.models_folder / folder_name
    shutil.copytree(folder_from, folder_to)
    hp.update_model_meta(folder_name, {'full_name': full_name})
    hp.fix_imports()
elif args.command == "delete-model":
    model = hp.choose_model()
    try:
        path = config.models_folder / model
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
    hp.fix_imports()
elif args.command == "web":
    if args.qt:
        run_server()
    else:
        app_flask.run(host='0.0.0.0', port=5000, debug=config.debug)
elif args.command == "gui":
    run_gui_app()
elif args.command == "install":
    path = Path("./fastdoc.bat").absolute()
    text = f"@echo off\n\"{path}\" %*"
    dest_file = Path("C:\\Windows\\fastdoc.bat")
    dest_file.write_text(text)
elif args.command == "update":
    rclone_exe = config.main_script_dir / "rclone-v1.58.0-windows-amd64/rclone.exe"
    subprocess.Popen([str(rclone_exe), 'sync', '-v', config.local_data['shared_folder'], str(config.main_script_dir)])
elif args.command == "publish":
    dest = config.local_data['shared_folder']
    input(f"Copiar para \"{dest}\"? Pressione algo para continuar.")
    rclone_exe = config.main_script_dir / "dist_start/rclone-v1.58.0-windows-amd64/rclone.exe"
    subprocess.Popen(
        [str(rclone_exe), 'sync', '-v', str(config.main_script_dir / "dist"), config.local_data['shared_folder']])
