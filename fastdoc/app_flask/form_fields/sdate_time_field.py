from wtforms import Field
from wtforms.widgets import TextInput
from datetime import datetime


class SDateTimeField(Field):
    widget = TextInput()

    def __init__(self, *args, format="%d/%m/%Y %H:%M:%S", **kargs):
        super().__init__(*args, **kargs)
        self.format = format

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data.strftime(self.format)
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            self.data = datetime.strptime(valuelist[0], self.format)
        except Exception as e:
            self.data = None
            raise ValueError(
                "O valor deve ser um valor de data/hora válido (ex: 12/12/2019 12:15:13)")