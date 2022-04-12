import fastdoc.gui_app.widgets as wt
from fastdoc.gui_app.widgets.svar_form.svar_form_item import SVarFormItem
from fastdoc.gui_app.widgets.swidget import SWidget


widgets: list[list[SWidget]] = [
    [
        wt.SText("nome", required=True, label="Nome", placeholder="Digite o seu nome", stretch=1),
        wt.SSpinBox("idade", label="Idade", stretch=1, min=1, max=100),
    ],
    [
        wt.SText("profissao", required=True, label="Profissão", placeholder="Digite o sua profissão"),
        wt.SDate("data_nascimento", label="Data de nascimento"),
    ],
    [
        wt.SVarForm("requisicao", label="Requisição", choices=[
            wt.SVarFormItem(choice_value="judiciario", widgets=[
                [
                    wt.SText("processo", required=True, label="Processo"),
                    wt.SDate("data_prisao", label="Data da prisão"),
                ],
            ]),
            wt.SVarFormItem(choice_value="delegacia", widgets=[
                [
                    wt.SText("inquerito", required=True, label="Inquérito"),
                    wt.SText("nome_delegado", label="Nome do delegado"),
                ],
            ]),
        ])
    ]

]
