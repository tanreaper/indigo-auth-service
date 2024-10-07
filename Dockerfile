FROM python:latest

#inside of my image/container i am trying to create a directory
WORKDIR /app

ENV FLASK_APP=app.py

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

CMD [ "python", "app.py"]