from flask import Blueprint, request, make_response
from app.models.experience import Experience
from app.models.country import Country
from app.routes.route_utilities import validate_model
from app.db import db
import os
from werkzeug.utils import secure_filename

# Define the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size (16MB)

bp = Blueprint("experience_bp", __name__, url_prefix="/country")

# Helper function to check if the file type is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    
    if not experience:
        return make_response({"message": "Experience not found."}, 404)

    return make_response(experience.to_dict(), 200)

@bp.get("/<country_id>/experience")
def get_experiences_for_country(country_id):
    country = validate_model(Country, country_id)

    experiences = db.session.query(Experience).filter_by(country_id=country.id).order_by(Experience.id).all()

    response_body = {
        "country": {
            "id": country.id,
            "name": country.name
        },
        "experiences": [experience.to_dict() for experience in experiences]
    }

    return make_response(response_body, 200) 

@bp.post("/<country_id>/experience")
def create_experience_to_a_country(country_id):
    request_body = request.get_json()

    title = request_body.get("title")
    description = request_body.get("description")
    country_id = request_body.get("country_id")

    country = validate_model(Country, country_id)

    # Check if an image file was included in the request
    image = request.files.get('image')

    # If an image is provided, save it
    if image and allowed_file(image.filename):
        # Ensure the file is safe to save (e.g., no path traversal attacks)
        filename = secure_filename(image.filename)
        
        image.save(os.path.join(UPLOAD_FOLDER, filename))

        image_path = os.path.join(UPLOAD_FOLDER, filename)  

    else:
        image_path = None  

    new_experience = Experience(
        title=title,
        description=description,
        country_id=country_id,
        image=image_path 
    )

    db.session.add(new_experience)
    db.session.commit()

    response_body = new_experience.to_dict()
    return make_response(response_body, 201)

@bp.patch("/<experience_id>")
def update_experience(experience_id):
    experience = Experience.query.get(experience_id)

    if not experience:
        return make_response({"message": "Experience not found."}, 404)

    request_body = request.get_json()

    borned = request_body.get("borned", None)
    visited = request_body.get("visited", None)
    want_to_visit = request_body.get("want_to_visit", None)

    if borned:
        experience.borned = True
        experience.visited = False  
        experience.want_to_visit = False  
    elif visited:
        experience.visited = True
        experience.borned = False  
        experience.want_to_visit = False  
    elif want_to_visit:
        experience.want_to_visit = True
        experience.borned = False  
        experience.visited = False  
    else:
        return make_response({"message": "No valid option selected."}, 400)

    db.session.commit()

    response_body = {
        "message": "Successfully updated the experience",
        "experience": experience.to_dict()
    }

    return make_response(response_body, 200)

@bp.delete("/<experience_id>")
def delete_a_experience(experience_id):
    experience = validate_model(Experience, experience_id)
    
    db.session.delete(experience)
    db.session.commit()

    response_body = {"details": f'Experience {experience_id} "{experience.title}" successfully deleted.'}
    return make_response(response_body, 200)


