FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app
# WORKDIR /app

ENV PATH $PATH:/home/django/.local/bin

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.4.1
RUN poetry config virtualenvs.create false
RUN poetry install --no-root


COPY . .

EXPOSE 8000
