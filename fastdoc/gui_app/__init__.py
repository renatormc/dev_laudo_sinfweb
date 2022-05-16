import os
from PyQt5.QtWidgets import QApplication

from fastdoc.preferences import PreferencesManager
from .main_window import MainWindow
import sys
from fastdoc.gui_app.helpers import get_icon


def run_gui_app():
    PreferencesManager.instance().load_preferences()
    app = QApplication(sys.argv)
    if os.name == "nt":
        app.setStyle("fusion")  # type: ignore
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())