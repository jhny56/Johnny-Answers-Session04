FROM python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000:5000 

ENV DEBIAN_FRONTEND=noninteractive

CMD [ "python","src/main.py" ]