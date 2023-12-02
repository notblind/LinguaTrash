FROM python:3.11
WORKDIR /app/LinguaTrash

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app/LinguaTrash

EXPOSE 8000
