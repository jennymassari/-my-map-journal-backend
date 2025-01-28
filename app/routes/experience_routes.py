from flask import Blueprint, abort, make_response, request
from app.models.experience import Experience
from app.models.country import Country
from app.db import db
from app.routes.route_utilities import validate_model
import os

bp = Blueprint("experience_bp", __name__, url_prefix="/experiences")

@bp.get("")
def get_all_experiences():
    query = db.select(Experience)
    
    query= query.order_by(Experience.id)
    experiences = db.session.scalars(query)
    
    response_body = [experience.to_dict() for experience in experiences]
    return response_body


@bp.get("/<experience_id>")
def get_a_experience(experience_id):
    experience = db.session.get(Experience, experience_id)

    db.session.add(experience)
    db.session.commit()

    return make_response(experience.to_dict(), 200)

@bp.delete("/<experience_id>")
def delete_a_experience(experience_id):
    experience = validate_model(Experience, experience_id)
    
    db.session.delete(experience)
    db.session.commit()

    response_body = {"details": f'Experience {experience_id} "{experience.title}" successfully deleted.'}
    return make_response(response_body, 200)

@bp.post("")
def create_experience_to_a_country():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]
    country_id = request_body["country_id"]

    #image = if in the backend/ optional

    country = validate_model(Country, country_id)

    new_experience = Experience(title=title, description=description, country_id=country_id)
    db.session.add(new_experience)
    db.session.commit()


    response_body = new_experience.to_dict()

    return make_response(response_body, 201)



