FROM python:3

WORKDIR /usr/src/app

COPY challenge.py /usr/src/app/

RUN pip install requests

CMD [ "python", "./challenge.py" ]