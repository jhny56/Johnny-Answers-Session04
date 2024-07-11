FROM python

WORKDIR /app

COPY . /app

EXPOSE 5000:5000 

ENV DEBIAN_FRONTEND=noninteractive

CMD [ "python","main.py" ]