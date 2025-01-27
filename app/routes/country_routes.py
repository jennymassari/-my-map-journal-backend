from flask import Blueprint, abort, make_response, request, Response
from app.models.country import Country
from app.models.experience import Experience
from app.db import db
from app.routes.route_utilities import validate_model
import os

bp = Blueprint("country_bp", __name__, url_prefix="/coutry")

# C- Not creating a country, but the user should be able to post if it was borned, visited or want to visit the country.
# R - Not readind all countries, but getting all the users post when page is loaded
# U - Update the user info about the country
# D - Unselect all options?

@bp.post("/<country_id>")
def select_country_option(country_id):
    pass

@bp.get("")
def gel_all_options():
    pass

@bp.patch("/<country_id>")
def update_an_option(country_id):
    pass

@bp.delete("/<country_id>")
def delete_an_option(country_id):
    pass