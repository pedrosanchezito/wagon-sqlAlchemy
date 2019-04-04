import os
import logging
logging.warn(os.environ["DUMMY"])

from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route('/hello')
def hello():
    return "Hello World!"
