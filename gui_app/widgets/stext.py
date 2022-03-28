from typing import Any

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from gui_app.widgets.sbase import SBase


class SText(SBase):

    def __init__(self, name: str, required=False, label=""):
        self.required = required
        self.name = name
        self.label = label or self.name
        super(SText, self).__init__()

    def get_context(self) -> Any:
        pass

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        l.addWidget(QLineEdit())
        return w


