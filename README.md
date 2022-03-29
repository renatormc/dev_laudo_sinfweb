# dev_laudo_sinfweb

## Objetivo

Desenvolver templates (docx) de laudos para poderem ser utilizados no sistema Sinfweb

## Como funciona

O Sinfweb possui a capacidade de gerar laudos a partir do preenchimento de um formulário de dados de acordo com o modelo de laudo. Para isto é possível 
criar vários modelos diferentes de laudos. A geração do laudo funciona da seguinte forma:   
1- O usuário preenche um formulário html no sistema Sinfweb.   
2- Os dados preenchidos neste formulários irão formar um contexto (conjunto de dados) que irão ser repassados a um renderizador.   
3- O renderizador irá receber os dados provenientes do formulário e irá gerar um arquivo docx a partir de um template criado também no formato docx.


### Processo de criação de novos modelos

Para se criar novos modelos de laudos é preciso criar um novo formulário html e um novo template docx. No template docx existem instruções na linguagem jinja2 a qual será utilizada para descrever a lógica que irá determinar como o texto do laudo será gerado. Para criar um novo template deve se utilizar um editor de textos comum como Microsoft Word, Only Office, LibreOffice, etc.    
Este projeto tem o propósito de facilitar a criação de novos templates e testá-los antes da integração com o Sinfweb.

## Requisitos

1- Ter instalado o python na versão 3.9  
2- Ter instalado virtualenv  

obs: Caso possuia sinftools instalado não é necessário instalar outra versão no Python

## Configuração

1- Clone o repositório com o comando  
```
git clone https://github.com/renatormc/dev_laudo_sinfweb.git
```

2- Copie a pasta "models_example" e a renomeia para "models"


# Filtros

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

## data_mes_extenso

Converte um objeto do tipo datetime para a data simples.
ex: 12/12/2020 será convertido para "12/12/2020"

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

