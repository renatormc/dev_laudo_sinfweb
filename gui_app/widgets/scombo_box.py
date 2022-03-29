from typing import Any

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from custom_types import FormError

from gui_app.widgets.sbase import SBase


class SComboBox(SBase):

    def __init__(self, name: str, label="", choices=[]):
        self._name = name
        self.choices = choices
        self.label = label or self.name
        super(SComboBox, self).__init__()
        self.combo: QComboBox = None

    @property
    def name(self)->str:
        return self._name

    def get_context(self) -> Any:
        return self.combo.currentText()

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        self.combo = QComboBox()
        self.combo.addItems(self.choices)
        l.addWidget(self.combo)
        return w

    def validate(self) -> list[FormError]:
        return []

