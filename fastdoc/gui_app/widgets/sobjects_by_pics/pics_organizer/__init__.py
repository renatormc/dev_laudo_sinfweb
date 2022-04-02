from copy import copy
from pathlib import Path
from .pics_organizer_ui import Ui_PicsOrganizer
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QListWidgetItem, QMenu, QAction, QListWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from .organizer_obj import OrganizerObj


class PicsOrganizer(QDialog):
    def __init__(self, objects):
        self.objects = objects
        super(self.__class__, self).__init__()
        self.ui = Ui_PicsOrganizer()
        self.ui.setupUi(self)
        self.ui.led_alias_pericias.setText(objects['alias'])
        self.connections()
        self.objects_widgets: dict[int, OrganizerObj] = {}
        self.change_icon_size(self.ui.sld_icon_size.value())
        self.reload()

    def connections(self):
        self.ui.btn_add.clicked.connect(self.add_obbjects)
        self.ui.sld_icon_size.valueChanged.connect(self.change_icon_size)
        self.ui.lsw_not_associated.customContextMenuRequested.connect(self.provide_context_menu_default)
    

    def reload(self):
        self.ui.lsw_not_associated.clear()
        for obj in self.objects['objects']:
            for pic in obj['pics']:
                item = QListWidgetItem()
                icon = QIcon()
                icon.addPixmap(QPixmap(pic), QIcon.Normal, QIcon.Off)
                item.setIcon(icon)
                path = Path(pic)
                item.setText(path.name)
                self.ui.lsw_not_associated.addItem(item)

    def add_object(self) -> OrganizerObj:
        n = len(self.objects_widgets.keys())
        index = n + 1
        obj = OrganizerObj(index)
        obj.set_object_types(['Celular', 'Computador', 'HDD'])
        self.ui.lay_objects.addWidget(obj)
        self.objects_widgets[index] = obj
        obj.close_clicked.connect(self.remove_object)
        obj.context_menu_requested.connect(self.provide_context_menu)
        obj.set_icon_size(QSize(10000, self.ui.sld_icon_size.value()))
        return obj

    def add_obbjects(self):
        for i in range(self.ui.spb_n_add.value()):
            self.add_object()

    def change_icon_size(self, value):
        self.ui.lsw_not_associated.setIconSize(QSize(10000, value))
        for item in self.objects_widgets.values():
            item.set_icon_size(QSize(10000, value))

    def remove_object(self, index: int):
        objw = self.objects_widgets[index].ui.lsw_object
        for i in range(objw.count()):
            self.move_item(objw, self.ui.lsw_not_associated, objw.item(i), copy=True)
        self.objects_widgets[index].deleteLater()
        del self.objects_widgets[index]

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
        for index in self.objects_widgets.keys():
            text = f"Adicionar ao objeto {index}"
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
        
