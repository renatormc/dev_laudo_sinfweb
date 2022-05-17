import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

from report_writer import ReportWriter
from fastdoc.custom_types import ModelInfo
from fastdoc.helpers import open_doc, render_doc, get_models_info
from fastdoc.gui_app.main_window.main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QSize, QThread, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QShowEvent
from fastdoc.gui_app.form import Form
from fastdoc import config
import importlib
from report_writer.types import InitialData
from fastdoc.gui_app.helpers import ask_confirmation, get_icon
from fastdoc.gui_app.manage_models import ManageModelsDialog
from fastdoc.gui_app.main_window.dialog_token import DialogToken
from database import repo
import traceback
from fastdoc.helpers.update import has_newer_version
from fastdoc.gui_app.about_dialog import AboutDialog
from fastdoc.preferences import PreferencesManager


class Worker(QObject):
    finished = pyqtSignal()
    error_occurered = pyqtSignal(Exception)
    doc_rendered = pyqtSignal(str)

    def __init__(self, model_name: str, context, file_: Path) -> None:
        super().__init__()
        self.model_name = model_name
        self.context = context
        self.file = file_

    def run(self):
        try:
            render_doc(self.model_name, self.context, self.file)
            self.doc_rendered.emit(str(self.file))
        except Exception as e:
            self.error_occurered.emit(e)
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_buttons_enable(False)
        self.setup_ui()
        self.connections()
        self.form: Optional[Form] = None
        self.populate_models()
        self.initial_data: Optional[InitialData] = None
        self.ui.led_workdir.setText(str(config.workdir))
        self._thread: Optional[QThread] = None
        self.worker: Optional[Worker] = None

    def connections(self):
        self.ui.btn_render.clicked.connect(self.render)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_load.clicked.connect(self.load)
        self.ui.cbx_model.currentTextChanged.connect(self.create_form)
        self.ui.btn_clear.clicked.connect(self.clear_content)
        self.ui.btn_initial_data.clicked.connect(self.load_initial_data)
        self.ui.act_manage_models.triggered.connect(self.manage_models)
        self.ui.act_add_token.triggered.connect(self.add_token)
        self.ui.btn_choose_workdir.clicked.connect(self.choose_workdir)
        self.ui.act_about.triggered.connect(self.show_about_dialog)
        self.ui.act_dev.triggered.connect(self.open_ide)
        self.ui.act_preferences.triggered.connect(self.open_preferences)
        self.ui.btn_load_last.clicked.connect(self.load_last_data)

    def populate_models(self):
        self.ui.cbx_model.clear()
        models = get_models_info('qt')
        for mi in models:
            self.ui.cbx_model.addItem(mi.meta['full_name'], mi)

    def setup_ui(self):
        self.setWindowIcon(get_icon("app_icon.png"))
        self.ui.btn_save.setIcon(get_icon("save.png"))
        self.ui.btn_save.setIconSize(QSize(22, 22))
        self.ui.btn_load.setIcon(get_icon("load.png"))
        self.ui.btn_load.setIconSize(QSize(20, 20))
        self.ui.btn_render.setIcon(get_icon("docx.png"))
        self.ui.btn_render.setIconSize(QSize(20, 20))
        self.ui.btn_clear.setIcon(get_icon("clear.png"))
        self.ui.btn_clear.setIconSize(QSize(34, 34))
        self.ui.btn_initial_data.setIcon(get_icon("initial_data.png"))
        self.ui.btn_initial_data.setIconSize(QSize(32, 32))
        self.ui.btn_load_last.setIcon(get_icon("undo.png"))
        self.ui.btn_load_last.setIconSize(QSize(28, 28))

    def set_buttons_enable(self, value: bool) -> None:
        self.ui.btn_clear.setEnabled(value)
        self.ui.btn_initial_data.setEnabled(value)
        self.ui.btn_load.setEnabled(value)
        self.ui.btn_render.setEnabled(value)
        self.ui.btn_save.setEnabled(value)

    def create_form(self):            
        mi: ModelInfo = self.ui.cbx_model.currentData()
        if mi is not None:
            form_module = importlib.import_module(f"models.{mi.name}.qt_form")
            widgets = form_module.widgets
            self.form = Form(mi, widgets)
            self.ui.sca_form.setWidget(self.form)
            self.set_buttons_enable(True)
            self.form.clear_content()
            self.show_instructions(mi)
        else:
            self.set_buttons_enable(False)

    def show_instructions(self, mi: ModelInfo):
        rw = ReportWriter(config.models_folder, model_name=mi.name)
        html = rw.get_instructions_html()
        if html:
            self.ui.teb_instructions.setHtml(html)
            self.ui.teb_instructions.setVisible(True)
        else:
            self.ui.teb_instructions.setVisible(False)

    def load_initial_data(self) -> None:
        if self.form:
            mi = self.ui.cbx_model.currentData()
            initial_feeder = importlib.import_module(
                f"models.{mi.name}.initial_feeder")
            try:
                self.initial_data = initial_feeder.get_initial_data(config.workdir)
                if self.initial_data is not None:
                    self.form.load(self.initial_data.form_data)
            except Exception as e:
                traceback.print_exc()
                QMessageBox.warning(self, "Erro", str(e))

    def render_doc(self, model_name: str, context, file_: Path) -> None:
        self._thread = QThread()
        self.worker = Worker(model_name, context, file_)
        self.worker.moveToThread(self._thread)
        self._thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._thread.quit)
        self.worker.doc_rendered.connect(self.finish_render)
        self.worker.error_occurered.connect(self.render_error)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self._thread.start()

    def finish_render(self, file_):
        QApplication.restoreOverrideCursor()
        if os.name == "nt":
            reply = QMessageBox.question(self, "Arquivo compilado",
                                         "Arquivo compilado. Deseja abri-lo no seu editor de textos padrão?",
                                         QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                open_doc(file_)
        else:
            QMessageBox.about(self, "Arquivo compilado", f"Arquivo compilado \"{file_}\"")

    def render_error(self, e):
        traceback.print_exc()
        QApplication.restoreOverrideCursor()
        QMessageBox.warning(self, "Erro", str(e))

    def render(self):
        self.form.save_last_data()
        # self.form.save_to_file(file_)
        context, errors = self.form.get_context()
        if config.debug:
            print(context)
        if errors:
            QMessageBox.warning(self, "Erro de formulário",
                                "Há erros em seu formulário. Corrija-os antes de prosseguir.")
            return
        if self.initial_data:
            context.update(self.initial_data.context)

        p = PreferencesManager.instance()
        if not p.preferences["doc_in_workdir"]:
            file_ = QFileDialog.getSaveFileName(self, "Escolha o arquivo",  ".", "DOCX (*.docx)")[0]
        else:
            file_ = config.workdir / p.preferences["doc_default_name"]
        if file_:
            self.render_doc(self.form.model_info.name, context, file_)

       
    def save(self):
        self.form.save_to_file()

    def load(self):
        self.form.load_from_file()

    def load_last_data(self):
        self.form.load_last_data()

    def clear_content(self):
        self.form.clear_content()

    def manage_models(self):
        dialog = ManageModelsDialog(self)
        dialog.exec_()
        self.populate_models()

    def add_token(self):
        dialog = DialogToken(self)
        ok = dialog.exec_()
        if ok:
            repo.save_token(dialog.name, dialog.token)
            QMessageBox.about(self, "Sucesso", "Token salvo com sucesso!")

    def choose_workdir(self):
        path = Path(self.ui.led_workdir.displayText())
        dir_ = QFileDialog.getExistingDirectory(self, "Escolher diretóriod e trabalho", str(path))
        if dir_:
            path = Path(dir_)
            config.workdir = path
            self.ui.led_workdir.setText(str(path))
            repo.save_last_workdir(path)

    def showEvent(self, a0: QShowEvent) -> None:
        if config.SELF_CONTAINED:
            res, info_remote = has_newer_version()
            if res:
                res = ask_confirmation(
                    self, "Nova versão disponível",
                    f"Seu programa está desatualizado. A versão {info_remote['version']} está disponível. Gostaria de atualizar?")
                if res:
                    path = config.main_script_dir / "fastdoc_update.bat"
                    subprocess.Popen(['cmd', '/k', str(path)])
                    sys.exit()
        return super().showEvent(a0)

    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec_()

    def open_ide(self):
        try:
            subprocess.Popen(['code', str(config.main_script_dir)], shell=True)
        except FileNotFoundError:
            filemanagers = ['explorer'] if os.name == "nt" else ['nautilus', 'nemo','dolphin']
            for item in filemanagers:
                try:
                    subprocess.Popen([item, str(config.main_script_dir)])
                    break
                except FileNotFoundError:
                    pass

    def open_preferences(self):
        PreferencesManager.instance().edit_preferences()
