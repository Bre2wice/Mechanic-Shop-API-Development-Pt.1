from flask import request, jsonify
from app.extensions import db
from app.models import Vehicle
from . import vehicles_bp
from .schemas import vehicle_schema, vehicles_schema


# CREATE a vehicle
@vehicles_bp.route("/", methods=["POST"])
def create_vehicle():
    data = request.json
    vehicle = Vehicle(
        customer_id=data["customer_id"],
        make=data["make"],
        model=data["model"],
        year=data["year"],
        vin=data["vin"]
    )
    db.session.add(vehicle)
    db.session.commit()
    return vehicle_schema.jsonify(vehicle), 201


# GET all vehicles
@vehicles_bp.route("/", methods=["GET"])
def get_vehicles():
    vehicles = db.session.query(Vehicle).all()
    return vehicles_schema.jsonify(vehicles), 200


# GET vehicle by ID
@vehicles_bp.route("/<int:id>", methods=["GET"])
def get_vehicle(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle:
        return jsonify({"message": "Vehicle not found"}), 404
    return vehicle_schema.jsonify(vehicle), 200


# UPDATE a vehicle
@vehicles_bp.route("/<int:id>", methods=["PUT"])
def update_vehicle(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle:
        return jsonify({"message": "Vehicle not found"}), 404

    data = request.json
    vehicle.make = data.get("make", vehicle.make)
    vehicle.model = data.get("model", vehicle.model)
    vehicle.year = data.get("year", vehicle.year)
    vehicle.vin = data.get("vin", vehicle.vin)
    vehicle.customer_id = data.get("customer_id", vehicle.customer_id)

    db.session.commit()
    return vehicle_schema.jsonify(vehicle), 200


# DELETE a vehicle
@vehicles_bp.route("/<int:id>", methods=["DELETE"])
def delete_vehicle(id):
    vehicle = db.session.get(Vehicle, id)
    if not vehicle:
        return jsonify({"message": "Vehicle not found"}), 404

    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle deleted"}), 200
