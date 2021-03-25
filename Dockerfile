FROM python:3.6.1

WORKDIR /dockertest

ADD . /dockertest

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]