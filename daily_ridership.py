import pandas as pd
import json
import requests
import datetime as dt

#Store URL in variable
url = "https://data.ny.gov/resource/vxuj-8kew.json"

#Store URL in variable for data from 2022 - 2024
url2 = "https://data.ny.gov/resource/vxuj-8kew.json?$offset=1000&$limit=1000"

#Make HTTP request to the data.ny.gov API Endpoint
page = requests.get(url)

page2 = requests.get(url2)

#Parse JSON data
ridership_data = page.json()

ridership_d2024 = page2.json()

#Create DataFrame from site data
df = pd.DataFrame(ridership_data)

df1 = pd.DataFrame(ridership_d2024)

#Create CSV file from DataFrame
df.to_csv("daily_ridership.csv", index=False)

df1.to_csv("daily_rider2024.csv", index=False)


#Load csv
dr_riders = pd.read_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership.csv")

#drop unwanted columns
dr_riders.drop(["subways_of_comparable_pre_pandemic_day","buses_total_estimated_ridersip","buses_of_comparable_pre_pandemic_day","lirr_total_estimated_ridership","lirr_of_comparable_pre_pandemic_day","metro_north_total_estimated_ridership","metro_north_of_comparable_pre_pandemic_day","access_a_ride_total_scheduled_trips","access_a_ride_of_comparable_pre_pandemic_day","bridges_and_tunnels_total_traffic","bridges_and_tunnels_of_comparable_pre_pandemic_day","staten_island_railway_total_estimated_ridership","staten_island_railway_of_comparable_pre_pandemic_day"], axis=1, inplace=True)

dr_riders["date"] = pd.to_datetime(dr_riders["date"], errors="coerce")

dr_riders["date"] = dr_riders["date"].dt.date

#create a csv file called daily ridership clean
dr_riders.to_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership_clean.csv", index=False)