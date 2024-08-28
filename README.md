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
   
2. **Configure a versão correta do Python com pyenv:**
    ```bash
   pyenv install 3.12.1
   pyenv local 3.12.1

3. **Ativação do ambiente virtual Poetry e download das dependências do projeto:**
    ```bash
   poetry install
   poetry shell

4. **Baseado no .env-example, crie seu arquivo .env para definir suas variáveis locais:**
    ```bash
   touch .env
    ```

5. **Iniciando a API**
    ```bash
    fastapi run api/app/main.py

6. **Iniciando aplicação web**
    ```bash
    streamlit run frontend/main.py

7. *Acesse a aplicação web na sua rede local, pelo link: <a href="http://localhost:8501/">http://localhost:8501/<a>*