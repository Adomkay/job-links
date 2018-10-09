print('__enter models.py__')

from jobs import db

class Agency(db.Model):
   __tablename__ = 'agencies'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.Text)
   locations = db.relationship('Location', secondary = 'agency_locations', back_populates = 'agencies')
   buisness_titles = db.relationship('Job_Info', back_populates = 'agency')

class Job_Info(db.Model):
   __tablename__ = 'jobs_info'
   id = db.Column(db.Integer, primary_key = True)
   agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))
   location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
   name = db.Column(db.Text)  #https://docs.python.org/3/tutorial/errors.html
   min_salery = db.Column(db.Float)
   max_salery = db.Column(db.Float)
   full_time_part_time = db.Column(db.Boolean)
   preferred_skills = db.Column(db.Text)
   job_description = db.Column(db.Text)
   minimum_qual = db.Column(db.Text)
   agency = db.relationship('Agency', back_populates = 'buisness_titles')
   location = db.relationship('Location', back_populates = 'buisness_titles')

class Location(db.Model):
   __tablename__ = 'locations'
   id = db.Column(db.Integer, primary_key = True)
   long = db.Column(db.Float)
   lat = db.Column(db.Float)
   address = db.Column(db.Text)
   geocodeBool = db.Column(db.Boolean)
   agencies = db.relationship('Agency', secondary = 'agency_locations', back_populates = 'locations')
   buisness_titles = db.relationship('Job_Info', back_populates = 'location')

class Agency_location(db.Model):
   __tablename__ = 'agency_locations'
   id = db.Column(db.Integer, primary_key = True)
   agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))
   location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

db.create_all()



print('__exit models.py__')
