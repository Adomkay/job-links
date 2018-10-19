# job-links
This app aggregates civil service job vacancies from the City of New York. All data was gotten from the New York Cyity Open Data api: https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t
## TECHNOLOGIES:
1. Python
2. SQL
3. SqlAlchemy
4. Folium
5. Dash
6. Googlemap API

![alt text](https://raw.githubusercontent.com/Adomkay/job_links/master/job_app.png)

## WORKFLOW
1. I retrieved the data from the API, cleaned it and stored it as a CSV
2. Using SqlAlchemy I was able to seed all the information into my SQL database at the point of instantiation of my class objects.
3. In order to plot the locations of jobs on a map I needed coordinates and the work addresses came in string format. I passed these addresses into the google map API and generated a list of coordinates for each address
4. Using the Folium library I plotted locations of jobs on a map of New York City
5. Created my dashboard app using Plotly's Dash

## DASH
I created the dashboard for my app using Dash. This includes an interactive map of NYC showing locations of all New York civil service job vacancies. The locations displayed change based on the desired salary range selected on the salary range slider below the map. Once a location on the map is selected, a table below the slider is displayed showing all jobs available at that location and their respective job descriptions.
