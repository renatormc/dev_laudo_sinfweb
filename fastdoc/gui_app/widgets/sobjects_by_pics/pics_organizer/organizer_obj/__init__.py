from .organizer_obj_ui import Ui_OrganizerObj
from PyQt5.QtWidgets import QWidget, QListWidget
from PyQt5.QtCore import pyqtSignal, QSize, QPoint
import hashlib

class OrganizerObj(QWidget):
    close_clicked = pyqtSignal(int)
    context_menu_requested = pyqtSignal(QPoint, QListWidget)


    def __init__(self, name: str, index: int):
        super(self.__class__, self).__init__()
        self.ui = Ui_OrganizerObj()
        self.ui.setupUi(self)
        self.connections()
        self.name = name
        self.index = index
     
    @property
    def name(self) -> str:
        return self.ui.led_name.displayText()

    @name.setter
    def name(self, value) -> None:
        self.ui.led_name.setText(value)
        # self._id = hashlib.md5(value).hexdigest()


    def connections(self):
        self.ui.btn_close.clicked.connect(self.close_button_pressed)
        self.ui.lsw_object.customContextMenuRequested.connect(self.provide_context_menu)

    def set_icon_size(self, size: QSize):
        # for i in range(self.ui.lsw_object.count()):
        #     item = self.ui.lsw_object.item(i)
        #     w = self.ui.lsw_object.itemWidget(item)
        #     w.test()
        self.ui.lsw_object.setIconSize(size)


    def close_button_pressed(self):
        self.close_clicked.emit(self.index)

    def provide_context_menu(self, pos):
        self.context_menu_requested.emit(pos, self.ui.lsw_object)
