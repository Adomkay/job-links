import folium
import pandas as pd
from jobs.routes import *
from jobs import db

NY_COORDINATES = (40.7128, -74.0060)

job_locations = lat_long_trace()


# create empty map zoomed in on New York
ny_map = folium.Map(location=NY_COORDINATES,tiles = 'Stamen Toner', zoom_start=12)

def map_job_locations():
    for item in job_locations:
        popup = folium.Popup(agencies_per_location([item['lat'], item['lng']]), parse_html=True)
        marker = folium.Marker(location = [item['lat'], item['lng']], popup = popup)
        marker.add_to(ny_map)
    return ny_map

location_map = map_job_locations()

location_map.save('NYC_Jobs_Locations.html')


# add a marker for every record in the filtered data, use a clustered view
# for item in job_locations:
#     map.simple_marker(location = [item['lat'], item['lng'])
#
# map.create_map(path='ny_map.html')
# display(map)
