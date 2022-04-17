from datetime import datetime
from rlibs.report_writer.helpers import exif_transpose_pics
from rlibs.report_writer.converters import pics_from_subfolders


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
    context["num_peritos"] = len(context["relatores"]) + len(context["revisores"])
    context["num_maquinas_funcionaram"] = len(context["maquinas_funcionaram"])
    context['peritos'] = concatenate_peritos(context['relatores'], context['revisores'])
    context["data_atual"] = datetime.now()
    context["num_maquinas_nao_func"] = context["n_objetos"] - context["num_maquinas_funcionaram"]   
    context['fotos'] = pics_from_subfolders(context['pasta_fotos'])
    exif_transpose_pics(context['fotos'])

