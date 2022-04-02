import argparse
import os
from pathlib import Path
import sys
from fastdoc import config
import shutil
from InquirerPy import inquirer
import unidecode

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workdir', default='.', help='Work directory')
parser.add_argument('-v', '--verbose', action="store_true",
                    help="Verbose mode")
subparsers = parser.add_subparsers(
    dest="command", required=True, help='Command to be used')

p_start = subparsers.add_parser("start")

p_render = subparsers.add_parser("render")
p_render.add_argument("-m", "--model", default="choose", help="Model")

p_GUI = subparsers.add_parser("gui")

p_new_model = subparsers.add_parser("new-model")

p_delete_model = subparsers.add_parser("delete-model")

args = parser.parse_args()
config.workdir = Path(args.workdir)
config.verbose = args.verbose

if args.command == "start":
    shutil.copytree(config.models_example_folder, config.models_folder)
    sys.exit()

from PyQt5.QtWidgets import QApplication
import fastdoc.helpers as hp
import stringcase
import models

if args.command == "render":
    if args.model == "choose":
        args.model = hp.choose_model()
    md = getattr(models, args.model)
    context = context = md.test_data.context
    hp.render_doc(args.model, context, "compilado.docx")
    print("Renderizado arquivo compilado.docx")
elif args.command == "gui":
    from PyQt5.QtWidgets import QApplication
    from fastdoc.gui_app.main_window import MainWindow

    app = QApplication(sys.argv)
    if os.name == "nt":
        app.setStyle("fusion")  # type: ignore
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
elif args.command == "new-model":
    full_name = inquirer.text(message="Nome:").execute()
    folder_name = stringcase.snakecase(unidecode.unidecode(full_name))
    folder_from = config.app_dir / "models_example/example"
    folder_to = config.models_folder / folder_name
    shutil.copytree(folder_from, folder_to)
    hp.set_model_meta(folder_name, full_name=full_name)
    hp.fix_imports()
elif args.command == "delete-model":
    model = hp.choose_model()
    try:
        path = config.models_folder / model
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
    hp.fix_imports()
