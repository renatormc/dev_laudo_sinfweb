import os
from PyQt5.QtWidgets import QApplication
from .main_window import MainWindow
import sys


def run_gui_app():
    app = QApplication(sys.argv)
    if os.name == "nt":
        app.setStyle("fusion")  # type: ignore
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())