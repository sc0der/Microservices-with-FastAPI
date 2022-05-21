FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install python-multipart

ENTRYPOINT ["uvicorn", "app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "4050"]