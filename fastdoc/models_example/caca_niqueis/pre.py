from datetime import datetime
from rlibs.report_writer.helpers import exif_transpose_pics


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
    context['peritos'] = concatenate_peritos(context["pericia"]['relatores'], context["pericia"]['revisores'])
    context["data_atual"] = datetime.now()
    context["num_maquinas_nao_func"] = context["n_objetos"] - context["num_maquinas_funcionaram"]
    exif_transpose_pics(context['fotos'])
