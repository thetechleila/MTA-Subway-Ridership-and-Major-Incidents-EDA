import pandas as pd
import json
import requests
import datetime as dt

#Store URL in variable
url = "https://data.ny.gov/resource/vxuj-8kew.json"

#Make HTTP request to the data.ny.gov API Endpoint
page = requests.get(url)

#Parse JSON data
ridership_data = page.json()

#Create DataFrame from site data
df = pd.DataFrame(ridership_data)

#Create CSV file from DataFrame
df.to_csv("daily_ridership.csv", index=False)

#Load csv
dr_riders = pd.read_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership.csv")
#drop unwanted columns
dr_riders.drop(["subways_of_comparable_pre_pandemic_day","buses_total_estimated_ridersip","buses_of_comparable_pre_pandemic_day","lirr_total_estimated_ridership","lirr_of_comparable_pre_pandemic_day","metro_north_total_estimated_ridership","metro_north_of_comparable_pre_pandemic_day","access_a_ride_total_scheduled_trips","access_a_ride_of_comparable_pre_pandemic_day","bridges_and_tunnels_total_traffic","bridges_and_tunnels_of_comparable_pre_pandemic_day","staten_island_railway_total_estimated_ridership","staten_island_railway_of_comparable_pre_pandemic_day"], axis=1, inplace=True)

dr_riders["date"] = pd.to_datetime(dr_riders["date"], errors="coerce")

dr_riders["date"] = dr_riders["date"].dt.date

#create a csv file called daily ridership clean
dr_riders.to_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership_clean.csv", index=False)