from typing import Any, Callable, Optional, TypedDict
from fastdoc import config
import json

FormError = dict[str, str]

ValidatorType = Callable[[Any], None]
ConverterType = Callable[[Any], Any]

class ModelMetaType(TypedDict):
    full_name: str
    has_qt_form: bool
    has_web_form: bool


class ModelInfo:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.meta: ModelMetaType =  {
            'full_name': '',
            'has_qt_form': False,
            'has_web_form': False
        }
    def load_meta(self):
        path = config.models_folder / self.name / "meta.json"
        with path.open("r", encoding="utf-8") as f:
            self.meta = json.load(f)
    
