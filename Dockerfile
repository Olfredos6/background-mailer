# docker run --rm -v /mnt/fd7836b6-1292-4493-b5e8-e849e35a2ead/Homy/work/my-open-sourced/background-mailer/src:/app bkg-mailer:latest bash -c 'django-admin startproject app .'
# docker run --rm -p 3000:3000 -v /mnt/fd7836b6-1292-4493-b5e8-e849e35a2ead/Homy/work/my-open-sourced/background-mailer/src:/app bkg-mailer:latest
FROM python:3.10-slim
RUN apt update && apt upgrade -y
COPY ./src /app
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD gunicorn --bind :3000 --workers 3 --reload app.wsgi:application