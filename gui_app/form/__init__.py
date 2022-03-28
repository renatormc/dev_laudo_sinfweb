from gui_app.widgets.sbase import SBase
from .form_ui import Ui_Form
from PyQt5.QtWidgets import QWidget, QHBoxLayout

class Form(QWidget):
    def __init__(self, widgets: list[list[SBase]]):
        self.widgets = widgets
        super(self.__class__, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connections()
        self.setup_ui()

    def setup_ui(self):
        for row in self.widgets:
            h_layout = QHBoxLayout()
            self.ui.lay_widgets.addLayout(h_layout)
            for item in row:
                w = item.get_widget()
                h_layout.addWidget(w)
        

    def connections(self):
        pass
