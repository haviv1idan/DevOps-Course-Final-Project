FROM python:3.11-alpine

WORKDIR /app

COPY ./python_server/ /app/

RUN pip install -r src/requirements.txt

CMD ["fastapi", "dev", "src/main.py", "--port", "8000", "--host", "0.0.0.0"]
