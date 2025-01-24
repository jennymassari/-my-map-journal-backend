# My Map Journal

1. Interactive Map Feature
•	Description: Users can interact with a world map, where countries can be highlighted or marked based on whether the user has visited them.
•	Details: Users click on a country to indicate that they’ve visited it, and they can add their personal experience (text and an optional image) for each country.
2. Add and View Personal Experiences
•	Description: Users can submit and view their experiences associated with each country.
•	Details: After selecting a country, users can write a short description of their visit, upload an image, and save it. Each country visited will have a record of the user's experience visible on the map.
3. User Authentication (Signup/Login)
•	Description: Users must sign up or log in to save and manage their experiences.
•	Details: A user profile will allow them to add experiences to countries, view their travel history, and edit/delete experiences as needed.
4. Display User’s Travel Map
•	Description: Once logged in, users can view a map displaying the countries they’ve visited, with markers indicating where they’ve left an experience.
•	Details: The map will show each country with a different visual cue (e.g., colored countries or a pin marking the country) for each experience added.

### Potential Additional Features

1.	Social Features
o	Description: Users can share their travel experiences with others, see what countries their friends have visited, and even leave comments on others' experiences.
2.	Statistics and Progress Tracker
o	Description: A progress tracker showing how many countries a user has visited. This could include a percentage or a visual graph of how many countries they’ve visited compared to the total number of countries in the world.
3.	Search and Filter Options
o	Description: Users can search for countries or filter experiences by date, location, or type of experience (e.g., adventure, food, culture).


## Draft Technology Choices

•	Backend:
o	Flask – A lightweight Python web framework to serve the RESTful API and handle the business logic.
o	PostgreSQL – To store user data, travel experiences, and country records.
o	Flask-SQLAlchemy – For ORM and database management in Flask.

•	Frontend:
o	React – For building the interactive user interface.
o	Axios – To make HTTP requests to the backend API for data fetching and submitting experiences.
o	Leaflet – For creating and displaying the interactive world map.
o OpenStreetMap - To provide map tiles for rendering the world map.
o GeoJSON - To get Geographical Coordinates and Country Data.

•	Authentication:
o	JWT (JSON Web Tokens) – For handling secure user authentication and session management.

•	Deployment:
o	Heroku 

## Database Structure & Relationships

The database for this project will store information about users, the countries they’ve visited, and their experiences in a relational manner. 

1.	Users Table:
o	Each user has many experiences.
o	Foreign key: id from Users is used in Experiences to associate experiences with users.

2.	Countries Table:
o	Each country can have many experiences.
o	Foreign key: id from Countries is used in Experiences to associate experiences with countries.

3.	Experiences Table:
o	Each experience is linked to one user and one country.
o	Foreign keys: user_id links to Users.id, and country_id links to Countries.id.

Relationships Between Tables

1.	User ↔ Experiences (One-to-Many Relationship):
o	A user can have many experiences, but each experience belongs to one specific user. This is represented by the user_id foreign key in the Experiences table, referencing the id in the Users table.

2.	Country ↔ Experiences (One-to-Many Relationship):
o	A country can have many experiences associated with it, but each experience is linked to one country. This is represented by the country_id foreign key in the Experiences table, referencing the id in the Countries table.

3.	User ↔ Country (Many-to-Many Relationship via Experiences):
o	A user can visit many countries, and each country can have many users visiting it. This relationship is represented by the Experiences table, which acts as a junction table between users and countries. Each experience links one user to one country, and each country can have many users associated with it through experiences.
