#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.order_by(Bakery.id).all()

    for bakery in bakeries: 
        bakeries_list = [bakery.to_dict()]

    response = make_response(bakeries_list, 200)
    return response


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id=id).first()

    bakery_id = bakery.to_dict()

    response = make_response(bakery_id, 200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()

    for goods in baked_goods:
        baked_goods_list = [goods.to_dict()]

    response = make_response(baked_goods_list, 200)
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).first()

    most_expensive_good = baked_goods.to_dict()

    response = make_response(most_expensive_good, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
