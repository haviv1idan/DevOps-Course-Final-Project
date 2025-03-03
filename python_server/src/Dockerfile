FROM python:3.11-alpine

WORKDIR /app

COPY . /app/

RUN pip install -r python_server/src/requirements.txt

CMD ["fastapi", "dev", "main.py", "--port", "8000", "--host", "0.0.0.0"]