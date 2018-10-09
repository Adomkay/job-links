import dash
from jobs import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from jobs.routes import *
from dashboard_views.nyc_map import *
import plotly.graph_objs as go
import folium
import dash_table_experiments as dt

app.layout = html.Div([
   html.H1('New York City Civil Service Job Openings'),
   html.Iframe(id = 'map', srcDoc = open('NYC_Jobs_Locations.html, 'r', errors = 'ignore').read(), width ='100%', height= '600'),
   html.H2('Filter job openings by desired salary'),
   dcc.RangeSlider(id = 'salary_slider', marks={int(min_salary() + n*10000):'$'+str(min_salary() + n*10000) for n in range(0,23)}, min = min_salary(), max = max_salary(), value = [min_salary(), max_salary()]),
   html.H1(' '),
   html.H1(' '),
   html.H1(' '),
   html.H1(' '),
   html.H2('Filter Histograms by desired agency'),
   dcc.Dropdown(id = 'Agencies_dropdown', value = 'agency', options = [{'label': i, 'value': i} for i in agency_name()]),
   dt.DataTable(id='table',
        rows=[{}],
        row_selectable=False,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        ),
   html.H3('Job Description Histogram'),
   dcc.Graph(id = 'histogram_desc'),
   html.H3('Job Preferred Histogram'),
   dcc.Graph(id = 'histogram_prefer'),
   html.H3('Job Minimum Qualifications'),
   dcc.Graph(id = 'histogram_qual')
])

@app.callback(
    dash.dependencies.Output('histogram_desc', 'figure'),
    [dash.dependencies.Input('Agencies_dropdown', 'value')])
def plot_desc(value):
    figure = go.Figure(data = [go.Bar(x = job_word_frequencies(job_descriptions(value))['x'],
                                      y = job_word_frequencies(job_descriptions(value))['y'])])
    return figure
@app.callback(
    dash.dependencies.Output('histogram_qual', 'figure'),
    [dash.dependencies.Input('Agencies_dropdown', 'value')])
def plot_desc(value):
    figure = go.Figure(data = [go.Bar(x = job_word_frequencies(job_minimum_qual(value))['x'],
                                      y = job_word_frequencies(job_minimum_qual(value))['y'])])
    return figure
@app.callback(
    dash.dependencies.Output('histogram_prefer', 'figure'),
    [dash.dependencies.Input('Agencies_dropdown', 'value')])
def plot_desc(value):
    figure = go.Figure(data = [go.Bar(x = job_word_frequencies(job_preferred_skills(value))['x'],
                                      y = job_word_frequencies(job_preferred_skills(value))['y'])])
    return figure
# @app.callback(
#     dash.dependencies.Output('map', 'srcDoc'),
#     [dash.dependencies.Input('salary_slider', 'value')])
# def nyc_map(value):
#     NY_COORDINATES = (40.7128, -74.0060)
#     job_locations =  job_location(value[0], value[1])
#     ny_map = folium.Map(location=NY_COORDINATES, zoom_start=12)
#     def map_job_locations():
#        for item in job_locations:
#            print('making_markers')
#            popup = folium.Popup(agencies_per_location([item[1].lat, item[1].long]), parse_html=True)
#            marker = folium.Marker(location = [item[1].lat, item[1].long], popup = popup)
#            marker.add_to(ny_map)
#        return ny_map
#     location_map = map_job_locations()
#     print('saving map')
#     location_map.save('NYC_Jobs_Locations.html')
#     return open('NYC_Jobs_Locations.html', 'r').read()

@app.callback(
    dash.dependencies.Output('table', 'rows'),
    [dash.dependencies.Input('Agencies_dropdown', 'value'),
    dash.dependencies.Input('salary_slider', 'value')])
def make_table(value, value_1):
    return [{'Business Title':  job.name, 'full time/ Part time': job_bool(job), 'Location': job.location.address, 'Job Description': job.job_description} for job in job(value) if (value_1[0] < job.min_salery < value_1[1])]
