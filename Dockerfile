FROM ubuntu

RUN apt update
RUN apt install -y python python-pip 

RUN pip install Flask 

COPY app.py /opt/app.py

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0

