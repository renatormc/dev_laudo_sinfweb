from report_writer.converters import str2date

context: dict = {
  "nome": "Renato Martins Costa",
  "idade": 38,
  "profissao": "Perito Criminal",
  "data_nascimento": str2date("30/08/1984")
}