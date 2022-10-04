FROM python

COPY . /home/app

CMD ['python','/home/app/app.py']