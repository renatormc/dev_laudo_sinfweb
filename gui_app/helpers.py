from typing import Any
import config
from PyQt5.QtGui import QIcon

from custom_types import ConverterType
from gui_app.widgets.validation_error import ValidationError

def get_icon(name):
    return QIcon(str(config.app_dir / "gui_app/assets/images" / name)) 

def apply_converter(value, converter: ConverterType) -> Any:
    try:
        return converter(value)
    except Exception as e:
        raise ValidationError(f"Valor inválido")