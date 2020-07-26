FROM python:alpine3.11

RUN mkdir -p /opt/sfia2/

COPY . /opt/sfia2/

WORKDIR /opt/sfia2/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "app.py"]