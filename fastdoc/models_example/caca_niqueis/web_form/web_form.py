from email.policy import default
import wtforms as wtf
from fastdoc.app_flask.form_base import FormBase
from fastdoc.app_flask.form_fields import SDateField, SInteger
from wtforms.validators import DataRequired


class WebForm(FormBase):

    nome = wtf.StringField("Nome", validators=[DataRequired("Valor obrigatório")])
    profissao = wtf.StringField("Profissão", validators=[DataRequired("Valor obrigatório")])
    idade = SInteger("Idade", default=10, min=10, max=100)
    data_nascimento = SDateField("Data de nascimento")
   

    def get_layout(self):
        return [
            [(self.nome, 0), (self.profissao, 0)],
            [(self.idade, 0), (self.data_nascimento, 0)],
        ]
