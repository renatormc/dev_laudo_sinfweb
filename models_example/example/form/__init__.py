import gui_app.widgets as wt
from gui_app.widgets.swidget import SWidget


widgets: list[list[SWidget]] = [
    [
        wt.SText("nome", required=True, label="Nome", placeholder="Digite o seu nome", stretch=1),
        wt.SSpinBox("idade", label="Idade", stretch=1, min=1, max=100),
    ],
    [
        wt.SText("profissao", required=True, label="Profissão", placeholder="Digite o sua profissão"),
        wt.SDate("data_nascimento", label="Data de nascimento"),
    ]
  
]
