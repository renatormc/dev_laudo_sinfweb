import os
from pathlib import Path
from typing import Optional
from helpers import open_doc, render_doc, get_models_list, get_model_meta
from gui_app.helpers import get_icon
from gui_app.main_window.main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
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
        for m in models:
            meta = get_model_meta(m)
            self.ui.cbx_model.addItem(meta['full_name'], m)

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
        model = self.ui.cbx_model.currentData()
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
        file_ = config.local_folder / f"{self.form.model}.json"
        self.form.save(file_)
        context, errors = self.form.get_context()
        if errors:
            QMessageBox.warning(self, "Erro de formulário", "Há erros em seu formulário. Corrija-os antes de prosseguir.")
            return
        print(context)
        try:
            file_= QFileDialog.getSaveFileName(self, "Escolha o arquivo",  ".", "DOCX (*.docx)")[0]
            if file_:
                render_doc(self.form.model, context, file_)
                if os.name == "nt":
                    reply = QMessageBox.question(self, "Arquivo compilado", "Arquivo compilado. Deseja abri-lo no seu editor de textos padrão?", QMessageBox.Yes, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        open_doc(file_)
                else:
                    QMessageBox.about(self, "Arquivo compilado", f"Arquivo compilado \"{file_}\"")
        except Exception as e:
            QMessageBox.warning(self, "Erro", str(e))

    def save(self):
        self.form.save()

    def load(self):
        self.form.load()

    def clear_content(self):
        self.form.clear_content()


