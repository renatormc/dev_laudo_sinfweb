from typing import Any, Protocol
from wtforms.fields import Field

class WidgetProtocol(Protocol):

    def get_context(self) -> Any:
        ...

    def get_widget(self) -> Field:
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
    def col(self) -> int:
        ...