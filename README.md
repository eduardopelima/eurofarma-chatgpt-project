# Meu Projeto Python

Este é um projeto Python que utiliza **Streamlit**, **FastAPI** e **Poetry** para criar uma aplicação web e uma API. O projeto está configurado para usar a versão **Python 3.12.1** localmente.

## Tecnologias Utilizadas

- **Python 3.12.1**: Versão do Python utilizada para o desenvolvimento do projeto.
- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **FastAPI**: Framework moderno e rápido para construção de APIs com Python.
- **Poetry**: Ferramenta de gerenciamento de dependências e empacotamento para projetos Python.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/eduardopelima/eurofarma-chatgpt-project
   cd eurofarma-chatgpt-project
   
2. **Setar versão correta do Python localmente:**
    ```bash
   pyenv local 3.12.1

3. **Ativação do ambiente Poetry e download das bibliotecas**
    ```bash
   poetry install
   poetry shell

4. **Arquivo de variáveis locais**
    ```bash
   touch .env
    ```

   <p>Dentro do arquivo de variáveis, preencha: <p>

   ```plaintext
    DATABASE_USERNAME=
    DATABASE_PASSWORD=
    DATABASE_HOST=
    DATABASE_PORT=
    DATABASE_NAME=
   ```

5. **Iniciando a API**
    ```bash
    fastapi run api/app/main.py

6. **Iniciando aplicação web**
    ```bash
    streamlit run frontend/main.py