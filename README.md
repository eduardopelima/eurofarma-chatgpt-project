# Projeto Eurofarma

## Tecnologias Utilizadas

- **Python 3.12.1**: Versão do Python utilizada para o desenvolvimento do projeto.
- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **FastAPI**: Framework moderno e rápido para construção de APIs com Python.
- **Poetry**: Ferramenta de gerenciamento de dependências e empacotamento para projetos Python.
- **Docker**: Plataforma de containerização utilizada para criar ambientes isolados e consistentes para o desenvolvimento e execução da aplicação.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar e gerenciar os dados da aplicação.

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

4. **Criando seu arquivo .env**
    <p>Baseado no arquivo na pasta raiz do projeto ".env-example", crie seu próprio arquivo na pasta raiz chamado ".env". Caso você já tenha uma instância PostgreSQL, altere para suas variáveis:</p>

    ```bash
   touch .env

5. **(opcional, caso já tenha um PostgreSQL configurado) Subindo um PostgreSQL localmente:**
    ```bash
    docker-compose -f ./database/docker-compose.yaml up -d

6. **Iniciando a API**
    ```bash
    fastapi run api/app/main.py

7. **Iniciando aplicação web**
    ```bash
    streamlit run frontend/main.py

8. **Acesse a aplicação web na sua rede local, pelo link: <a href="http://localhost:8501/">http://localhost:8501/<a>**