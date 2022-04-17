import fastdoc.gui_app.widgets as wt
from fastdoc.gui_app.widgets.swidget import SWidget


def pericia_converter(value):
    try:
        parts = value.split("/")
        return {'sinf', int(parts[0]), 'rg', int(parts[1]), 'ano', int(parts[2])}
    except:
        raise wt.ValidationError("Valor incorreto")

widgets: list[list[SWidget]] = [
    [
        wt.SText("pericia", required=True, label="Perícia", placeholder="SINF/RG/ANO", converter=pericia_converter),
        wt.SText("ocorrencia_odin",label="Ocorrência ODIN"),
        wt.SText("n_quesito",label="Número do quesito"),
        wt.SText("tipo_exame", required=True, label="Tipo do exame", default="VISTORIA EM OBJETOS"),
     
    ],
    [ 
        wt.SText("procedimento", label="Procedimento", placeholder="RAI, Inquérito ou Processo"),
        wt.SText("requisitante", label="Requisitante", placeholder="Nome da delegacia ou judiciário"),
        wt.SText("autoridade", label="Autoridade", placeholder="Nome do delegado ou juiz"),
    ],
    [
        wt.SSpinBox("n_objetos", label="Número de objetos"),
        wt.SStringList("maquinas_funcionaram", label="Máquinas que funcionaram", placeholder="Número das máquinas separados por vírgula"),
        wt.SFloat("valor_encontrado", label="Valor encontrado", default=0.0),
        wt.SCheckBox("maquinas_molhadas", label="Máquinas molhadas", default=False),
    ],
    [
        wt.SFileChooser('pasta_fotos', label="Pasta com as fotos", type='dir')
    ],
    [
       wt.SStringList('relatores', label="Relatores", placeholder="Relatores separados por vírgula")
    ],
    [
       wt.SStringList('revisores', label="Revisores", placeholder="Revisores separados por vírgula")
    ]
  
  
]