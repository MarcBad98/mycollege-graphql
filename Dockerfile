FROM python:3

WORKDIR /usr/src/

COPY requirements.txt .

RUN python -m pip install --upgrade pip &&\
    python -m pip install --no-cache-dir -r requirements.txt

COPY ./app/ ./app/

COPY ./wsgi.py .

CMD [ "python", "wsgi.py" ]