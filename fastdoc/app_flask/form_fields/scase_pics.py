from wtforms import Field
from wtforms.widgets import TextInput
import json
from rlibs.report_writer.types import CaseObjectsType


class SCasePics(Field):
    widget = TextInput()

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        elif self.data:
            return self.data
        else:
            return u''

    def process_formdata(self, valuelist):
        
        try:
            data = json.loads(valuelist[0])
            
            obj = CaseObjectsType().from_dict(data)
            self.data = obj
        except Exception as e:
            print(e)
            self.data = CaseObjectsType()
            raise ValueError(str(e))
