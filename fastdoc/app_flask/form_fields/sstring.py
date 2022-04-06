from wtforms import StringField, validators
from .helpers import add_render_kw, add_validators

class SString(StringField):
    def __init__(self, *args, placeholder="", required=False, **kargs):
        if placeholder is not None:
            add_render_kw(kargs, 'placeholder', placeholder)
        if required:
            add_validators(kargs, [validators.DataRequired("Campo obrigatório")])
        super().__init__(*args, **kargs)
   
