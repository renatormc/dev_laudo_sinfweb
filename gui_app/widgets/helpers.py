from typing import Any
from custom_types import ConverterType
from gui_app.widgets.validation_error import ValidationError

def apply_converter(value, converter: ConverterType) -> Any:
    try:
        return converter(value)
    except Exception as e:
        raise ValidationError(f"Valor inválido")