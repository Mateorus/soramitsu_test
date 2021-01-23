FROM python:3

EXPOSE 80
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./server.py" ]
