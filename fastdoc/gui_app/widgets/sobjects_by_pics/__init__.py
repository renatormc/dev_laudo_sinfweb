from pathlib import Path
from typing import Any, Optional, Union
from fastdoc.gui_app.widgets.helpers import apply_converter
from rlibs.report_writer.types import CaseObjectsType
from fastdoc.gui_app.widgets.types import ValidationError

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QToolButton, QFileDialog
from fastdoc.custom_types import ConverterType, ValidatorType
from fastdoc.gui_app.widgets.label_error import LabelError
from fastdoc.gui_app.widgets.sobjects_by_pics.pics_organizer import PicsOrganizer
from rlibs.report_writer.pics_analyzer import get_objects_from_pics
from fastdoc import config


class SObjetctsByPics:

    def __init__(
        self, name: str, required=False, label="", placeholder="",
            validators: list[ValidatorType] = [], stretch=0,
            converter: Optional[ConverterType] = None, extensions=[".jpg", ".png"],
            default_object_type: Optional[str]=None) -> None:
        self.required = required
        self.placeholder = placeholder
        self._name = name
        self.validators = validators
        self._label = label or self.name
        self._stretch = stretch
        self.converter = converter
        self.extensions = extensions
        self.default_object_type = default_object_type
        super(SObjetctsByPics, self).__init__()
        self._led: Optional[QLineEdit] = None
        self._w: Optional[QWidget] = None
        self._lbl_error: Optional[LabelError] = None
        self._btn_choose: Optional[QToolButton] = None
        self._btn_open_organizer: Optional[QToolButton] = None
        self.current_objects: CaseObjectsType = CaseObjectsType(config.workdir)

    @property
    def stretch(self) -> int:
        return self._stretch

    @property
    def w(self) -> QWidget:
        if not self._w:
            raise Exception("get_widget must be executed once before")
        return self._w

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
    def btn_open_organizer(self) -> QToolButton:
        if not self._btn_open_organizer:
            raise Exception("get_widget must be executed once before")
        return self._btn_open_organizer

    @property
    def label(self) -> str:
        return self._label

    @property
    def name(self) -> str:
        return self._name

    def get_context(self) -> CaseObjectsType:
        text = self.led.displayText().strip()
        path = Path(text)
        if self.required and text == "":
            raise ValidationError('O valor não pode ser vazio')
        if not path.exists() or not path.is_dir():
            raise ValidationError('Pasta não existente')
        self.remove_pics_not_existents()
        objs = self.current_objects
        if self.converter is not None:
            objs = apply_converter(objs, self.converter)
        for v in self.validators:
            v(objs)
        return objs

    def get_widget(self) -> QWidget:
        self._w = QWidget()
        l = QVBoxLayout()
        self._w.setLayout(l)
        l.addWidget(QLabel(self.label))
        h_layout = QHBoxLayout()
        self._led = QLineEdit()
        self._led.textChanged.connect(self.on_folder_change)
        self._led.setPlaceholderText(self.placeholder)
        h_layout.addWidget(self._led)
        self._btn_choose = QToolButton()
        self._btn_choose.setText("...")
        self._btn_choose.clicked.connect(self.choose_folder)
        h_layout.addWidget(self._btn_choose)
        self._btn_open_organizer = QToolButton()
        self._btn_open_organizer.setText("Organizador")
        self._btn_open_organizer.setEnabled(False)
        self._btn_open_organizer.clicked.connect(self.organize_pics)
        h_layout.addWidget(self._btn_open_organizer)
        l.addLayout(h_layout)

        self._lbl_error = LabelError()
        l.addWidget(self._lbl_error)
        return self._w

    def show_error(self, message: str) -> None:
        self.lbl_error.setText(message)

    def choose_folder(self):
        dir_ = QFileDialog.getExistingDirectory(
            None, "Escolha um diretório", ".")
        if dir_:
            self.load(str(Path(dir_)))

    def organize_pics(self):
        dialog = PicsOrganizer(self.w, self.current_objects)
        ok = dialog.exec_()
        if ok:
            self.current_objects = dialog.objects
                      

    def serialize(self) -> Any:
        return self.led.displayText()

    def load(self, value: str) -> None:
        self.led.setText(value)

    def clear_content(self) -> None:
        pass

    def get_pics_from_folder(self, folder: Union[Path, str]) -> list[str]:
        folder = Path(folder)
        return [str(entry.absolute()) for entry in folder.iterdir() if entry.is_file() and entry.suffix.lower() in self.extensions]

    def remove_pics_not_existents(self):
        if not self.current_objects.folder.exists():
            self.current_objects = CaseObjectsType()
            return
        folder = self.current_objects.folder
        self.current_objects.pics_not_classified = [
            pic for pic in self.current_objects.pics_not_classified if(folder / pic).exists()]
        for obj in self.current_objects.objects:
            obj.pics = [pic for pic in obj.pics if (folder / pic).exists()]

    def on_folder_change(self, value):
        path = Path(value)
        if path.exists() and path.is_dir():
            # self.current_objects = CaseObjectsType(pics_not_classified=self.get_pics_from_folder(path))
            self.current_objects = get_objects_from_pics(path, self.default_object_type)
            self.btn_open_organizer.setEnabled(True)
        else:
            self.current_objects = CaseObjectsType()
            self.btn_open_organizer.setEnabled(False)

    
