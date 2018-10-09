
from jobs.models import Job_Info, Agency, Location, Agency_location
from jobs import db
import nltk, re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#from flask_sqlalchemy import func

##Agency Queries
def agency_name(): #<A>
    return [agency.name for agency in db.session.query(Agency)]
def agency_Locations(filter_query = db.session.query(Agency).all()): #(<A>, [<l>, <l>])
    return [(agency, agency.locations) for agency in db.session.query(Agency) if agency in filter_query]
def agency_Jobs(filter_query = db.session.query(Agency).all()): #(<A>, [<j>, <j>])
    return [(agency, agency.buisness_titles) for agency in db.session.query(Agency) if agency in filter_query]

##Job Queries
def job(name): # <j>
    return [job for job in db.session.query(Job_Info) if job.agency.name == name]
def job_bool(job):
    if job.full_time_part_time == 1:
        return 'Full time'
    else:
        return 'Part time'

def job_names():
    return [job.name for job in db.session.query(Job_Info).all()]
def job_location(value0, value1): #(<j>, <l>)
    return [(job, job.location) for job in db.session.query(Job_Info) if ((value0 <= job.min_salery <= value1)) and (job.location.lat != None)]
def specitic_job_location(name):
    lists = job_location(filter_query = db.session.query(Job_Info).all())
    for item in lists:
        if item[0].name == name:
            return item[1].address
def job_location_salery(filter_query = db.session.query(Job_Info).all()): #(<j>, <l>, float, float)
    return [(job, job.location, job.min_salery, job.max_salery) for job in db.session.query(Job_Info) if job in filter_query]

def min_max_salary():
    job_salary = job_location_salery(filter_query = db.session.query(Job_Info).all())
    min_salary = min([salary[2] for salary in job_salary])
    max_salary = max([salary[3] for salary in job_salary])
    return [min_salary, max_salary]

def jobs_agency(filter_query = db.session.query(Job_Info).all()): #(<j>, <A>)
    return [(job, job.agency) for job in db.session.query(Job_Info) if job in filter_query]
def specific_jobs_agency(name):
    lists = jobs_agency(filter_query = db.session.query(Job_Info).all())
    for item in lists:
        if item[0].name == name:
            return item[1].name

def job_info_with_locations(filter_query = db.session.query(Job_Info).all()): #(<j>, <A>, <l>)
    return [(job, job.agency, job.location) for job in db.session.query(Job_Info) if job in filter_query]
def job_descriptions(name): #(<j>, <A>, str)
   return [(job, job.agency, job.job_description)for job in db.session.query(Job_Info) if job.agency.name == name]
def specitic_job_description(name):
    lists = job_descriptions(filter_query = db.session.query(Job_Info).all())
    for item in lists:
        if item[0].name == name:
            return item[2]
def job_preferred_skills(name): #(<j>, <A>, str)
   return [(job, job.agency, job.preferred_skills) for job in db.session.query(Job_Info) if job.agency.name == name]
def specitic_job_preferred_skills(name):
    lists = job_preferred_skills(filter_query = db.session.query(Job_Info).all())
    for item in lists:
        if item[0].name == name:
            return item[2]
def job_minimum_qual(name): #(<j>, <A>, str)
   return [(job, job.agency, job.minimum_qual) for job in db.session.query(Job_Info) if job.agency.name == name]
def job_min_max_salary(filter_query = db.session.query(Job_Info).all()): #(<j>, <A>, float, float, Bool)
    return [(job, job.agency, job.min_salery, job.max_salery, job.full_time_part_time)for job in db.session.query(Job_Info) if job in filter_query]

def min_salary():
    return min([job.min_salery for job in db.session.query(Job_Info) if job.min_salery != 0])

def max_salary():
    return max([job.max_salery for job in db.session.query(Job_Info) if job.max_salery != 0])

##Location Queries
def locations(filter_query = db.session.query(Location).all()): # <l>
    return [loc for loc in db.session.query(Location) if loc in filter_query]
def loc_names():
    return [loc.address for loc in db.session.query(Location).all()]
def loc_lat_long(filter_query = db.session.query(Location).all()): #(<l>, float, float)
    return [(loc, loc.lat, loc.long) for loc in db.session.query(Location) if loc in filter_query]
def loc_Agencies(filter_query = db.session.query(Location).all()): #(<l>, [<A>,<A>])
    return [(loc, loc.agencies) for loc in db.session.query(Location) if loc in filter_query]
def agencies_per_location(location):
    lists = loc_Agencies(filter_query = db.session.query(Location).all()) #(<l>, [<A>,<A>])
    for item in lists:
        if item[0].lat == location[0] and item[0].long == location[1]:
            agency_objects = item[1]
            agency_names = [agency.name for agency in agency_objects]
            return_string = ''
            for item in range(0, len(agency_names)):
                if item < len(agency_names):
                    return_string += agency_names[item] + ', '
                else:
                    return_string += agency_names[item]
            return return_string
def specific_loc_agencies(address):
    lists = loc_Agencies(filter_query = db.session.query(Location).all())
    for item in lists:
        if item[0].address == address:
            return item[1].name
def loc_Jobs(filter_query = db.session.query(Location).all()): #(<l>, [<j>, <j>])
    return [(loc, loc.jobs) for loc in db.session.query(Location) if loc in filter_query]

##Traces
def lat_long_trace():
    return [{'lat': location.lat, 'lng': location.long, 'type': 'scattermapbox'} for location in db.session.query(Location).all() if location.lat != None]
def lat_long_trace_2():
    return [{'lat':[_tuple[1] for _tuple in loc_lat_long() if _tuple[1] != None],'lng':[_tuple[2] for _tuple in loc_lat_long() if _tuple[2] != None],'type': 'scattermapbox'}]
#Word Frequencies
def job_word_frequencies(query_function):
   word_freq = {}
   stopwords_ = list(set(stopwords.words('english')))
   for _tuple in query_function:
       tokenizer = RegexpTokenizer(r'\w+')
       words_2 = tokenizer.tokenize(_tuple[2])
       words = [word for word in words_2 if word.lower() not in stopwords_ + ['â']]
       for word in words:
           word = word.replace('.', '').replace(':', '').replace(' ', '').replace('*', '').replace(')', '').replace(',','').replace('\t','').replace(';','').replace('-','')
           if word.upper() in word_freq.keys():
               word_freq[word.upper()] += 1
           else:
               word_freq[word.upper()] = 1
   trace = {'x':[key for key in word_freq.keys()],'y':[word_freq[key] for key in word_freq.keys()],'type':'bar'}
   return trace
