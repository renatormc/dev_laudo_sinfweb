import fastdoc.gui_app.widgets as wt
from fastdoc.gui_app.widgets.swidget import SWidget


widgets: list[list[SWidget]] = [
    [
        wt.SText("nome", required=True, label="Nome", placeholder="Digite o seu nome", stretch=1),
        wt.SSpinBox("idade", label="Idade", stretch=1, min=1, max=100),
    ],
    [
        wt.SText("profissao", required=True, label="Profissão", placeholder="Digite o sua profissão"),
        wt.SDate("data_nascimento", label="Data de nascimento"),
        wt.SFloat("valor_encontrado", label="Valor encontrado", placeholder="Valor em dinheiro", required=True, default=0)
    ],
    [
        wt.SArray("pessoas", label="Pessoas", widgets=[
            [
                wt.SText("nome", required=True, label="Nome", placeholder="Digite o seu nome", stretch=1),
                wt.SSpinBox("idade", label="Idade", stretch=1, min=1, max=100),
            ]
        ])
    ],
    [
        wt.SFileChooser("fotos", label="Fotos", type='dir', required=True)
    ]
  
]