from wtforms import Field
from wtforms.widgets import TextInput
import humanfriendly
from .helpers import format_size, parse_filesize


class SFileSizeField(Field):
    widget = TextInput()

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return format_size(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        try:
            self.data = parse_filesize(valuelist[0])
        except humanfriendly.InvalidSize:
            self.data = None
            raise ValueError('Formato inválido.')
