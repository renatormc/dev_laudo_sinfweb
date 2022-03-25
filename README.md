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

## Configuração

1- Clone o repositório com o comando  
```
git clone https://github.com/renatormc/dev_laudo_sinfweb.git
```
2- Abra o terminal na pasta do projeto e crie um virtualenv com o comando  
```
python -m venv .venv
```

3- Copie a pasta "models_example" e a renomeie para "models"  
4- Edite o template models/laudo_examplo/Main.docx   
5- Crie um contexto para testes editando o arquivo models/laudo_exemplo/test_data.py  
6- Realize uma renderização para testar utilizando o comando   
```
python render.py laudo_exemplo
```

Será gerado o arquivo compilado.docx
