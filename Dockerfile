FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP app.py

EXPOSE 5000
ENTRYPOINT ["bash", "/app/boot.sh"]
