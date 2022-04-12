from pathlib import Path
import shutil
from fastdoc.custom_types import ModelInfo
from .manage_models_ui import Ui_ManageModels
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5.QtCore import QSize
from fastdoc.helpers import get_models_info
from fastdoc import config
from fastdoc.helpers.zip import zip_folder, unzip_file
from fastdoc.helpers import model_name_to_folder_name, find_model_meta_by_folder, fix_imports
from fastdoc.gui_app.helpers import ask_confirmation, get_icon


class ManageModelsDialog(QDialog):
    def __init__(self, parent):
        self.parent = parent
        super(self.__class__, self).__init__(parent)
        self.ui = Ui_ManageModels()
        self.ui.setupUi(self)
        self.setup_ui()
        self.connections()
        self.populate_models()

    def setup_ui(self):
        self.ui.btn_import.setIcon(get_icon("import.png"))
        self.ui.btn_import.setIconSize(QSize(22, 22))
        self.ui.btn_export.setIcon(get_icon("export.png"))
        self.ui.btn_export.setIconSize(QSize(22, 22))
        self.ui.btn_remove.setIcon(get_icon("delete.jpg"))
        self.ui.btn_remove.setIconSize(QSize(22, 22))


    def connections(self):
        self.ui.btn_import.clicked.connect(self.import_model)
        self.ui.btn_export.clicked.connect(self.export_model)
        self.ui.btn_remove.clicked.connect(self.remove_model)

    def populate_models(self):
        self.ui.cbx_model.clear()
        models = get_models_info('qt')
        for mi in models:
            self.ui.cbx_model.addItem(mi.meta['full_name'], mi)
        
    def import_model(self):
        file_, _ = QFileDialog.getOpenFileName(self, "Escolha um arquivo", "","Zip Files (*.zip)")
        if file_:
            try:
                folder = unzip_file(file_)
                meta = find_model_meta_by_folder(folder)
                model_name = model_name_to_folder_name(meta['full_name'])
                folder_to = config.models_folder / model_name
                if folder_to.exists():
                    ok = ask_confirmation(self, "Atenção!", f"Já existe um modelo de nome \"{folder_to}\". Deseja sobrescrevê-lo?")
                    if ok:
                        shutil.rmtree(folder_to)     
                    else:
                        return    

                shutil.move(folder, folder_to)
                fix_imports()
                self.populate_models()
                QMessageBox.about(self, "Sucesso", "Modelo importado com sucesso!")

            finally:
                if folder.exists():
                    shutil.rmtree(folder)

    def export_model(self):
        mi: ModelInfo = self.ui.cbx_model.currentData()
        file_, _ = QFileDialog.getSaveFileName(self, "Escolha um arquivo", f"{mi.name}.zip","Zip Files (*.zip)")
        if file_:
            path_from = config.models_folder / mi.name
            zip_folder(str(path_from), file_)
            QMessageBox.about(self, "Sucesso", "Modelo exportado com sucesso!")
            


    def remove_model(self):
        mi: ModelInfo = self.ui.cbx_model.currentData()
        ok = ask_confirmation(self, "Tem certeza?", f"Tem certeza que deseja deletar o modelo \"{mi.meta['full_name']}\"?")
        if ok:
            folder_to = config.models_folder / mi.name
            shutil.rmtree(folder_to)
            fix_imports()
            self.populate_models()