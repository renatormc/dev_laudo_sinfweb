from typing import TypedDict


class FormError(TypedDict):
    field: str
    message: str