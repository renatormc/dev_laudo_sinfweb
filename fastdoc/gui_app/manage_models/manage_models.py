from .manage_models_ui import Ui_ManageModels
from PyQt5.QtWidgets import QDialog, QFileDialog
from fastdoc.helpers import get_models_info


class ManageModelsDialog(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_ManageModels()
        self.ui.setupUi(self)
        self.connections()
        self.populate_models()

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
        file_, _ = QFileDialog.getOpenFileName(self, "Escolha um arquivo", "","All Files (*);;Zip Files (*.zip)")

    def export_model(self):
        pass

    def remove_model(self):
        pass
