from typing import Optional, Tuple
from fastdoc.custom_types import FormError, ModelInfo
from fastdoc.gui_app.widgets.scomposite import SComposite
from fastdoc.gui_app.widgets.swidget import SWidget
from fastdoc.gui_app.widgets.types import ValidationError
from PyQt5.QtWidgets import QFileDialog
import json
from pathlib import Path
from database import repo


class Form(SComposite):
    def __init__(self, model_info: ModelInfo, widgets: list[list[SWidget]]):
        self.model_info = model_info
        super(Form, self).__init__(widgets, model_name=self.model_info.name)


    def save_last_data(self):
        data = self.serialize()
        repo.save_last_data(self.model_info.name,  data)

    def load_last_data(self):
        data = repo.get_last_data(self.model_info.name)
        self.load(data)

    def save_to_file(self, file_: Optional[str] = None):
        data = self.serialize()
        file_= file_ or QFileDialog.getSaveFileName(self, "Escolha o arquivo",  ".", "JSON (*.json)")[0]
        if file_:
            with Path(file_).open("w", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=4))


    def load_from_file(self, file_: Optional[str] = None) -> None:
        file_ = file_ or QFileDialog.getOpenFileName(self, "Escolha o arquivo",  ".", "JSON (*.json)")[0]
        if file_:
            path = Path(file_)
            if path.exists():
                with Path(file_).open("r", encoding="utf-8") as f:
                    data = json.load(f)
                self.load(data)

    # def load_data(self, data: dict) -> None:
    #     for key, w in self.widgets_map.items():
    #         try:
    #             w.load(data[key])
    #         except Exception:
    #             pass

    # def clear_content(self):
    #     for row in self.widgets:
    #         for item in row:
    #             item.clear_content()
