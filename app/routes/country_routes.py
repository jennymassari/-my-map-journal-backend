from flask import Blueprint, abort, make_response, request, Response
from app.models.country import Country
from app.models.experience import Experience
from app.db import db
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
import os

bp = Blueprint("country_bp", __name__, url_prefix="/country")

@bp.get("")
def gel_all_options():
    return get_models_with_filters(Country, request.args)

@bp.patch("/<country_id>")
def select_country_option(country_id):
    country = validate_model(Country, country_id)

    data = request.get_json()
    borned = data.get('borned', False)
    visited = data.get('visited', False)
    want_to_visit = data.get('want_to_visit', False)

    country.visited = visited
    country.borned = borned
    country.want_to_visit = want_to_visit

    db.session.commit()

    response_body = {
        "message": "Successfully updated the country options",
        "country": country.to_dict() 
    }
    return make_response(response_body, 200)


@bp.put("/<country_id>/unselect")
def unselect_country_option(country_id):
    country = validate_model(Country, country_id)

    country.visited = False
    country.borned = False
    country.want_to_visit = False

    db.session.commit()

    response_body = {
        "message": f"The option for country {country_id} has been unselected.",
        "country": country.to_dict()  
    }
    return make_response(response_body, 200)
