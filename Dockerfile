FROM python:3.8-buster

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/app.py .

ENV PYTHONUNBUFFERED=TRUE
CMD python3 app.py

EXPOSE 5000
