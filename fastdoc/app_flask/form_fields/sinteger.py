from wtforms import Field
from wtforms.widgets import TextInput


class SInteger(Field):
    widget = TextInput()

    def __init__(self, *args, min: int = None, max: int = None, **kargs):
        super().__init__(*args, **kargs)
        self.min = min
        self.max = max

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data is not None:
            return self.data
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            text = valuelist[0]
        except IndexError:
            return
        try:
            self.data = int(text)
            if self.min and self.data < self.min:
                raise Exception("")
            if self.max and self.data > self.max:
                raise Exception("")
        except Exception as e:
            # self.data = None
            raise ValueError("Valor inválido")
