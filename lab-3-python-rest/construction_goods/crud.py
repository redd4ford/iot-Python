from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from construction_goods.classes.abstract_construction_goods import AbstractConstructionGoods
import json
from flask_cors import cross_origin
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Door(AbstractConstructionGoods, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer = db.Column(db.String(32), unique=False)
    price = db.Column(db.Float, unique=False)
    color = db.Column(db.String(32), unique=False)
    weight = db.Column(db.Integer, unique=False)
    height = db.Column(db.Integer, unique=False)
    wood_type = db.Column(db.String(32), unique=False)

    def __init__(self, producer=None, price=0.0, color=None, weight=0,
                 height=0, wood_type=None):
        super().__init__(producer, price, color, weight, height)
        self.wood_type = wood_type


class DoorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'producer', 'price', 'color', 'weight',
                  'height', 'wood_type')


door_schema = DoorSchema()
doors_schema = DoorSchema(many=True)


@app.route("/door", methods=["POST"])
@cross_origin()
def create_door():
    producer_name = request.json['producer']
    price_in_uah = request.json['price']
    color = request.json['color']
    weight_in_kilograms = request.json['weight']
    height_in_centimeters = request.json['height']
    wood_type = request.json['wood_type']
    door = Door(
        producer_name,
        price_in_uah,
        color,
        weight_in_kilograms,
        height_in_centimeters,
        wood_type
    )
    db.session.add(door)
    db.session.commit()

    response = door_schema.jsonify(door)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/door", methods=["GET"])
def get_doors():
    all_doors = Door.query.all()
    result = doors_schema.dump(all_doors)
    
    response = jsonify(result)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/door/<id>", methods=["GET"])
@cross_origin()
def get_door_by_id(id):
    door = Door.query.get(id)
    if not door:
        abort(404)

    response = door_schema.jsonify(door)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/door/<id>", methods=["PUT"])
@cross_origin()
def update_door(id):
    door = Door.query.get(id)
    if not door:
        abort(404)
    old_door = copy.deepcopy(door)
    door.producer = request.json['producer']
    door.price = request.json['price']
    door.color = request.json['color']
    door.weight = request.json['weight']
    door.height = request.json['height']
    door.wood_type = request.json['wood_type']
    db.session.commit()
    response = door_schema.jsonify(door)
    return response


@app.route("/door/<id>", methods=["DELETE"])
def delete_door(id):
    door = Door.query.get(id)
    if not door:
        abort(404)
    db.session.delete(door)
    db.session.commit()
    response = door_schema.jsonify(door)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, host='localhost', port=8090)
