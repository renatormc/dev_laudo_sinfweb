from wtforms import Field
from typing import Any, Protocol, Type
from .form_fields import *
from datetime import datetime


class FormFielSerializer(Protocol):

    def serialize(field: Field) -> Any:
        ...

    def desserialize(field: Field, data: Any) -> None:
        ...


class SDateFieldSerializer:
    def serialize(field: Field) -> Any:
        return field.data.strftime("%d/%m/%Y")

    def desserialize(field: Field, data: Any) -> None:
        field.data = datetime.strptime(str(data),  "%d/%m/%Y")


class SDateTimeFieldSerializer:

    def serialize(field: Field) -> Any:
        return field.data.strftime("%d/%m/%Y %H:%M:%S")

    def desserialize(field: Field, data: Any) -> None:
        field.data = datetime.strptime(str(data),  "%d/%m/%Y %H:%M:%S")


class SFileSizeFieldSerializer:

    def serialize(field: Field) -> Any:
        return field.data

    def desserialize(field: Field, data: Any) -> None:
        field.data = data

serializers: dict[str, Type[FormFielSerializer]] = {
    'SDateField': SDateFieldSerializer,
    'SDateTimeSerializer': SDateTimeFieldSerializer,
    'SFileSizeFieldSerializer': SFileSizeFieldSerializer,
}


def get_serializer(field: Field) -> FormFielSerializer:
    return serializers[field.name]()
