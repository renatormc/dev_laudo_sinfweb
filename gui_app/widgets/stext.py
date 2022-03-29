from typing import Any

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from custom_types import FormError

from gui_app.widgets.sbase import SBase


class SText(SBase):

    def __init__(self, name: str, required=False, label="", placeholder=""):
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self.label = label or self.name
        super(SText, self).__init__()
        self.led: QLineEdit = None

    @property
    def name(self)->str:
        return self._name

    def get_context(self) -> Any:
        return self.led.displayText()

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        self.led = QLineEdit()
        self.led.setPlaceholderText(self.placeholder)
        l.addWidget(self.led)
        return w

    def validate(self) -> list[FormError]:
        if self.required and self.led.displayText().strip() == "":
            return [{'field': self.name, 'message': 'O valor não pode ser vazio'}]
        return []

