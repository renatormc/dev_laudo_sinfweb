from fastdoc.gui_app.widgets.scomposite import SComposite
from fastdoc.gui_app.widgets.swidget import SWidget


class SVarFormItem:
    def __init__(self, choice_value: str, widgets: list[list[SWidget]]) -> None:
        self.choice_value = choice_value
        self.form = SComposite(widgets=widgets, color="red")
        self.form.setStyleSheet("margin-left: 0; background-color: red;")