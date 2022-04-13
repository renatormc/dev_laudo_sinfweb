from pathlib import Path
from datetime import datetime
from report_writer.helpers import exif_transpose_folder

def folder_to_matrix(folder):
    rows = []
    for entry in Path(folder).iterdir():
        if entry.is_file():
            continue
        fotos = []
        for entry2 in entry.iterdir():
            if entry2.is_file():
                fotos.append(str(entry2))
        rows.append(fotos)
    return rows

def concatenate_peritos(relatores, revisores):
    peritos = []
    for relator in relatores:
        peritos.append(
            {'nome': relator, 'tipo': 'Perito relator'}
        )
    for revisor in revisores:
        peritos.append(
            {'nome': revisor, 'tipo': 'Perito revisor'}
        )
    return peritos


def pre(context):
    context["num_peritos"] = len(context["pericia"]["relatores"]) + len(context["pericia"]["revisores"])
    context["num_maquinas_funcionaram"] = len(context["maquinas_funcionaram"])
    context["fotos"]=folder_to_matrix(context["pasta_fotos"])
    context['peritos'] = concatenate_peritos(context["pericia"]['relatores'], context["pericia"]['revisores'])
    context["data_atual"] = datetime.now()
    context["num_maquinas_nao_func"] = context["n_objetos"] - context["num_maquinas_funcionaram"]
    exif_transpose_folder(context['pasta_fotos'], recursive=True, verbose=True)
