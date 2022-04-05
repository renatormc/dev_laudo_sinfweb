from wtforms import Field
from wtforms.widgets import TextInput
from datetime import datetime


class SDateField(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data.strftime("%d/%m/%Y")
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            self.data = datetime.strptime(valuelist[0], "%d/%m/%Y")
        except Exception as e:
            self.data = None
            raise ValueError(
                "Data inválida")