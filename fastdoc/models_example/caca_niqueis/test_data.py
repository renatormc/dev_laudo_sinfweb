from rlibs.report_writer.converters import str2date

def get_context():
    return {
        "tipo_exame": "VISTORIA EM OBJETOS",
        "procedimento": "RAI 19509193",
        "requisitante": "5ª Delegacia Distrital de Polícia de Goiânia",
        "data_exame": str2date("04/02/2022"),
        "pericia": {
            'sinf': 43,
            'rg': 6281,
            'ano': 2022,
        },
        'relatores': ["Rodrigo Jorge Neves", "Conan de Almeida Alfonso"],
        'revisores': [],
        "n_objetos": 2,
        "ocorrencia_odin": "24211/2021",
        "n_quesito": 246276,
        "autoridade": "Jacó Machado das Chagas",

        "maquinas_molhadas" : False,
        "maquinas_funcionaram": ["1", "2"],
        "valor_encontrado" : 250.00,

        "pasta_fotos": r'/media/renato/charlie/tests/pericia/FOTOS',
    }