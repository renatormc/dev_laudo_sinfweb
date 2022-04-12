from .dialog_token_ui import Ui_DialogToken
from PyQt5.QtWidgets import QDialog, QMessageBox

class DialogToken(QDialog):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.ui = Ui_DialogToken()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        self.ui.buttonBox.accepted.connect(self.ok_clicked)
        self.ui.buttonBox.rejected.connect(self.close)

    @property
    def name(self):
        return self.ui.led_name.displayText().strip()

    @property
    def token(self):
        return self.ui.pte_token.toPlainText().strip()

    def ok_clicked(self):
        text = self.ui.led_name.displayText().strip()
        token = self.ui.pte_token.toPlainText().strip()
        if text != "" and token != "":
            self.accept()
        else:
            QMessageBox.warning(self, "Erro", "Os valores não podem ser vazios!")
