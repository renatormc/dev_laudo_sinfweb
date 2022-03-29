from pathlib import Path
import sys
from PyQt5.QtWidgets import QApplication
from gui_app.main_window import MainWindow

app = QApplication(sys.argv)
# app.setStyle("fusion")
# app.setWindowIcon(get_icon("icon.png"))
w = MainWindow()
w.show()
sys.exit(app.exec_())
