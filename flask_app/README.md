# Flask APP (frontend)

## setup

First we need to run our python server (backend) to communicate with the server
```bash
fastapi dev python_server/main.py
```

After running the server, open new terminal session and run the flask app
```bash
python3 flask_app/app.py
```

open browser with the url: https://localhost:5000 and try this paths:
- https://localhost:5000/questions
- https://localhost:5000/questions/1


## using docker
```bash
docker build -t flask_app:latest .

docker run --name flask_app -p 5000:5000 -t flask_app:latest
```
