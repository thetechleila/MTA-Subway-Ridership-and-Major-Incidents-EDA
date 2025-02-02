import pandas as pd

df1 = pd.read_csv("daily_ridership.csv")
df2 = pd.read_csv("incidents.csv")

merge_df = pd.merge(df1,df2, left_index=True, right_index=True)

merge_df.to_csv("merged_file.csv", index=False)