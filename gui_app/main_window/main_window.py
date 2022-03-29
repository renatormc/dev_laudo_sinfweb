from gui_app.main_window.main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from gui_app.form import Form
import config
import models


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()
        # self.create_form()
        self.form = self.create_form()
        # md = getattr(models, config.model)
        # widgets = md.form.widgets
        self.ui.lay_form.addWidget(self.form)

    def connections(self):
        self.ui.btn_render.clicked.connect(self.render)

    @staticmethod
    def create_form() -> Form:
        md = getattr(models, config.model)
        widgets = md.form.widgets
        return Form(widgets)

    def render(self):
        errors = self.form.validate()
        if errors:
            print(errors)
            return
        context = self.form.get_context()
        print(context)
