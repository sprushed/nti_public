FROM python:3.9.2

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

#RUN apt update && install -y gunicorn python-gevent

RUN chown nobody -R /app
USER nobody

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
#CMD "gunicorn --keep-alive 10 -k gevent --bind 0.0.0.0:5000 -w 4 app:app"
