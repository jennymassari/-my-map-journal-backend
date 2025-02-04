from flask import Blueprint, request, make_response
from app.models.experience import Experience
from app.models.country import Country
from app.routes.route_utilities import validate_model
from app.db import db
import os
from werkzeug.utils import secure_filename


bp = Blueprint("experiences_bp", __name__, url_prefix='/experiences')


@bp.get("/experiences")
def get_all_experiences():
    query = db.select(Experience)
    
    query= query.order_by(Experience.id)
    experiences = db.session.scalars(query)
    
    response_body = [experience.to_dict() for experience in experiences]
    return response_body
   


# @bp.get("/experience/<experience_id>")
@bp.get("/<experience_id>")
def get_a_experience(experience_id):
    experience = db.session.get(Experience, experience_id)
    
    if not experience:
        return make_response({"message": "Experience not found."}, 404)

    return make_response(experience.to_dict(), 200)





# @bp.patch("/experience/<experience_id>")
@bp.patch("/<experience_id>")
def update_experience(experience_id):
    experience = Experience.query.get(experience_id)

    if not experience:
        return make_response({"message": "Experience not found."}, 404)

    request_body = request.get_json()

    title = request_body.get("title", None)
    description = request_body.get("description", None)
    image = request_body.get("image", None)

    if title is not None:
        experience.title = title
    if description is not None:
        experience.description = description
    if image is not None:
        experience.image = image

    db.session.commit()

    response_body = {
        "message": "Successfully updated the experience",
        "experience": experience.to_dict()
    }

    return make_response(response_body, 200)

# @bp.delete("/experience/<experience_id>")

@bp.delete("/<experience_id>")
def delete_a_experience(experience_id):
    experience = validate_model(Experience, experience_id)
    
    db.session.delete(experience)
    db.session.commit()

    response_body = {"details": f'Experience {experience_id} "{experience.title}" successfully deleted.'}
    return make_response(response_body, 200)

    #when an experience is deleted by ID. The other ID's don't update in ascending order, for example if I delete the id 1 I am not going to have an ID 1 in next post request. I'll keep folloing the order of id's



