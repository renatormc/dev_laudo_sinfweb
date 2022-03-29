from typing import Any, Protocol
from abc import ABC, abstractmethod, abstractproperty
from PyQt5.QtWidgets import QWidget

from custom_types import FormError


class SWidget(Protocol):

    def get_context(self) -> Any:
        ...

    def get_widget(self) -> QWidget:
        ...

    def validate(self) -> None:
        ...

    def show_error(self, message: str) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def label(self) -> str:
        ...
