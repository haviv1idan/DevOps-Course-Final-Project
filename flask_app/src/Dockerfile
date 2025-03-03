FROM python:3.11-alpine

WORKDIR /app

COPY . /app/

RUN pip install -r app/requirements.txt

ENTRYPOINT ["python", "app.py"]