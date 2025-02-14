FROM node:slim

RUN npm install --global smee-client

ENTRYPOINT [ "smee", "--url", "https://smee.io/13T6p9okQv4hBWJb", "--path", "/multibranch-webhook-trigger/invoke?token=TRIVIA", "--port", "8080" ]

