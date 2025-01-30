import pandas as pd
import json
import requests

#Store URL in variable
url = "https://data.ny.gov/resource/vxuj-8kew.json"

#Make HTTP request to the data.ny.gov API Endpoint
page = requests.get(url)

#Parse JSON data
ridership_data = page.json()

#Create DataFrame from site data
df = pd.DataFrame(ridership_data)

#Create CSV file from DataFrame
df.to_csv("daily_ridership_5yrs.csv", index=False)