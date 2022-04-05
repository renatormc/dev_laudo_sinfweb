from wtforms import Field
from wtforms.widgets import TextInput
from datetime import datetime


class SStringList(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return ",".join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        
        try:
            self.data = [item.strip() for item in valuelist[0].split(",")]
        except Exception as e:
            self.data = []
            raise ValueError(str(e))