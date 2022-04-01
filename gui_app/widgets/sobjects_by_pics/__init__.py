from pathlib import Path
from typing import Any, Optional
from gui_app.widgets.helpers import apply_converter
from gui_app.widgets.validation_error import ValidationError

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QToolButton, QFileDialog
from custom_types import ConverterType, ValidatorType
from gui_app.widgets.label_error import LabelError
from gui_app.widgets.sobjects_by_pics.name_analyzer import get_objects_from_pics


class SObjetctsByPics:

    def __init__(
            self, name: str, required=False, label="", placeholder="",
             validators: list[ValidatorType] = [], stretch=0,converter: Optional[ConverterType] = None) -> None:
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self.validators = validators
        self._label = label or self.name
        self._stretch = stretch
        self.converter = converter
        super(SObjetctsByPics, self).__init__()
        self._led: Optional[QLineEdit] = None
        self._lbl_error: Optional[LabelError] = None
        self._btn_choose: Optional[QToolButton] = None

    @property
    def stretch(self) -> int:
        return self._stretch

    @property
    def led(self) -> QLineEdit:
        if not self._led:
            raise Exception("get_widget must be executed once before")
        return self._led

    @property
    def lbl_error(self) -> LabelError:
        if not self._lbl_error:
            raise Exception("get_widget must be executed once before")
        return self._lbl_error

    @property
    def btn_choose(self) -> QToolButton:
        if not self._btn_choose:
            raise Exception("get_widget must be executed once before")
        return self._btn_choose

    @property
    def label(self) -> str:
        return self._label

    @property
    def name(self) -> str:
        return self._name

    def get_context(self) -> Any:
        text = self.led.displayText().strip()
        path = Path(text)
        if self.required and text == "":
            raise ValidationError('O valor não pode ser vazio')
        if not path.exists() or not path.is_dir():
            raise ValidationError('Pasta não existente')
        objs = get_objects_from_pics(path)
        if self.converter is not None:
            objs = apply_converter(objs, self.converter)
        for v in self.validators:
            v(objs)
        return objs

    def get_widget(self) -> QWidget:
        w = QWidget()
        l = QVBoxLayout()
        w.setLayout(l)
        l.addWidget(QLabel(self.label))
        h_layout = QHBoxLayout()
        self._led = QLineEdit()
        self._led.setPlaceholderText(self.placeholder)
        h_layout.addWidget(self._led)
        self._btn_choose = QToolButton()
        self._btn_choose.setText("...")
        self._btn_choose.clicked.connect(self.choose_folder)
        h_layout.addWidget(self._btn_choose)
        l.addLayout(h_layout)

        self._lbl_error = LabelError()
        l.addWidget(self._lbl_error)
        return w


    def show_error(self, message: str) -> None:
        self.lbl_error.setText(message)

    def choose_folder(self):
        dir_ = QFileDialog.getExistingDirectory(
            None, "Escolha um diretório", ".")
        if dir_:
            self.led.setText(str(Path(dir_)))

    def serialize(self) -> Any:
        return self.led.displayText()

    def load(self, value: Any) -> None:
        self.led.setText(value)

    def clear_content(self) -> None:
        pass
