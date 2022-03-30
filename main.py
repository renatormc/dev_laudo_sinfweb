import argparse
import sys
from PyQt5.QtWidgets import QApplication
from helpers import choose_model, get_test_context
from helpers import render_doc

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help='Command to be used')


p_render = subparsers.add_parser("render")
p_render.add_argument("-m", "--model", default="choose", help="Model")
p_GUI = subparsers.add_parser("gui")

args = parser.parse_args()

    
if args.command == "render":
    if args.model == "choose":
        args.model = choose_model()
    context = get_test_context(args.model)
    render_doc(args.model, context)
    print("Renderizado arquivo compilado.docx")
elif args.command == "gui":
    from PyQt5.QtWidgets import QApplication
    from gui_app.main_window  import MainWindow
    
    app = QApplication(sys.argv)
    # app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())