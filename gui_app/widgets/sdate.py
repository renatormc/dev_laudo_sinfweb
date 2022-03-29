from typing import Any, Optional

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from custom_types import FormError

from gui_app.widgets.sbase import SBase
from datetime import datetime


class SDate(SBase):

    def __init__(self, name: str, required=False, label="", placeholder=""):
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self.label = label or self.name
        super(SDate, self).__init__()
        self.led: Optional[QLineEdit] = None


    @property
    def name(self)->str:
        return self._name

    def get_context(self) -> Any:
        return datetime.strptime(self.led.displayText(), "%d/%m/%Y")

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
        try:
            datetime.strptime(self.led.displayText(), "%d/%m/%Y")
        except:
            return [{'field': self.name,'message':'Data inválida'}]
        return []


