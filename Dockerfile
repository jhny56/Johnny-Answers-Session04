FROM python

WORKDIR /app

COPY . /app

EXPOSE 5000:5000 

ENV DEBIAN_FRONTEND=noninteractive

RUN python -m unittest discover -s tests

CMD [ "python","main.py" ]