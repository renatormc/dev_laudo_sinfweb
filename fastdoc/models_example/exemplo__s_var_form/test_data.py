from rlibs.report_writer.converters import str2date

context: dict = {
    "nome": "joão Silva Pereira",
    "profissao": "carpinteiro",
    "idade": 28,
    "ano_nascimento": str2date("12/12/1990"),
    "pessoas": [
        {'nome': 'Robson Araujo de Souza', 'idade': 19},
        {'nome': 'Maria do Carmos de Jesus', 'idade': 35}
    ]
}