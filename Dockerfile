FROM python:3.12-bullseye

RUN pip install poetry

WORKDIR /code

COPY . /code/

RUN poetry install --no-interaction --no-ansi

RUN poetry run python manage.py migrate

ENV OPENAI_API_KEY=$OPENAI_API_KEY

EXPOSE 8000

CMD poetry run gunicorn editcraft.wsgi:application --bind 0.0.0.0:8000 --workers 4