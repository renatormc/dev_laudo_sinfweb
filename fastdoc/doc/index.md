# Fastdoc

# Processo de criação e deleção de modelos
Para criar um novo model digite o seguinte comando:
```
python main.py new-model
```

Para deletar um model existente utilize o comando
```
python main.py delete-model
```

*Não delete ou crie modelos deletando ou copiando manualmente as pastas. Sempre utilize os comandos acima.*
## Edite o template docx

Abra o arquivo models/my_model/templates/Main.docx e faça as edições. Nessa etapa é utilizado a biblioteca docxtpl. Para maiores detalhes visite a [documentação](https://docxtpl.readthedocs.io/en/latest/) da lib. A linguagem utilizada dentro do template docx é [Jinja2](https://devhints.io/jinja).

## Crie o formulário de entrada
Para criação do formulário edite o arquivo **models/my_model/qt_form/qt_form.py** utilizando os widgets disponíveis.

# Executar o programa
Para executar o programa utilize o seguinte comando:
```
python main.py gui
```

# Widgets disponíveis

| Widget | Definição |
|--------|-----------|
| SText  |    Aceita texto simples e retorna um objeto do tipo str       |
|  SCheckBox      | Caixa de marcação de verdadeiro ou falso. Retorna um objeto do tipo bool           |
|   SSpinBox  | Aceita números inteiros e retorna um objeto do tipo int.           |
|SComboBox|Caixa de seleção de lista fechada. Retorna um objeto do tipo str.|
|SDate|Recebe um string que representa uma data no formato dd/mm/YYYY. Retorna um objeto do tipo datetime|
|SFolderPics|Recebe o endereço de uma pasta e retorna a lista de imagens encontradas dentro dela com a possiblidade de utilizar subpastas .|
|SObjectsByPics|Destinado ao uso com pasta de fotos de objetos de perícia nomeados seguindo o padrão casepics. Retorna a lista de objetos da perícia pela análise do nome das fotos.|

# Filtros disponíveis

## not_null

Caso a variável seja nula preenche com uma string vazia

## xxx

Caso a variável for nula preenche com "xxx". Útil para deixar certos campos para preencher posteriormente no editor de textos.

## data_completa

Converte um objeto do tipo datetime para a data em extenso.  
ex: 12/12/2020 será convertido para "12 dias do mês de dezembro do ano de 2020"

## data_mes_extenso

Converte um objeto do tipo datetime para a data em extenso.
ex: 12/12/2020 será convertido para "12 de dezembro de 2020"

## numero_extenso_masc

Converte um número para sua grafia em extenso no masculino.
ex: 22 será convertido para "vinte e dois"

## numero_extenso_masc

Converte um número para sua grafia em extenso no feminino.
ex: 22 será convertido para "vinte e duas"


# Funções
## image(path, width)

Insere uma image contida no endereço "path" na largura de "width" em milímetros.

## subdoc(template, context)

Renderiza o template especificado na variável "template" utilizando o contexto passado na variável "context" e insere na posição específicada.

## len(value)

Retorna o tamanho de uma lista.

## to_table(value, per_row)

Converte um array para uma matrix com um número de per_row colunas.

## not_null_or(value, default)

Caso value for nulo retorna o valor default, caso não seja nulo retorna o próprio valor.

## join_path(*args)

Concatena caminhos de arquivos ou diretórios

