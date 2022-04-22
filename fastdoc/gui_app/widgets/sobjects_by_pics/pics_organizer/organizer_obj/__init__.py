from pathlib import Path

from fastdoc.gui_app.widgets.types import ObjectPicUserData
from .organizer_obj_ui import Ui_OrganizerObj
from PyQt5.QtWidgets import QWidget, QListWidget
from PyQt5.QtCore import pyqtSignal, QSize, QPoint, Qt
from ..item_delegate import ItemDelegate
from ..helpers import ajust_size_hint

class OrganizerObj(QWidget):
    close_clicked = pyqtSignal(int)
    context_menu_requested = pyqtSignal(QPoint, QListWidget)


    def __init__(self, name: str, index: int):
        super(self.__class__, self).__init__()
        self.ui = Ui_OrganizerObj()
        self.ui.setupUi(self)
        self.setup_ui()
        self.connections()
        self.name = name
        self.index = index

    def setup_ui(self):
        self.delegate = ItemDelegate()
        self.ui.lsw_object.setItemDelegate(self.delegate)
     
    @property
    def name(self) -> str:
        return self.ui.led_name.displayText()

    @name.setter
    def name(self, value) -> None:
        self.ui.led_name.setText(value)

    @property
    def type(self) -> str:
        return self.ui.cbx_type.currentData()

    @type.setter
    def type(self, value) -> None:
        self.ui.cbx_type.setCurrentText(value)


    @property
    def pics(self)-> list[str]:
        pics: list[str] = []
        for i in range(self.ui.lsw_object.count()):
            item = self.ui.lsw_object.item(i)
            user_data: ObjectPicUserData = item.data(Qt.UserRole)
            pics.append(str(user_data.pic))
        return pics


    def connections(self):
        self.ui.btn_close.clicked.connect(self.close_button_pressed)
        self.ui.lsw_object.customContextMenuRequested.connect(self.provide_context_menu)

    def set_icon_size(self, size: QSize):
        self.ui.lsw_object.setIconSize(size)
        for i in range(self.ui.lsw_object.count()):
            item = self.ui.lsw_object.item(i)
            ajust_size_hint(item, size)
            

    def close_button_pressed(self):
        self.close_clicked.emit(self.index)

    def provide_context_menu(self, pos):
        self.context_menu_requested.emit(pos, self.ui.lsw_object)
