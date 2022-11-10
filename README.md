# TEXT TO SPEECH

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-<COLOR>.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)](https://shields.io)

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Instruções](#Instruções)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Licença](#Licença)

# Descrição do Projeto


## Tecnologias utilizadas

- [Python versão 3](https://docs.python.org/3/)
- [Pacote gtts](https://gtts.readthedocs.io/en/latest/)

## Instruções

1. Ative um ambiente virtual (virtualenv, venv, pyenv, etc.). 

2. Instale os requisitos desse projeto
    ```
    pip install -r requirements.txt
    ```
3. Rode a aplicação
    ```
    python text-to-speech.py <TEXTO  A SER CONVERTIDO> <IDIOMA ( VER LISTA )> <DIRETÓRIO PARA SALVAR O ARQUIVO CONVERTIDO>
    ```
    Exemplo
    
    ```
    python text-to-speech.py "Hello World!" en /home/audio
    ```

## Licença

[Licença MIT](./LICENSE) © César Augusto de Carvalho Calafrioli Móes
