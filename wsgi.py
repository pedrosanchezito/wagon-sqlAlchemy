import os
import logging
import json

from flask import Flask, jsonify, request
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema, product_schema

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products', methods = ['GET','POST'])
def products():
    if request.method == 'GET':
        products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
        return products_schema.jsonify(products), 200

    if request.method == 'POST':
        name = json.dumps(request.get_json())
        return "Product created", 201



@app.route('/products/<int:id>', methods = ['GET', 'PATCH'])
def product(id):
    if request.method == 'GET':
        product = db.session.query(Product).get(id)
        return product_schema.jsonify(product), 200

    if request.method == 'PATCH':
        pass

    return "Product not found", 404
