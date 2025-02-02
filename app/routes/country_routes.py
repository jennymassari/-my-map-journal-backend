from flask import Blueprint, abort, make_response, request, Response, jsonify
from app.models.country import Country
from app.models.experience import Experience
from app.db import db
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
import os

bp = Blueprint("country_bp", __name__, url_prefix="/country")

@bp.get("")
def gel_all_options():
    countries =  get_models_with_filters(Country, request.args)
    return jsonify(countries, 200)

@bp.get("/<country_id>")
def get_a_country(country_id):
    country = db.session.get(Country, country_id)

    db.session.add(country)
    db.session.commit()
    
    return make_response(country.to_dict(), 200)

@bp.post("")
def select_country_option():
    request_body = request.get_json()

    country_id = request_body.get('country_id')
    name = request_body.get("name")
    lat = request_body.get("lat")
    long = request_body.get("long")
    borned = request_body.get('borned', False)
    visited = request_body.get('visited', False)
    want_to_visit = request_body.get('want_to_visit', False)

    country = Country.query.filter_by(id=country_id).first()

    if not country:
        country = Country(id=country_id, name=name, lat=lat, long=long)
        db.session.add(country)

    country.borned = borned
    country.visited = visited
    country.want_to_visit = want_to_visit

    db.session.commit()

    response_body = {
        "message": "Country options have been successfully selected/created.",
        "country": country.to_dict()
    }

    return make_response(response_body, 201) 

@bp.patch("/<country_id>")
def update_country_option(country_id):
    country = validate_model(Country, country_id)


    request_body = request.get_json()


    if request_body.get("unselect_all", False):
        country.borned = False
        country.visited = False
        country.want_to_visit = False
    else:

        if "borned" in request_body:
            country.borned = request_body["borned"]
        if "visited" in request_body:
            country.visited = request_body["visited"]
        if "want_to_visit" in request_body:
            country.want_to_visit = request_body["want_to_visit"]

    db.session.commit()

    response_body = {
        "message": "Successfully updated the country options",
        "country": country.to_dict()
    }

    return make_response(response_body, 200)

