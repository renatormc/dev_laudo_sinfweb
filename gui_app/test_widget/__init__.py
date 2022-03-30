from .test_widget_ui import Ui_TestWidget
from PyQt5.QtWidgets import QWidget

class TestWidget(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_TestWidget()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        pass
