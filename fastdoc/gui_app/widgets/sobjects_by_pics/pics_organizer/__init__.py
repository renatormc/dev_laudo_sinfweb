from copy import copy
from pathlib import Path

from fastdoc.gui_app.widgets.sobjects_by_pics.objects_typy import CaseObjectsType
from .pics_organizer_ui import Ui_PicsOrganizer
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMenu, QAction, QListWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from .organizer_obj import OrganizerObj
from .item_delegate import ItemDelegate


class PicsOrganizer(QDialog):
    def __init__(self, objects: CaseObjectsType):
        self.objects = objects
        super(self.__class__, self).__init__()
        self.ui = Ui_PicsOrganizer()
        self.ui.setupUi(self)
        self.setup_ui()
        self.connections()
        self.objects_widgets: list[OrganizerObj] = []
        self.change_icon_size(self.ui.sld_icon_size.value())
        self.populate()

    def connections(self):
        self.ui.btn_add.clicked.connect(self.add_obbjects)
        self.ui.sld_icon_size.valueChanged.connect(self.change_icon_size)
        self.ui.lsw_not_associated.customContextMenuRequested.connect(self.provide_context_menu_default)

    def setup_ui(self):
        self.delegate = ItemDelegate()
        self.ui.lsw_not_associated.setItemDelegate(self.delegate)

    @property
    def pic_size(self) -> QSize:
        value = self.ui.sld_icon_size.value()
        return QSize(value, value)

    @property
    def item_size_hint(self) -> QSize:
        return QSize(self.pic_size.width() + 5, self.pic_size.height() + 20)

    def populate(self):
        self.ui.lsw_not_associated.clear()
        for pic in self.objects.pics_not_classified_iterator():
            item = QListWidgetItem()
            item.setSizeHint(self.item_size_hint)
            item.setTextAlignment(Qt.AlignCenter)
            icon = QIcon()
            icon.addPixmap(QPixmap(str(pic)), QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
            path = Path(pic)
            item.setText(path.name)
            self.ui.lsw_not_associated.addItem(item)
        for obj in self.objects.objects:
            objw = self.add_object(obj.name)
            for pic in obj.pics_iterator():
                self.add_pic_to_object_widget(objw, pic)

    def add_pic_to_object_widget(self, objw: OrganizerObj,  pic: Path) -> None:
        item = QListWidgetItem()
        item.setSizeHint(self.item_size_hint)
        item.setTextAlignment(Qt.AlignCenter)
        icon = QIcon()
        icon.addPixmap(QPixmap(str(pic)), QIcon.Normal, QIcon.Off)
        item.setIcon(icon)
        item.setText(pic.name)

    def add_object(self) -> OrganizerObj:
        index = len(self.objects_widgets)
        obj = OrganizerObj(f"Objeto {index + 1}", index)
        self.ui.lay_objects.addWidget(obj)
        self.objects_widgets.append(obj)
        obj.close_clicked.connect(self.remove_object)
        obj.context_menu_requested.connect(self.provide_context_menu)
        obj.set_icon_size(self.pic_size, self.item_size_hint)
        return obj

    def add_obbjects(self):
        for i in range(self.ui.spb_n_add.value()):
            self.add_object()

    def change_icon_size(self, value):
        self.ui.lsw_not_associated.setIconSize(self.pic_size)
        for i in range(self.ui.lsw_not_associated.count()):
            item = self.ui.lsw_not_associated.item(i)
            item.setSizeHint(self.item_size_hint)

        # w = self.ui.lsw_not_associated.itemWidget(item)
        # w.pic_size = self.pic_size
        for objw in self.objects_widgets:
            objw.set_icon_size(self.pic_size, self.item_size_hint)
            

    def remove_object(self, index: int):
        objw = self.objects_widgets[index].ui.lsw_object
        for i in range(objw.count()):
            self.move_item(objw, self.ui.lsw_not_associated, objw.item(i), copy=True)
        self.objects_widgets[index].deleteLater()
        self.objects_widgets.pop(index)
        for i in range(index, len(self.objects_widgets)):
            self.objects_widgets[i].index -= 1

    def move_item(self, lsw_from: QListWidget, lsw_to: QListWidget, item: QListWidgetItem, copy=False):
        item_clone = item.clone()
        lsw_to.addItem(item_clone)
        if not copy:
            lsw_from.takeItem(lsw_from.row(item))

    def provide_context_menu_default(self, pos):
        self.provide_context_menu(pos, self.ui.lsw_not_associated)

    def provide_context_menu(self, pos, lsw: QListWidget):
        menu = QMenu()

        act_move_new = QAction('Mover para novo ojeto')
        menu.addAction(act_move_new)

        if lsw != self.ui.lsw_not_associated:
            menu.addAction("Remover do objeto")

        objects_actions = {}
        for index, obj in enumerate(self.objects_widgets):
            text = f"Adicionar ao objeto \"{obj.name}\""
            objects_actions[text] = index
            menu.addAction(text)

        act = menu.exec_(lsw.mapToGlobal(pos))
        if act:
            if act == act_move_new:
                obj = self.add_object()
                objw = obj.ui.lsw_object
                for item in lsw.selectedItems():
                    self.move_item(lsw, objw, item)
            elif act.text() == "Remover do objeto":
                for item in lsw.selectedItems():
                    self.move_item(lsw, self.ui.lsw_not_associated, item)
            else:
                try:
                    index = objects_actions[act.text()]
                    obj = self.objects_widgets[index]
                    objw = obj.ui.lsw_object
                    for item in lsw.selectedItems():
                        self.move_item(lsw, objw, item)
                except KeyError:
                    pass
