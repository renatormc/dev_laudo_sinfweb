import gui_app.widgets as wt


widgets = [
    [
        wt.SText("requisitante", label="Requisitante", required=True),
        wt.SComboBox("relator",  label="Relator", choices=["Renato Martins Costa", "Danilo Januario Camara", "Rodrigo Jorge Neves"])
    ]
]
