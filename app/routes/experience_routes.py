from flask import Blueprint, abort, make_response, request
from app.models.experience import Experience
from app.db import db
from app.routes.route_utilities import validate_model
import os

bp = Blueprint("experience_bp", __name__, url_prefix="/experiences")

# C - user can post an experience adding a title, a description and an image
# R - user can read all the experiences for the country selected
# U - user can update the title, description and image
# D - user can delete the whole experience or delete only the picture(optional)

@bp.get("")
def get_all_experiences():
    query = db.select(Experience)
    
    query= query.order_by(Experience.id)
    cards = db.session.scalars(query)
    
    response_body = [experience.to_dict() for experience in experiences]
    return response_body

@bp.get("/<experience_id>")
def get_a_experience(experience_id):
    experience = db.session.get(Experience, experience_id)

    db.session.add(experience)
    db.session.commit()

@bp.post("")
def create_experience():
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]
    #image = if in the backend/ optional

    new_experience = Experience(title=title, description=description)
    db.session.add(new_experience)
    db.session.commit()

    response_body = new_experience.to_dict()

    return response_body,201

@bp.delete("/<experience_id>")
def delete_a_experience(experience_id):
    experience = validate_model(Experience, experience_id)
    
    response_body = {"details": f'Experience {experience_id} "{experience.title}" successfully deleted.'}
    return make_response(response_body, 200)