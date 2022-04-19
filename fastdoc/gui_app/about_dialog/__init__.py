from .about_dialog_ui import Ui_AboutDialog
from PyQt5.QtWidgets import QDialog

class AboutDialog(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        pass

    def show_version(self):
        pass
