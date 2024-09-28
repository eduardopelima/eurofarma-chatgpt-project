FROM python:3.12
RUN pip install poetry
COPY . /api
WORKDIR /api
RUN poetry install

EXPOSE 8080 

ENTRYPOINT [ "poetry","run","fastapi", "run","main.py","--port=8080", "--host", "0.0.0.0"]