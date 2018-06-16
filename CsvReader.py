import pandas as pd
import numpy as np

#Reading CSV
df = pd.read_csv('Aishwarya - Problem Data - Sheet1.csv')

#Counting Number of Phone Unlocks
unlock_count = df.event_name
print(np.sum(unlock_count == "Phone_unlock"))

#Counting number of Apps Used
app_count = df.event_name
print(len(set(app_count))-4)

#Calculating time spent away from phone
