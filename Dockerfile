FROM python:3.6

ADD app.py .

RUN pip install prometheus_client

CMD ["python", "./app.py"]


