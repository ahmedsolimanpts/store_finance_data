FROM python

COPY . /home/app/

RUN pip install -r /home/app/requierments.txt

CMD ["python3","/home/app/app.py"]