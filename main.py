import argparse
from pathlib import Path
import sys
from PyQt5.QtWidgets import QApplication
import helpers as hp
import stringcase
import config
import shutil
import models

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workdir', default='.', help='Work directory')
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')


p_render = subparsers.add_parser("render")
p_render.add_argument("-m", "--model", default="choose", help="Model")

p_GUI = subparsers.add_parser("gui")

p_new_model = subparsers.add_parser("new-model")

p_delete_model = subparsers.add_parser("delete-model")

args = parser.parse_args()
config.workdir = Path(args.workdir)
    
if args.command == "render":
    if args.model == "choose":
        args.model = hp.choose_model()
    md = getattr(models, args.model)
    context = context = md.test_data.context
    print(context)
    hp.render_doc(args.model, context)
    print("Renderizado arquivo compilado.docx")
elif args.command == "gui":
    from PyQt5.QtWidgets import QApplication
    from gui_app.main_window  import MainWindow
    
    app = QApplication(sys.argv)
    # app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
elif args.command == "new-model":
    answers = hp.inquire_new_model()
    full_name = answers['full_name']
    folder_name = stringcase.snakecase(full_name)
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
    
