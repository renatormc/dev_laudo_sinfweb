from distutils import errors
from fastdoc.custom_types import FormError
# from fastdoc.gui_app.form import Form
from typing import Any, Optional
from fastdoc.gui_app.widgets.scomposite import SComposite
from fastdoc.gui_app.widgets.swidget import SWidget
from fastdoc.gui_app.widgets.types import ValidationError
from fastdoc.gui_app.widgets.label_error import LabelError
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QSize
from fastdoc.gui_app.helpers import get_icon
from fastdoc.gui_app.colors import Colors


class SArray:
    def __init__(self, name: str, widgets: list[list[SWidget]], label="", stretch=0, ) -> None:
        self._name = name
        self._label = label or self.name
        self._stretch = stretch
        self.widgets = widgets
        super(SArray, self).__init__()
        self._composites: Optional[list[SComposite]] = None
        # self._lbl_error: Optional[LabelError] = None

    @property
    def stretch(self) -> int:
        return self._stretch

    @property
    def composites(self) -> list[SComposite]:
        if self._composites is None:
            raise Exception("get_widget must be executed once before")
        return self._composites

    # @property
    # def lbl_error(self) -> LabelError:
    #     if not self._lbl_error:
    #         raise Exception("get_widget must be executed once before")
    #     return self._lbl_error

    @property
    def label(self) -> str:
        return self._label

    @property
    def name(self) -> str:
        return self._name

    def get_context(self) -> Any:
        data = []
        errors = False
        for comp in self.composites:
            c, error = comp.get_context()
            if error:
                errors = True
            data.append(c)
        if errors:
            raise ValidationError("Há erros")
        return data

    def get_widget(self) -> QWidget:
        w = QWidget()
        w.setStyleSheet(f"background-color: {Colors.array_widget_background};")
        w.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        lay_main = QVBoxLayout()
        lay_main.setContentsMargins(0,0,0,0)
        lay_main.setSpacing(0)
        w.setLayout(lay_main)

        lay_main.addWidget(QLabel(self.label))
        lay_main.setSpacing(0)

        lay_horizontal = QHBoxLayout()

        self.spb_add = QSpinBox()
        self.spb_add.setMinimumHeight(30)
        self.spb_add.setMinimum(1)
        lay_horizontal.addWidget(self.spb_add)

        self.btn_add = QPushButton("Adicionar")
        self.btn_add.setMinimumHeight(30)
        self.btn_add.setIcon(get_icon("add.png"))
        self.btn_add.setIconSize(QSize(30,30))
        self.btn_add.clicked.connect(self.add_items)
        lay_horizontal.addWidget(self.btn_add)

        self.btn_remove_all = QPushButton("Remover todos")
        self.btn_remove_all.setMinimumHeight(30)
        self.btn_remove_all.setIcon(get_icon("x.png"))
        self.btn_remove_all.clicked.connect(self.remove_all_items)
        lay_horizontal.addWidget(self.btn_remove_all)

        lay_horizontal.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        lay_main.addLayout(lay_horizontal)

        self.lay_composites = QVBoxLayout()
        self.lay_composites.setContentsMargins(0,0,0,0)
        self.lay_composites.setSpacing(0)
        lay_main.addLayout(self.lay_composites)

        self._composites = []
        return w

    def add_items(self, qtd: Optional[int] = None):
        qtd = qtd or self.spb_add.value()
        n = len(self.composites)
        for i in range(qtd):
            index = n + i
            composite = SComposite(self.widgets, color=Colors.item_array_widget_background, show_delete_button=True, index=index)
            composite.removeRequested.connect(self.remove_by_index)
            self.lay_composites.addWidget(composite)
            self.composites.append(composite)

    def remove_all_items(self):
        n = len(self.composites)
        for i in range(n):
            ri = n-i-1
            self.composites[ri].deleteLater()
            self.composites.pop(ri)
       
    def remove_by_index(self, index: int) -> None:
        self.composites[index].deleteLater()
        self.composites.pop(index)
        for i in range(index, len(self.composites)):
            self.composites[i].index -= 1

    def serialize(self) -> Any:
        data = []
        for composite in self.composites:
            data.append(composite.serialize())
        return data

    def load(self, data: list[Any]) -> None:
        n = len(data)
        self.clear_content()
        self.add_items(n)
        for i in range(n):
            self.composites[i].load(data[i])


    def clear_content(self) -> None:
        for composite in self.composites:
            composite.clear_content()

    def show_error(self, message: str) -> None:
        pass


