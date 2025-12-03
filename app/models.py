# app/models.py

from app.extensions import db

# ------------------------------------------------
# Customer Model
# ------------------------------------------------
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50), nullable=True)

    vehicles = db.relationship("Vehicle", backref="customer", cascade="all, delete-orphan")


# ------------------------------------------------
# Vehicle Model
# ------------------------------------------------
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

    service_tickets = db.relationship("ServiceTicket", backref="vehicle", cascade="all, delete-orphan")


# ------------------------------------------------
# Mechanic Model
# ------------------------------------------------
class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(120))


# ------------------------------------------------
# Join Table: ServiceTicketMechanic
# ------------------------------------------------
class ServiceTicketMechanic(db.Model):
    __tablename__ = "service_ticket_mechanic"

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("service_ticket.id"))
    mechanic_id = db.Column(db.Integer, db.ForeignKey("mechanic.id"))


# ------------------------------------------------
# Service Ticket Model
# ------------------------------------------------
class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default="open")

    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)

    mechanics = db.relationship(
        "Mechanic",
        secondary="service_ticket_mechanic",
        backref="service_tickets",
    )
