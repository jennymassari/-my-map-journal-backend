from app import create_app, db
from app.models.experience import Experience  
from app.models.country import Country 

my_app = create_app()

with my_app.app_context():

    canada = Country.query.filter_by(name="Canada").first()
    japan = Country.query.filter_by(name="Japan").first()
    australia = Country.query.filter_by(name="Australia").first()
    brazil = Country.query.filter_by(name="Brazil").first()
    germany = Country.query.filter_by(name="Germany").first()

    db.session.add(Experience(
        title="Hiking in the Rockies", 
        description="A beautiful trek through the Canadian Rockies.", 
        country_id=canada.id
    ))
    db.session.add(Experience(
        title="Tokyo City Tour", 
        description="Exploring the vibrant city of Tokyo.", 
        country_id=japan.id
    ))
    db.session.add(Experience(
        title="Great Barrier Reef Diving", 
        description="An unforgettable diving experience in the Great Barrier Reef.", 
        country_id=australia.id
    ))
    db.session.add(Experience(
        title="Amazon Rainforest Adventure", 
        description="Exploring the wilds of the Amazon Rainforest in Brazil.", 
        country_id=brazil.id
    ))
    db.session.add(Experience(
        title="Berlin Wall History Tour", 
        description="Learning about the history of the Berlin Wall.", 
        country_id=germany.id
    ))

    db.session.commit()

    print("Experiences have been successfully added!")
