from typing import Any
from fastdoc.custom_types import ConverterType
from fastdoc.gui_app.widgets.types import ValidationError

def apply_converter(value, converter: ConverterType) -> Any:
    try:
        return converter(value)
    except Exception as e:
        raise ValidationError(f"Valor inválido")