from typing import Optional, TypedDict
from custom_types import FormError
from gui_app.widgets.swidget import SWidget
from .form_ui import Ui_Form
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog
import json
from pathlib import Path


class Form(QWidget):
    def __init__(self, model:str, widgets: list[list[SWidget]]):
        self.model = model
        self.widgets = widgets
        self.widgets_map: dict[str, SWidget] = {}
        for row in self.widgets:
            for item in row:
                self.widgets_map[item.name] = item
        super(self.__class__, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connections()
        self.setup_ui()

    def setup_ui(self):
        for row in self.widgets:
            h_layout = QHBoxLayout()
            self.ui.lay_widgets.addLayout(h_layout)
            # stretchs = []
            for i, item in enumerate(row):
                w = item.get_widget()
                h_layout.addWidget(w)
                h_layout.setStretch(i, item.stretch)
        spacer_item = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.lay_widgets.addItem(spacer_item)
        self.ui.lay_widgets.setSpacing(0)

    def connections(self):
        pass

    def get_context(self):
        context = {}
        for row in self.widgets:
            for item in row:
                context[item.name] = item.get_context()
        return context

    def validate(self) -> FormError:
        errors: FormError = {}
        for row in self.widgets:
            for item in row:
                message = ""
                try:
                    item.validate()
                except Exception as e:
                    message = str(e)
                    errors[item.name] = message
                item.show_error(message)
        return errors

    def save(self, file_: Optional[str] = None):
        data = {}
        for row in self.widgets:
            for item in row:
                data[item.name] = item.serialize()
        
        file_= file_ or QFileDialog.getSaveFileName(self, "Escolha o arquivo",  ".", "JSON (*.json)")[0]
        if file_:
            with Path(file_).open("w", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=4))

    def load(self, file_: Optional[str] = None):
        file_ = file_ or QFileDialog.getOpenFileName(self, "Escolha o arquivo",  ".", "JSON (*.json)")[0]
        if file_:
            path = Path(file_)
            if path.exists():
                with Path(file_).open("r", encoding="utf-8") as f:
                    data = json.load(f)
                for key, w in self.widgets_map.items():
                    try:
                        w.load(data[key])
                    except KeyError:
                        pass

    def clear_content(self):
        for row in self.widgets:
            for item in row:
                item.clear_content()
