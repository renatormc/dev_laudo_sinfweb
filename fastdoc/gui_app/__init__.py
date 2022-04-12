import os
from PyQt5.QtWidgets import QApplication
from .main_window import MainWindow
import sys
from fastdoc import config


def run_gui_app():
    app = QApplication(sys.argv)
    if os.name == "nt":
        app.setStyle("fusion")  # type: ignore
    w = MainWindow()
    if config.debug:
        w.show()
    else:
        w.showMaximized()
    sys.exit(app.exec_())