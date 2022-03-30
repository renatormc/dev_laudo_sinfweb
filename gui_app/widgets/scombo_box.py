from typing import Any, Optional

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from custom_types import FormError
from gui_app.widgets.label_error import LabelError


class SComboBox:

    def __init__(self, name: str, label="", choices=[], stretch=0, default=""):
        self._name = name
        self.choices = choices
        self._label = label or self.name
        self._stretch = stretch
        self.default = default
        super(SComboBox, self).__init__()
        self._combo: Optional[QComboBox] = None
        self._lbl_error: Optional[LabelError] = None

    @property
    def stretch(self) -> int:
        return self._stretch

    @property
    def combo(self) -> QComboBox:
        if self._combo is None:
            raise Exception("get_widget must be executed once before")
        return self._combo

    @property
    def lbl_error(self) -> LabelError:
        if not self._lbl_error:
            raise Exception("get_widget must be executed once before")
        return self._lbl_error

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
        self._lbl_error = LabelError()
        l.addWidget(self._lbl_error)
        return w

    def validate(self):
        pass

    def show_error(self, message: str) -> None:
        self.lbl_error.setText(message)

    def serialize(self) -> Any:
        return self.get_context()

    def load(self, value: Any) -> None:
        self.combo.setCurrentText(value)

    def clear_content(self)-> None:
        if self.default != "":
            self.combo.setCurrentText(self.default)
