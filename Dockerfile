FROM ubuntu:latest
RUN apt-get -y update 
RUN apt-get -y install python3-pip
RUN pip3 install flask

COPY . /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 5000
CMD ["flask", "run"]