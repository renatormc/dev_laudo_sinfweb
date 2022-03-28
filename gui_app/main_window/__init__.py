from .main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from gui_app.form import Form
import config
import models


class MainWindow(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        # self.create_form()
        self.form = self.create_form()
        # md = getattr(models, config.model)
        # widgets = md.form.widgets
        self.setCentralWidget(self.form)

    def connections(self):
        pass

    @staticmethod
    def create_form() -> Form:
        md = getattr(models, config.model)
        widgets = md.form.widgets
        return Form(widgets)
