from flask import Blueprint

service_ticket_mechanics_bp = Blueprint("service_ticket_mechanics", __name__)

from . import routes
