import pandas as pd

#Load csv
dr_riders = pd.read_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership.csv")
#drop unwanted columns
dr_riders.drop(["subways_of_comparable_pre_pandemic_day","buses_total_estimated_ridersip","buses_of_comparable_pre_pandemic_day","lirr_total_estimated_ridership","lirr_of_comparable_pre_pandemic_day","metro_north_total_estimated_ridership","metro_north_of_comparable_pre_pandemic_day","access_a_ride_total_scheduled_trips","access_a_ride_of_comparable_pre_pandemic_day","bridges_and_tunnels_total_traffic","bridges_and_tunnels_of_comparable_pre_pandemic_day","staten_island_railway_total_estimated_ridership","staten_island_railway_of_comparable_pre_pandemic_day"], axis=1, inplace=True)

#create a csv file called daily ridership clean
dr_riders.to_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership_clean.csv", index=False)

print("CSV created")