from .organizer_obj_ui import Ui_OrganizerObj
from PyQt5.QtWidgets import QWidget

class OrganizerObj(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_OrganizerObj()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        pass

    def set_object_types(self, types: list[str]):
        self.ui.cbx_type.clear()
        self.ui.cbx_type.addItems(types)

    def set_name(self, value):
        self.ui.lbl_name.setText(value)

    def get_type(self) -> str:
        return self.ui.cbx_type.currentText()
