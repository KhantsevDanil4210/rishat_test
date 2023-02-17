FROM python:3.8.5

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
