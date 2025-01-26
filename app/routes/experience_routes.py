from flask import Blueprint, abort, make_response, request
from app.models.experience import Experience
from app.db import db
from app.routes.route_utilities import validate_model

bp = Blueprint("experience_bp", __name__, url_prefix="/experiences")