from .about_dialog_ui import Ui_AboutDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSize
from fastdoc.helpers.update import get_local_version_info
from fastdoc.gui_app.helpers import get_icon

class AboutDialog(QDialog):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.connections()
        self.show_version_and_icon()

    def connections(self):
        pass

    def show_version_and_icon(self):
        info_local = get_local_version_info()
        self.ui.lbl_version.setText(f"Version: {info_local['version']}")
        icon = get_icon("app_icon.png")
        self.ui.lbl_icon.setPixmap(icon.pixmap(QSize(60,60)))
        self.ui.lbl_github.setOpenExternalLinks(True)
        self.ui.lbl_github.setText("Código fonte: <a href=\"https://github.com/renatormc/fastdoc\">https://github.com/renatormc/fastdoc</a>")
