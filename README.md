# Fastdoc


# Instalação no Windows

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

Para utilização do programa execute o arquivo fastdoc.exe. Crie um atalho para tal executável para sua área de trabalho caso ache necessário.

