import pandas as pd
import json
import requests


url = "https://data.ny.gov/api/views/j6d2-s8m2/rows.json?accessType=DOWNLOAD"

response = requests.get(url)
incidents = response.json()
with open("url", mode="w") as file:
    json.dump(incidents, file, indent=4)


incident_data = incidents.get('data', [])
df = pd.DataFrame(incident_data)

df.to_csv("incidents.csv", index=False)
