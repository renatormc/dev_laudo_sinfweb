from typing import Any, Protocol
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget


class SBase(ABC):

    @abstractmethod
    def get_context(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_widget(self) -> QWidget:
        raise NotImplementedError


