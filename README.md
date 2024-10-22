
Projeto focado em aprender funcionalidades de python para as seguintes ferramentas:
    - Interação direta com banco de dados (mySql);
    - Processamento da informação recebida para disponibilizar em um web Service;
    - Desenvolver um fluxo básico para um banco de dados como uma API.

Será preciso instalar dependencias adicionais ao python para rodar:
    - será necessário um mySql connector compatível com a versão do python;
    - será utilizada a biblioteca Flask para o desenvolvimento do Web Service;
    - uma pequena interface visual será criada usando a biblioteca tkinter.

Preparando o ambiente de trabalho para desenvolver em Python com virtual enviroment:
    Para iniciar o ambiente virtual e trabalhar em um projeto python vamos usar venv
    
    - No terminal navegue até o diretório do projeto e digite o comando:
    python -m venv venv

    - agora para ativar digite o seguinte comando:
    .venv/Scripts/activate

    - criar um arquivo .gitignore para os arquivos locais, e extensões temporárias:

    .venv/
    .env
    __pycache__/
    *.py[cod]
    *.pyo

Com o ambiente preparado podemos começar a instalar as dependências que serão usadas:
    no projeto a versão do python:
    Python 3.12.1

    para adicionar as bibliotecas adicionais serão os seguintes comandos:

    pip install mysql-connector-python
    pip install python-dotenv
    pip install Flask


Estrutura de diretórios para desenvolver o projeto de forma escalável:

    Depois de preparar o ambiente de trabalho é importante estruturar
    os diretórios de forma que facilite a manutenção escalabilidade e
    reaproveitamento de código.

    A princípio dividimos em três pastas dentro da main:

    - frombase(main)
        - api = pasta que conterá o módulo que usa a biblioteca Flask;
        - database = pasta com os conectores de banco de dados (my SQL);
        - interface = pasta dedicada a arquivos de interface gráfica (tkinter);
        - .env = arquivo que contém as variáveis de ambiente e acesso ao database;
        - main.py = arquivo responsável por chamar os módulos a partir da raiz.
