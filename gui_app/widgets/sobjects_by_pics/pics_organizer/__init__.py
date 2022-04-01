from .pics_organizer_ui import Ui_PicsOrganizer
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QListWidgetItem
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
        self.objects_widgets: list[OrganizerObj] = []

    def connections(self):
        self.ui.btn_reconfig.clicked.connect(self.reconfig)

    def reconfig(self):
        for obj in self.objects_widgets:
            obj.deleteLater()
        self.objects_widgets = []
        for i in range(self.ui.spb_n_objetos.value()):
            obj = OrganizerObj()
            obj.set_object_types(['Celular', 'Computador', 'HDD'])
            obj.set_name(f"Objeto {i+1}")
            self.ui.lay_objects.addWidget(obj)
            self.objects_widgets.append(obj)
        # self.ui.lsw_others.setIconSize(QSize(150,150))
        for obj in self.objects['objects']:
            for pic in obj['pics']:
                item = QListWidgetItem()
                icon = QIcon()
                icon.addPixmap(QPixmap(pic),QIcon.Normal, QIcon.Off)
                item.setIcon(icon)
                self.ui.lsw_others.addItem(item)


