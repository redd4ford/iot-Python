from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from construction_goods.classes.abstract_construction_goods import AbstractConstructionGoods

import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Door(AbstractConstructionGoods, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer_name = db.Column(db.String(32), unique=False)
    price_in_uah = db.Column(db.Float, unique=False)
    color = db.Column(db.String(32), unique=False)
    weight_in_kilograms = db.Column(db.Integer, unique=False)
    length_in_centimeters = db.Column(db.Integer, unique=False)
    width_in_centimeters = db.Column(db.Integer, unique=False)
    wood_type = db.Column(db.String(32), unique=False)

    def __init__(self, producer_name=None, price_in_uah=0.0, color=None, weight_in_kilograms=0,
                 length_in_centimeters=0, width_in_centimeters=0, wood_type=None):
        super().__init__(producer_name, price_in_uah, color, weight_in_kilograms, length_in_centimeters,
                         width_in_centimeters)
        self.wood_type = wood_type


class DoorSchema(ma.Schema):
    class Meta:
        fields = ('producer_name', 'price_in_uah', 'color', 'weight_in_kilograms',
                  'length_in_centimeters', 'width_in_centimeters', 'wood_type')


door_schema = DoorSchema()
doors_schema = DoorSchema(many=True)


@app.route("/door", methods=["POST"])
def create_door():
    producer_name = request.json['producer_name']
    price_in_uah = request.json['price_in_uah']
    color = request.json['color']
    weight_in_kilograms = request.json['weight_in_kilograms']
    length_in_centimeters = request.json['length_in_centimeters']
    width_in_centimeters = request.json['width_in_centimeters']
    wood_type = request.json['wood_type']
    door = Door(
                producer_name,
                price_in_uah,
                color,
                weight_in_kilograms,
                length_in_centimeters,
                width_in_centimeters,
                wood_type
               )
    db.session.add(door)
    db.session.commit()
    return door_schema.jsonify(door)


@app.route("/door", methods=["GET"])
def get_doors():
    all_doors = Door.query.all()
    result = doors_schema.dump(all_doors)
    return jsonify({'doors': result})


@app.route("/door/<id>", methods=["GET"])
def get_door_by_id(id):
    door = Door.query.get(id)
    if not door:
        abort(404)
    return door_schema.jsonify(door)


@app.route("/door/<id>", methods=["PUT"])
def update_door(id):
    door = Door.query.get(id)
    if not door:
        abort(404)
    old_door = copy.deepcopy(door)
    door.producer_name = request.json['producer_name']
    door.price_in_uah = request.json['price_in_uah']
    door.color = request.json['color']
    door.weight_in_kilograms = request.json['weight_in_kilograms']
    door.length_in_centimeters = request.json['length_in_centimeters']
    door.width_in_centimeters = request.json['width_in_centimeters']
    door.wood_type = request.json['wood_type']
    db.session.commit()
    return door_schema.jsonify(door)


@app.route("/door/<id>", methods=["DELETE"])
def delete_door(id):
    door = Door.query.get(id)
    if not door:
        abort(404)
    db.session.delete(door)
    db.session.commit()
    return door_schema.jsonify(door)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, host='0.0.0.0')
