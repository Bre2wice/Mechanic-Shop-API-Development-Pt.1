# app/customers/routes.py

from flask import request, jsonify
from . import customers_bp
from app.extensions import db
from app.models import Customer
from .schemas import customer_schema, customers_schema


# GET all customers
@customers_bp.get("/")
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)


# POST create customer
@customers_bp.post("/")
def create_customer():
    data = request.get_json()
    new_customer = customer_schema.load(data)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.jsonify(new_customer), 201


# PUT update customer
@customers_bp.put("/<int:id>")
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.get_json()

    customer.name = data.get("name", customer.name)
    customer.phone = data.get("phone", customer.phone)

    db.session.commit()
    return customer_schema.jsonify(customer)


# DELETE customer
@customers_bp.route("/<int:id>", methods=["DELETE"])
def delete_customer(id):
    customer = db.session.get(Customer, id)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    # Check for vehicles
    if customer.vehicles and len(customer.vehicles) > 0:
        return jsonify({"error": "Cannot delete customer with existing vehicles"}), 400

    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted"}), 200

