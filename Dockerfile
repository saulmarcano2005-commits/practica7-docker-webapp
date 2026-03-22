FROM python:3.9

WORKDIR /app

COPY src/ .

RUN pip install flask
RUN pip install mysql-connector-python

CMD ["python","app.py"]
