
from flask import Blueprint

main = Blueprint('main', __name__)

from app.main import routes  # Import routes to register the blueprint's routes
