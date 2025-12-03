from . import service_ticket_mechanics_bp
from app.models import ServiceTicketMechanic
from .schemas import st_mech_schema, st_mechs_schema


@service_ticket_mechanics_bp.get("/")
def get_all_links():
    links = ServiceTicketMechanic.query.all()
    return st_mechs_schema.jsonify(links)


@service_ticket_mechanics_bp.get("/<int:id>")
def get_link(id):
    link = ServiceTicketMechanic.query.get_or_404(id)
    return st_mech_schema.jsonify(link)
