# Fastdoc

Fastdoc é um progama cujo objetivo é facilitar a redação de documentos tais como laudos. Ao executar o programa o usuário escolhe o tipo de documento o qual ele quer criar, preenche um formulário e clica no botão "Gerar docx" e o programa gerará automaticamente um documento no formato docx já com os dados preenchidos o qual pode ser utilizado para impressão direta ou modificações posteriores utilizando um editor de textos como Word. 

# Instalação no Windows binários

Baixe o [pacote](https://www.4shared.com/zip/E9zhHVF_ea/fastdoc.html?) e o descompacte em uma pasta de sua preferência.

# Instalação no Windows modo manual

## Instalar Python versão 3.10

Baixe o [instalador](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe) e efetue a instalação.

## Instalar o git

Efetue a instalação do git em sua máquina. Uma forma de se efetuar tal instalação é utilizando este [link](https://git-scm.com/downloads).
Outra forma de se instalar o git é utilizando [Chocolatey](https://chocolatey.org/install) com  o commando:

```
choco install git
```

## Clone o projeto
Abra o terminal em uma pasta na qual você irá salvar o projeto e execute o seguinte comando
```
git clone https://github.com/renatormc/fastdoc.git
```

## Instale as dependências
Abra o terminal na pasta fastdoc criada e execute os comandos a seguir na sequência

```
py -3.10 -m pip install poetry
py -3.10 -m poetry install
fastdoc.bat start
```

# Como usar

Para utilização do programa execute o arquivo fastdoc_gui.exe. Crie um atalho para tal executável para sua área de trabalho caso necessário.

# Como atualizar

Para atualizar ara o terminal na pasta do projeto e digite o seguinte comando.
```
git pull origin master
py -3.10 -m poetry install
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

