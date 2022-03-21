FROM ubuntu
LABEL MAINTAINER="Chiheb Edine Zoghlemi  <chihebedine.zoghlemi@gmail.com>"
RUN apt-get update -y && apt-get install -y python3 python3-pip python-dev
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000 27017
ENTRYPOINT [ "python3" ]
CMD ["app.py" ]
