import requests
from flask import Flask

from skeleton.settings import REMOTE_SERVICE_URL, HTTP_TIMEOUT

app = Flask(__name__)

# This is an alternative way of loading the settings for flask
# app.config.from_object('skeleton.settings')
# Then you can load the settings through
#     app.config["REMOTE_SERVICE_URL"]


@app.route('/')
def hello_world():
    response = requests.get(REMOTE_SERVICE_URL + "/hello", timeout=HTTP_TIMEOUT)
    return f"got response from other server: {response.content}"
