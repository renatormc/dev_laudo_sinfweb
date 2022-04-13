import fastdoc.gui_app.widgets as wt
from fastdoc.gui_app.widgets.swidget import SWidget


widgets: list[list[SWidget]] = [
    [
        wt.SVarForm('requisicao', choices=[
            wt.SVarFormItem(choice_value='judiciario', widgets=[
                [
                    wt.SText("processo", required=True, label="Processo"),
                    wt.SDate("data_audiencia", label="Data da audiência"),
                ],
            ]),
            wt.SVarFormItem(choice_value='delegacia', widgets=[
                [
                    wt.SText("inquerito", required=True, label="Inquérito"),
                    wt.SText("nome_delegado", required=True, label="Nome do delegado"),
                ],
            ])
        ])
    ]
]
