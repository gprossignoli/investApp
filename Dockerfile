FROM python:3.9-buster

RUN apt-get -y update

EXPOSE 8001

RUN useradd --create-home investappuser

WORKDIR /home/investappuser/investapp

COPY requirements.txt .
RUN pip --default-timeout=1000 install -r requirements.txt

COPY investapp ./investapp
COPY markets ./markets
COPY profiles ./profiles
COPY static ./static
COPY templates ./templates
COPY utils ./utils
RUN touch investapp.log investapp_errors.log
COPY manage.py .
COPY .env .
COPY entrypoint.sh ./entrypoint.sh

RUN chown -R investappuser .
RUN chmod -R 700 .

USER investappuser
