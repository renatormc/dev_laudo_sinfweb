import fastdoc.gui_app.widgets as wt
from fastdoc.gui_app.widgets.swidget import SWidget


def convert_pericia(value):
    parts = value.split("/")
    return {"seq": int(parts[0]), "rg": int(parts[1]), "ano": int(parts[2])}


def convert_relatores(value):
    return [item.strip() for item in value.split(",")]


widgets: list[list[SWidget]] = [
    [
        wt.SText("pericia", required=True, label="Perícia",
                 placeholder="ex: 123/123465/2021", stretch=1, converter=convert_pericia),
        wt.SText("requisitante", required=True,
                 label="Requisitante", stretch=1),
        wt.SText("procedimento", required=True,
                 label="procedimento", stretch=1),
        wt.SText("ocorrencia_odin", label="Ocorrência do ODIN", stretch=1),
    ],
    [
        wt.SDate("data_odin", label="Data Odin"),
        wt.SDate("inicio_exame", label="Data de início do exame"),
        wt.SDate("data_recebimento", label="Data de recebimento"),
    ],
    [
        wt.SText("numero_quesito", label="Número do quesito"),
        wt.SText("autoridade", label="Autoridade"),
    ],
    [
        wt.SText("relatores", label="Relatores",
                 placeholder="Entre os relatores separados por vírgula", converter=convert_relatores),
        wt.SText("revisor", label="Revisor"),
    ],
    [
        wt.SText("lacre_entrada", label="Lacre de entrada"),
        wt.SText("lacre_saida", label="Lacre de saída")
    ],
    [
        wt.SObjetctsByPics("objects", "Pasta com fotos dos objetos")
    ]

]
