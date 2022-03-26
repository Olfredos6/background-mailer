FROM python:3.10-slim
RUN apt update && apt upgrade -y
COPY ./src /app
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD gunicorn --bind :3000 --workers 3 --reload app.wsgi:application