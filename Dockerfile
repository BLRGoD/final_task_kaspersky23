FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install -r ./app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["python uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
