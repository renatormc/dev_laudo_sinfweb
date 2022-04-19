# Fastdoc

Fastdoc é um progama cujo objetivo é facilitar a redação de documentos tais como laudos. Ao executar o programa o usuário escolhe o tipo de documento o qual ele quer criar, preenche um formulário e clica no botão "Gerar docx" e o programa gerará automaticamente um documento no formato docx já com os dados preenchidos o qual pode ser utilizado para impressão direta ou modificações posteriores utilizando um editor de textos como Word. 

# Instalação no Windows (forma mais fácil)

Baixe o  arquivo [fastdoc 0.1.2.zip](https://www.4shared.com/zip/269yVzYIiq/fastdoc_012.html?) e o descompacte em uma pasta de sua preferência.  
Para utilização execute o arquivo fastdoc_gui.exe. Crie um atalho para ele na area de trabalho caso necessário.

Hash SHA-512 do arquivo "fastdoc 0.1.2.zip": 
```
67e68f48c65f0cbfaaf439e56d86185e213d42a8ca05132033745e2a877cca2c2f4196caf4fc48b7e33068521eaf1ec203be1ddf561d673c2428130f1a21d47d
```

# Instalação Manual

Requisitos:

- Ter Python 3.10 instalado
- Ter git instalado
- Ter Poetry instalado

## Clone o projeto
Abra o terminal em uma pasta na qual você irá salvar o projeto e execute o seguinte comando
```
git clone https://github.com/renatormc/fastdoc.git
```

## Instale as dependências
Abra o terminal na pasta fastdoc criada e execute os comandos a seguir na sequência

```
poetry install
poetry shell
python main.py start
```


## Como usar

Para execução rode o programa com o comando abaixo:
```
python main.py gui
```

## Como atualizar

Para atualizar ara o terminal na pasta do projeto e digite o seguinte comando.
```
git pull origin master
poetry install
```

# Gerenciamento de modelos

Os modelos ficam dentro da pasta "models" na raiz do projeto. Cada subpasta é um modelo diferente.

## Criar novo modelo
Para se criar um novo modelo é necessário executar o comando a seguir:

```
fastdoc.bat new-model
```

## Deletar modelos
Para se deletar um modelo é preciso digitar o comando a seguir.
```
fastdoc.bat delete-model
```
*Não delete ou crie modelos deletando ou copiando manualmente as pastas. Sempre utilize os comandos acima.*

Após criação do novo modelo basicamente o que preciso fazer é editar o arquivo templates/Main.docx dentro da pasta do modelo e criar um formulário no arquivo qt_form/qt_form.py.

