from optparse import Option
from typing import Any, Optional, Tuple
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QToolButton, QLabel
from PyQt5.QtCore import pyqtSignal
from fastdoc.custom_types import FormError
from fastdoc.gui_app.widgets.swidget import SWidget
from fastdoc.gui_app.widgets.types import ValidationError
from fastdoc.gui_app.helpers import get_icon


class SComposite(QWidget):
    removeRequested = pyqtSignal(int)
    cloneRequested = pyqtSignal(int)

    def __init__(self, widgets: list[list[SWidget]],
            color: Optional[str] = "white", is_array_child=False, index: int = 0) -> None:
        super().__init__()
        self._index = index
        self.color = color
        self.widgets = widgets
        self.widgets_map: dict[str, SWidget] = {}
        for row in self.widgets:
            for item in row:
                self.widgets_map[item.name] = item
        self.is_array_child = is_array_child
        self.lbl_index: Optional[QLabel] = None
        self.setup_ui()

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        self._index = value
        if self.lbl_index is not None:
            self.lbl_index.setText(str(value + 1))

    def setup_ui(self):
        self.lay_main = QVBoxLayout()
        self.lay_main.setSpacing(0)
        self.setLayout(self.lay_main)

        if self.is_array_child:
            lay = QHBoxLayout()
            self.lbl_index = QLabel(str(self.index + 1))
            lay.addWidget(self.lbl_index)
            # lay.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
            
            btn = QToolButton()
            btn.clicked.connect(self.request_clone)
            btn.setIcon(get_icon("clone.jpeg"))
            btn.setToolTip("Clonar")
            lay.addWidget(btn)

            btn = QToolButton()
            btn.clicked.connect(self.request_remove)
            btn.setIcon(get_icon("x.png"))
            btn.setToolTip("Remover")
            lay.addWidget(btn)
    
            self.lay_main.addLayout(lay)

        for row in self.widgets:
            h_layout = QHBoxLayout()
            self.lay_main.addLayout(h_layout)
            for i, item in enumerate(row):
                w = item.get_widget()
                h_layout.addWidget(w)
                h_layout.setStretch(i, item.stretch)
                h_layout.setContentsMargins(0,0,0,0)
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.lay_main.addSpacerItem(spacer_item)
        if self.color:
            self.setStyleSheet(f"background-color: {self.color}")
        

    def get_context(self) -> Tuple[dict, FormError]:
        context = {}
        errors: FormError = {}
        for row in self.widgets:
            for item in row:
                message = ""
                try:
                    context[item.name] = item.get_context()
                except ValidationError as e:
                    message = str(e)
                    errors[item.name] = message
                item.show_error(message)
        return context, errors

    def load(self, data: dict) -> None:
        for key, w in self.widgets_map.items():
            try:
                w.load(data[key])
            except Exception:
                pass

    def serialize(self):
        data = {}
        for row in self.widgets:
            for item in row:
                data[item.name] = item.serialize()
        return data

    def clear_content(self):
        for row in self.widgets:
            for item in row:
                item.clear_content()

    def request_remove(self):
        self.removeRequested.emit(self.index)

    def request_clone(self):
        self.cloneRequested.emit(self.index)
