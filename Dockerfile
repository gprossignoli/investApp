FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /investApp
COPY requirements.txt /investApp/
COPY 
RUN pip install -r requirements.txt
COPY . /investApp/
