from typing import Any, Protocol
from PyQt5.QtWidgets import QWidget


class SWidget(Protocol):

    def get_context(self) -> Any:
        ...

    def get_widget(self) -> QWidget:
        ...

    def show_error(self, message: str) -> None:
        ...

    def serialize(self) -> Any:
        ...

    def load(self, value: Any) -> None:
        ...

    def clear_content(self) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def label(self) -> str:
        ...

    @property
    def stretch(self) -> int:
        ...
