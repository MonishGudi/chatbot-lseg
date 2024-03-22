FROM python:slim

WORKDIR /app

COPY . /app

CMD ["python", "chatbot.py"]

