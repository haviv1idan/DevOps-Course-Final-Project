FROM python:3.11-alpine

WORKDIR /

COPY flask_app /flask_app

RUN pip install -r flask_app/src/requirements.txt

ENTRYPOINT ["flask", "--app", "flask_app/src/app", "run", "--debug", "--host", "0.0.0.0", "--port", "59000"]
