
from flask import Flask
from flask import jsonify

import uuid
import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello():
    response = {
        'uuid': str(uuid.uuid4()),
        'time': str(datetime.datetime.now()),
        'host': os.uname().nodename
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port='8080')
