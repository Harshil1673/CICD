import pandas as pd

attendance = pd.read_csv("attendance.csv")
print(pd.crosstab(attendance["name"], attendance["status"]).to_string())
