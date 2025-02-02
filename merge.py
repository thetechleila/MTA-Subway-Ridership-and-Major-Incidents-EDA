import pandas as pd

df1 = pd.read_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/daily_ridership.csv")
df2 = pd.read_csv("/Users/sa24/Downloads/Portfolio-Project-main/Portfolio-Project/incidents.csv")

merged_df = df1.merge(df2, on="date", how="inner")
merged_df.to_csv("merged_file.csv", index=False)