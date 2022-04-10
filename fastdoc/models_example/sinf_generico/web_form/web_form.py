import wtforms as wtf
from fastdoc.app_flask.form_base import FormBase
from fastdoc.app_flask.form_fields import SDateField, SStringList, SCasePics
from fastdoc.helpers import get_objects_from_folder
from fastdoc import config

class WebForm(FormBase):

    # pericia = wtf
    relatores = SStringList("Relatores", render_kw={'placeholder': 'Relatores separados por vírgula'})
    revisores = SStringList("Revisores", render_kw={'placeholder': 'Revisores separados por vírgula'})
    requisitante = wtf.StringField("Requisitante", render_kw={
                                   'placeholder': "Delegacia, vara criminal ou núcleo"})
    procedimento = wtf.StringField("Procedimento", render_kw={
                                   'placeholder': "RAI, IP, etc"})
    ocorrencia_odin = wtf.StringField("Ocorrência ODIN")
    data_odin = SDateField("Data Odin", render_kw={
                           'placeholder': 'ex: 12/12/2019'})
    n_quesito = wtf.StringField("Número do quesito")
    autoridade = wtf.StringField("Autoridade", render_kw={
                                 'placeholder': "Nome do delegado ou juiz que requisitou"})
    inicio_exame = SDateField("Inicio do exame", render_kw={
                              'placeholder': 'ex: 12/12/2019'})
    data_recebimento = SDateField("Data de recebimento", render_kw={
                                  'placeholder': 'Data em que a seção recebeu os objetos'})
    lacre_entrada = wtf.StringField("Lacre de entrada")
    lacre_saida = wtf.StringField("Lacre de saída")
    objects = SCasePics("Objects")
    # tipo_laudo = wtf.HiddenField()

    def get_layout(self):
        return [
            [(self.requisitante, 8), (self.procedimento, 4)],
            [(self.ocorrencia_odin, 0), (self.data_odin, 0),  (self.inicio_exame, 0), (self.data_recebimento, 0)],
            [(self.autoridade, 0), (self.n_quesito, 0)],
            [(self.lacre_entrada, 0), (self.lacre_saida, 0)],
            [(self.relatores, 0)],
            [(self.revisores, 0)],
            [(self.objects, 0)],
        ]

    def load_initial_data(self) -> None:
        self.objects.data = get_objects_from_folder(config.workdir / "fotos")
