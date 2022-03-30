import gui_app.widgets as wt
from gui_app.widgets.swidget import SWidget


widgets: list[list[SWidget]] = [
    [
        wt.SText("pericia", required=True, label="Perícia"),
        wt.SText("requisitante", label="Requisitante"),
        wt.SText("RAI", label="RAI")
    ],
    [
        wt.SComboBox("funcionamento", label="Funcionamento", choices=['Funcionamento Normal', 'Defeito'], stretch=1),
        wt.SDate("inicio_pericia", label="Início da perícia", stretch=1)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
    [
       wt.SFolderPics("fotos", label="Fotos", required=True, subfolders=True),
       wt.SObjetctsByPics("objects", label="Objetos", required=True)
    ],
]
