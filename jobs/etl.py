print('enter ETL')
from models import Agency, Job_Info, Location, Agency_location
from jobs import db
from jobs_data import complete_data2
import pandas as pd
import geocoder
import time

def construct_Agency():
   agency_list =  [Agency(name = u_agency) for u_agency in list(set([row['agency'] for index, row in complete_data2.iterrows()]))]
   db.session.add_all(agency_list)
   db.session.commit()


def construct_Location():
    location_dict = {}
    u_locations =list(set([row['work_location2'] for index, row in complete_data2.iterrows()]))
    for u_location in u_locations:
        geo = geocoder.google(u_location).latlng
        if not type(geo) == type(geocoder.google('').latlng):
            location_dict[u_location] = Location(address = u_location, lat = geo[0], long = geo[1], geocodeBool = 1)
        else:
            location_dict[u_location] = Location(address = u_location, geocodeBool = 0)
        time.sleep(2)
    db.session.add_all([location_dict[key] for key in location_dict.keys()])
    db.session.commit()

def construct_Job_Info():
    construct_Agency()
    construct_Location()
    for index, row in complete_data2.iterrows():
        temp_job_info = Job_Info(name = row['business_title'],
        min_salery = row['salary_range_from'],
        max_salery = row['salary_range_to'],
        full_time_part_time = row['full_time_part_time_indicator'],
        preferred_skills = row['preferred_skills'],
        job_description = row['job_description'],
        minimum_qual = row['minimum_qual_requirements'],
        agency = db.session.query(Agency).filter_by(name = row['agency']).all()[0],
        location = db.session.query(Location).filter_by(address = row['work_location2']).all()[0])
        # jobs_info_objs.append(temp_job_info)
        # temp_job_info.location.agencies.append(temp_job_info.agency)
        temp_job_loc = temp_job_info.location
        temp_job_age = temp_job_info.agency
        if temp_job_age not in temp_job_loc.agencies:
            temp_job_loc.agencies.append(temp_job_age)
            db.session.add(temp_job_info)
        print(index)
    import pdb; pdb.set_trace()
    db.session.commit()

print('exit ETL')
