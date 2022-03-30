from pathlib import Path
from typing import Optional
from helpers import render_doc, get_models_list
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
        self.form: Optional[Form] = None
        self.populate_models()
        
        # self.form = self.create_form()
        

    def connections(self):
        self.ui.btn_render.clicked.connect(self.render)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_load.clicked.connect(self.load)
        self.ui.cbx_model.currentTextChanged.connect(self.create_form)
        self.ui.btn_clear.clicked.connect(self.clear_content)

    def populate_models(self):
        self.ui.cbx_model.clear()
        models = get_models_list()
        self.ui.cbx_model.addItems(models)

    def setup_ui(self):
        self.setWindowIcon(get_icon("icon.png"))
        self.ui.btn_save.setIcon(get_icon("save.png"))
        self.ui.btn_save.setIconSize(QSize(32, 32))
        self.ui.btn_load.setIcon(get_icon("load.png"))
        self.ui.btn_load.setIconSize(QSize(20, 20))
        self.ui.btn_render.setIcon(get_icon("docx.png"))
        self.ui.btn_render.setIconSize(QSize(20, 20))
        self.ui.btn_clear.setIcon(get_icon("clear.png"))
        self.ui.btn_clear.setIconSize(QSize(32, 32))

    def create_form(self):
        if self.form is not None:
            file_ = config.local_folder / f"{self.form.model}.json"
            self.form.save(file_)
        model = self.ui.cbx_model.currentText()
        md = getattr(models, model)
        widgets = md.form.widgets
        self.form =  Form(model, widgets)
        self.ui.sca_form.setWidget(self.form)
        file_ = config.local_folder / f"{self.form.model}.json"
        if Path(file_).exists():
            self.form.load(file_)
        else:
            self.form.clear_content()
        

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

    def clear_content(self):
        self.form.clear_content()


