import pandas as pd
import requests
url = 'https://data.cityofnewyork.us/resource/swhp-yxa4.json'

response = requests.get(url)
data_with_none = response.json()

df = pd.DataFrame(data_with_none)

data_with_relevant_columns = df[['agency', 'business_title', 'salary_range_from', "salary_range_to", "work_location", "preferred_skills", "minimum_qual_requirements", "job_description", "full_time_part_time_indicator"]].copy()

complete_data = data_with_relevant_columns.dropna()

addresses = complete_data['work_location']

def clean_addresses():
    lists = []
    for index, row in addresses.iteritems():
        lists.append([index,row.lower().replace(',', '').replace('.', '')])
    return lists

def add_new_york():
    location_list = clean_addresses()
    lists2 = []
    for item in location_list:
        if not item[1].endswith(('new york', 'ny', 'n y', 'nyc')):
            item[1] = item[1] + ' new york'
        lists2.append(item)
    return lists2

formatted_work_locations = add_new_york()


location_series = pd.Series((item[1] for item in formatted_work_locations))

complete_data['work_location2'] = location_series.values

def clean_min_max_salary():
    for index, row in complete_data.iterrows():
        try:
            row['salary_range_from'] = float(row['salary_range_from'])
            row['salary_range_to'] = float(row['salary_range_to'])
        except:
            pass
    mask_to = complete_data['salary_range_to'] == 'F'
    mask_from = complete_data['salary_range_from'] == 'F'
    mask_to_0 = complete_data['salary_range_to'] == 0
    mask_from_0 = complete_data['salary_range_from'] == 0
    f_data_to = complete_data[mask_to]
    f_data_from = complete_data[mask_from]
    f_data_to_0 = complete_data[mask_to_0]
    f_data_from_0 = complete_data[mask_from_0]
    temp = complete_data.drop(f_data_to.index)
    temp2 = temp.drop(f_data_from.index)
    temp3 = temp2.drop(f_data_to_0.index)
    temp4 = temp3.drop(f_data_from_0.index)
    return temp4

complete_data2 = clean_min_max_salary()

def full_time_to_bool():
    for index, row in complete_data2.iterrows():
        if row['full_time_part_time_indicator'] == 'F':
            row['full_time_part_time_indicator'] = 1
        else:
            row['full_time_part_time_indicator'] = 0

full_time_to_bool()
