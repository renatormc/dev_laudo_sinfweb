from converters import str2date

context = {
        "pericia": {
            "rg": "11235",
            "ano": "2022",
            "relator": {
                "nome": "João Castro Almeida"
            }
    
        },
        "revisor": {
            "nome": "Romeu Pereira Silva"
        },
        "procedimento": "IP 12345/2022",
        "requisitante": "Delegacia de Caldas Novas",
         "autoridade": "Roberto Costa Silva", 
        "n_objetos": 5,
        "inicio_exame": str2date("12/12/2021"),
        "data_odin": str2date("10/09/2021"),
        "ocorrencia_odin": "12345/2021",
        "n_quesito": "123456",
        "data_recebimento": str2date("12/09/2021"),
        "lacre_entrada": "1265789456",
        "lacre_saida": "xx",
        "objetos": [
            {
                "type": "Celular",
                "name": "Vestígio 1"
            },
            {
                "type": "Celular",
                "name": "Vestígio 2"
            }
        ]
    }