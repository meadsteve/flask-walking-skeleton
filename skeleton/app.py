import os

import requests
from flask import Flask

REMOTE_SERVICE_URL = os.environ['REMOTE_SERVICE_URL']

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = requests.get(REMOTE_SERVICE_URL + "/hello")
    return f"got response from other server: {response.content}"
