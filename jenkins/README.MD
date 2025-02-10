# Setup

## smee.io url
Go to smee.io web and start new channel

## create GitHub Webhook
Go to repo settings -> webhooks -> add new webhook

enter the smee.io webhook url in `Payload URL`

## create smee container
Navigate to jenkins folder on this repo and run the following command

Edit the Dockerfile and create a new token word and the smee url

```bash
docker build -t smee-client:<TOKEN> .
```
## Run smee container
run:
```
docker run -itd smee-client:TOKEN
```

## Jenkins configuration
create Jenkins multibranch pipeline

- in Branch Sources enter your repo https url and your access token

- Scan Repository Triggers -> scan by webhook -> <TOKEN>

apply / save

## validate connection
In jenkins pipeline run scan Repository Now

In your local computer:
```bash
❯ docker logs <SMEE-CONTAINER-NAME>
Forwarding https://smee.io/13T6p9okQv4hBWJb to http://127.0.0.1:8080/multibranch-webhook-trigger/invoke?token=TRIVIA
Connected https://smee.io/13T6p9okQv4hBWJb
POST http://127.0.0.1:8080/multibranch-webhook-trigger/invoke?token=TRIVIA - 200
POST http://127.0.0.1:8080/multibranch-webhook-trigger/invoke?token=TRIVIA - 200
POST http://127.0.0.1:8080/multibranch-webhook-trigger/invoke?token=TRIVIA - 200
POST http://127.0.0.1:8080/multibranch-webhook-trigger/invoke?token=TRIVIA - 200
```
