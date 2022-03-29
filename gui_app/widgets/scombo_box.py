from typing import Any, Optional

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from custom_types import FormError


class SComboBox:

    def __init__(self, name: str, label="", choices=[]):
        self._name = name
        self.choices = choices
        self._label = label or self.name
        super(SComboBox, self).__init__()
        self._combo: Optional[QComboBox] = None

    @property
    def combo(self) -> QComboBox:
        if self._combo is None:
            raise Exception("Get Widget must be executed once before")
        return self._combo

    @property
    def name(self) -> str:
        return self._name

    @property
    def label(self) -> str:
        return self._label

    def get_context(self) -> Any:
        return self.combo.currentText()

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        self._combo = QComboBox()
        self.combo.addItems(self.choices)
        l.addWidget(self.combo)
        return w

    def validate(self):
        pass
