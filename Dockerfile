FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /code/src
CMD python manage.py collectstatic --noinput; gunicorn acacia.wsgi:application --bind 0.0.0.0:$PORT --log-file -
