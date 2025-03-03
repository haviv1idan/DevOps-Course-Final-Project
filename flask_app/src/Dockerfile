FROM python:3.11-alpine

WORKDIR /app

COPY . /app/

RUN pip install -r flask_app/src/requirements.txt

CMD ["python", "app.py"]