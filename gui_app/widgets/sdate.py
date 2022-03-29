from typing import Any, Optional
from xml.dom import ValidationErr

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from custom_types import FormError

from datetime import datetime


class SDate:

    def __init__(self, name: str, required=False, label="", placeholder="") -> None:
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self._label = label or self.name
        super(SDate, self).__init__()
        self._led: Optional[QLineEdit] = None

    @property
    def led(self) -> QLineEdit:
        if not self._led:
            raise Exception("Get Widget must be executed once before")
        return self._led

    @property
    def name(self) -> str:
        return self._name

    @property
    def label(self) -> str:
        return self._label

    def get_context(self) -> Any:
        return datetime.strptime(self.led.displayText(), "%d/%m/%Y")

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        self._led = QLineEdit()
        self.led.setPlaceholderText(self.placeholder)
        l.addWidget(self.led)
        return w

    def validate(self):
        try:
            datetime.strptime(self.led.displayText(), "%d/%m/%Y")
        except:
            raise ValidationErr('Data inválida')
