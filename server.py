from flask import Flask
from datetime import datetime,timezone
import pytz


app = Flask(__name__)

@app.route('/', methods=['GET'])
def utc_moscow():
    time = datetime.now(pytz.timezone('Europe/Moscow'))
    return time.strftime("%H:%M:%S")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
