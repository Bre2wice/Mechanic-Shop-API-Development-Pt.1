from flask import request, jsonify
from app.extensions import db
from app.models import ServiceTicket, Mechanic, ServiceTicketMechanic
from . import service_tickets_bp
from .schemas import service_ticket_schema, service_tickets_schema

# CREATE SERVICE TICKET
@service_tickets_bp.route("/", methods=["POST"])
def create_ticket():
    data = request.json

    new_ticket = ServiceTicket(
        vehicle_id=data["vehicle_id"],
        odometer_reading=data["odometer_reading"],
        description_of_issue=data.get("description_of_issue"),
        work_performed=data.get("work_performed"),
        estimated_cost=data.get("estimated_cost"),
        final_cost=data.get("final_cost"),
        status=data.get("status", "open")
    )

    db.session.add(new_ticket)
    db.session.commit()

    return service_ticket_schema.jsonify(new_ticket), 201


# GET ALL TICKETS
@service_tickets_bp.route("/", methods=["GET"])
def get_tickets():
    tickets = ServiceTicket.query.all()
    return service_tickets_schema.jsonify(tickets)


# ASSIGN MECHANIC
@service_tickets_bp.route("/<int:ticket_id>/assign-mechanic/<int:mechanic_id>", methods=["PUT"])
def assign_mechanic(ticket_id, mechanic_id):

    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)

    assignment = ServiceTicketMechanic(ticket_id=ticket.id, mechanic_id=mechanic.id)

    db.session.add(assignment)
    db.session.commit()

    return jsonify({"message": "Mechanic assigned to ticket"})


# REMOVE MECHANIC
@service_tickets_bp.route("/<int:ticket_id>/remove-mechanic/<int:mechanic_id>", methods=["PUT"])
def remove_mechanic(ticket_id, mechanic_id):

    assignment = ServiceTicketMechanic.query.filter_by(
        ticket_id=ticket_id, mechanic_id=mechanic_id
    ).first_or_404()

    db.session.delete(assignment)
    db.session.commit()

    return jsonify({"message": "Mechanic removed from service ticket"})
