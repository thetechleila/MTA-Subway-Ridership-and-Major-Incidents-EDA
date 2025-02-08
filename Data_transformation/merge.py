import pandas as pd
#open and read csv files
df1 = pd.read_csv("combined_df.csv")
df2 = pd.read_csv("incidents.csv")
#merge them together
merged_df = df1.merge(df2, on="date", how="inner")
merged_df.to_csv("merged_file.csv", index=False)