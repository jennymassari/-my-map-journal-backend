from app import create_app, db
from app.models.country import Country  

my_app = create_app()

with my_app.app_context():

    db.session.add(Country(
        name="Canada", 
        lat=56, 
        long=-106, 
        visited=True, 
        borned=False, 
        want_to_visit=False
    ))
    db.session.add(Country(
        name="Japan", 
        lat=36, 
        long=138, 
        visited=False, 
        borned=False, 
        want_to_visit=True
    ))
    db.session.add(Country(
        name="Australia", 
        lat=-25, 
        long=133, 
        visited=True, 
        borned=False, 
        want_to_visit=False
    ))
    db.session.add(Country(
        name="Brazil", 
        lat=-14, 
        long=-51, 
        visited=False, 
        borned=True, 
        want_to_visit=False
    ))
    db.session.add(Country(
        name="Germany", 
        lat=51, 
        long=9, 
        visited=False, 
        borned=False, 
        want_to_visit=True
    ))

    db.session.commit()

    print("Countries have been successfully added!")
