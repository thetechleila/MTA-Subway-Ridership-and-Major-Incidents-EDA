import pandas as pd
import json
import requests
import datetime as dt

url = "https://data.ny.gov/api/views/j6d2-s8m2/rows.json?accessType=DOWNLOAD"

response = requests.get(url)
incidents = response.json()
with open("url", mode="w") as file:
    json.dump(incidents, file, indent=4)


incident_data = incidents.get('data', [])
df = pd.DataFrame(incident_data)

df.to_csv("incidents.csv", index=False)

# Load the CSV 
df_raw = pd.read_csv("incidents.csv", header=None)

# Print first 15 rows to inspect structure
print(df_raw.head(15))

# Assign column names manually, ensuring Row 8 is named "Date_Occurred"
df_raw.columns = ["col_" + str(i) for i in range(len(df_raw.columns))] 

# Rename the specific column
df_raw.rename(columns={"col_8": "date", "col_12": "incident_type", "col_13": "incident_count", "col_11": "wday_wnd","col_9": "division","col_10": "train_line"} , inplace=True)

columns_to_drop = ["col_0", "col_1","col_2","col_3","col_4","col_5","col_6","col_7"]  
df_raw.drop(columns=columns_to_drop, inplace=True)

df_raw['date'] = pd.to_datetime(df_raw['date'], errors="coerce")
df_raw['date'] = df_raw['date'].dt.date

# Display column names to confirm
print(df_raw.columns)

# Save the cleaned CSV
df_raw.to_csv("incidents.csv", index=False)

print(df_raw.columns)
df_raw.head()
