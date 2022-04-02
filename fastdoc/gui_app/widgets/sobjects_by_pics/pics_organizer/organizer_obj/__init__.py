from .organizer_obj_ui import Ui_OrganizerObj
from PyQt5.QtWidgets import QWidget, QListWidget
from PyQt5.QtCore import pyqtSignal, QSize, QPoint


class OrganizerObj(QWidget):
    close_clicked = pyqtSignal(int)
    context_menu_requested = pyqtSignal(QPoint, QListWidget)

    def __init__(self, index: int):
        super(self.__class__, self).__init__()
        self._index = 0
        self.ui = Ui_OrganizerObj()
        self.ui.setupUi(self)
        self.index = index
        self.connections()

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        self._index = value
        self.ui.lbl_name.setText(f"Objeto {value}")

    def connections(self):
        self.ui.btn_close.clicked.connect(self.close_button_pressed)
        self.ui.lsw_object.customContextMenuRequested.connect(self.provide_context_menu)

    def set_icon_size(self, size: QSize):
        self.ui.lsw_object.setIconSize(size)


    def set_object_types(self, types: list[str]):
        self.ui.cbx_type.clear()
        self.ui.cbx_type.addItems(types)

    def get_type(self) -> str:
        return self.ui.cbx_type.currentText()

    def close_button_pressed(self):
        self.close_clicked.emit(self._index)

    def provide_context_menu(self, pos):
        self.context_menu_requested.emit(pos, self.ui.lsw_object)
