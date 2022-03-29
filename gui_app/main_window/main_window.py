from helpers import render_doc
from gui_app.helpers import get_icon
from gui_app.main_window.main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
from gui_app.form import Form
import config
import models


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.connections()
        self.form = self.create_form()
        self.ui.lay_form.addWidget(self.form)

    def connections(self):
        self.ui.btn_render.clicked.connect(self.render)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_load.clicked.connect(self.load)

    def setup_ui(self):
        self.setWindowIcon(get_icon("icon.png"))
        self.ui.btn_save.setIcon(get_icon("save.png"))
        self.ui.btn_save.setIconSize(QSize(32, 32))
        self.ui.btn_load.setIcon(get_icon("load.png"))
        self.ui.btn_load.setIconSize(QSize(20, 20))
        self.ui.btn_render.setIcon(get_icon("docx.png"))
        self.ui.btn_render.setIconSize(QSize(20, 20))

    @staticmethod
    def create_form() -> Form:
        md = getattr(models, config.model)
        widgets = md.form.widgets
        return Form(widgets)

    def render(self):
        errors = self.form.validate()
        if errors:
            return
        context = self.form.get_context()
        print(context)
        render_doc(config.model, context)

    def save(self):
        self.form.save()

    def load(self):
        self.form.load()
