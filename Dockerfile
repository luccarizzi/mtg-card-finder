FROM python:3.10.0-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./app.py"]