from flask import request, jsonify
from app.extensions import db
from app.models import Mechanic
from . import mechanics_bp
from .schemas import mechanic_schema, mechanics_schema

# CREATE
@mechanics_bp.route("/", methods=["POST"])
def create_mechanic():
    data = request.json

    mechanic = Mechanic(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone"),
        address=data.get("address"),
        salary=data.get("salary")
    )

    db.session.add(mechanic)
    db.session.commit()

    return mechanic_schema.jsonify(mechanic), 201


# READ ALL
@mechanics_bp.route("/", methods=["GET"])
def get_mechanics():
    all_mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(all_mechanics)


# UPDATE
@mechanics_bp.route("/<int:id>", methods=["PUT"])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    data = request.json

    mechanic.name = data.get("name", mechanic.name)
    mechanic.email = data.get("email", mechanic.email)
    mechanic.phone = data.get("phone", mechanic.phone)
    mechanic.address = data.get("address", mechanic.address)
    mechanic.salary = data.get("salary", mechanic.salary)

    db.session.commit()

    return mechanic_schema.jsonify(mechanic)


# DELETE
@mechanics_bp.route("/<int:id>", methods=["DELETE"])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": "Mechanic deleted"})
