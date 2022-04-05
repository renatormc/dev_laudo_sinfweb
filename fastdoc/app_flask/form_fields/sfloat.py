from wtforms import Field
from wtforms.widgets import TextInput


class SFloat(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data is not None:
            return str(self.data).replace(".", ",")
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            text = valuelist[0].replace(",", ".")
        except IndexError:
            return
        try:
            self.data = float(text)
        except Exception as e:
            # self.data = None
            raise ValueError(
                "Valor inválido")