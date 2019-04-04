import os
import logging
logging.warn(os.environ["DUMMY"])

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"
