from typing import Any, Protocol
from abc import ABC, abstractmethod, abstractproperty
from PyQt5.QtWidgets import QWidget

from custom_types import FormError


class SBase(ABC):

    @abstractmethod
    def get_context(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_widget(self) -> QWidget:
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> list[FormError]:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError



