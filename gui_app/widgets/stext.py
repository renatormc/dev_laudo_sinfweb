from optparse import Option
from typing import Any, Optional
from xml.dom import ValidationErr

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from custom_types import FormError


class SText:

    def __init__(self, name: str, required=False, label="", placeholder="") -> None:
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self._label = label or self.name
        super(SText, self).__init__()
        self.led: Optional[QLineEdit] = None
        self.lbl_error: Optional[QLabel] = None

    @property
    def led(self) -> QLineEdit:
        if not self._led:
            raise Exception("Get Widget must be executed once before")
        return self._led

    @property
    def label(self) -> str:
        return self._label

    @property
    def name(self) -> str:
        return self._name

    def get_context(self) -> Any:
        return self.led.displayText()

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        self._led = QLineEdit()
        self._led.setPlaceholderText(self.placeholder)
        l.addWidget(self._led)
        return w

    def validate(self):
        if self.required and self.led.displayText().strip() == "":
            raise ValidationErr('O valor não pode ser vazio')
        