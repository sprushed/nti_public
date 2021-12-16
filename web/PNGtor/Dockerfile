FROM python:3.9.2

WORKDIR /app

COPY . /app

COPY flag /etc/flag

RUN pip3 install -r requirements.txt

RUN chown nobody -R /app
USER nobody

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
