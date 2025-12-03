Mechanic Shop API
#### Overview

The Mechanic Shop API is a RESTful API built with Flask, SQLAlchemy, and Marshmallow, designed to manage a mechanic shop’s resources including customers, vehicles, mechanics, service tickets, and service ticket assignments. The API follows the Application Factory Pattern and uses Blueprints for modularity.

## Features

## Customers

Create, Read, Update, Delete (CRUD)

Each customer can have multiple vehicles

## Vehicles

CRUD operations

Each vehicle belongs to a customer

## Mechanics

CRUD operations

## Service Tickets

Create tickets for vehicle service

Assign and remove mechanics

Track work performed, estimated and final costs

## Service Ticket Mechanics

Manage relationships between service tickets and mechanics

Track hours worked and roles

### My File Structure
backend/
│
├── app/
│   ├── __init__.py               # Application Factory
│   ├── extensions.py             # db and ma initialization
│   ├── models.py                 # SQLAlchemy models
│   │
│   ├── customers/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── vehicles/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── mechanics/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── service_tickets/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   └── service_ticket_mechanics/
│       ├── __init__.py
│       ├── routes.py
│       └── schemas.py
│
└── venv/                         # Virtual environment


### Setup Instructions

## Clone the repository:

git clone <repo-url>
cd backend


## Set up virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


## Install dependencies:

pip install -r requirements.txt


## Configure MySQL database:

Create a database named mechanic_shop.

## Update database URI in app/__init__.py:

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@localhost/mechanic_shop"


## Run the application:

export FLASK_APP=app
flask run

### API Endpoints
## Customers

POST /customers/ → Create a customer

GET /customers/ → Retrieve all customers

GET /customers/<id> → Retrieve specific customer

PUT /customers/<id> → Update customer

DELETE /customers/<id> → Delete customer

## Vehicles

POST /vehicles/ → Create a vehicle

GET /vehicles/ → Retrieve all vehicles

GET /vehicles/<id> → Retrieve specific vehicle

PUT /vehicles/<id> → Update vehicle

DELETE /vehicles/<id> → Delete vehicle

## Mechanics

POST /mechanics/ → Create a mechanic

GET /mechanics/ → Retrieve all mechanics

GET /mechanics/<id> → Retrieve specific mechanic

PUT /mechanics/<id> → Update mechanic

DELETE /mechanics/<id> → Delete mechanic

## Service Tickets

POST /service-tickets/ → Create service ticket

GET /service-tickets/ → Retrieve all service tickets

PUT /service-tickets/<id>/assign-mechanic/<mechanic_id> → Assign a mechanic

PUT /service-tickets/<id>/remove-mechanic/<mechanic_id> → Remove a mechanic

## Service Ticket Mechanics

POST /service-ticket-mechanics/ → Create a ticket-mechanic assignment

GET /service-ticket-mechanics/ → Retrieve all assignments

GET /service-ticket-mechanics/<id> → Retrieve specific assignment

PUT /service-ticket-mechanics/<id> → Update assignment

DELETE /service-ticket-mechanics/<id> → Delete assignment

## Testing

All endpoints should be tested in Postman.

A Postman collection is included with pre-configured requests for each endpoint.

Ensure to include JSON bodies where required and set Content-Type: application/json.

## Notes

Relationships are enforced via foreign keys (customer_id, vehicle_id, mechanic_id).

Marshmallow schemas handle serialization and deserialization.

Follow the Application Factory Pattern and Blueprints to keep the project modular and scalable.
