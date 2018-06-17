import pandas as pd
import numpy as np
from dateutil.parser import parse
#Reading CSV
df = pd.read_csv('Aishwarya - Problem Data - Sheet1.csv')

#Counting Number of Phone Unlocks
unlock_count = df.event_name
print("Total number of times phone was unlocked: ",np.sum(unlock_count == "Phone_unlock"))

#Counting number of Apps Used
app_count = df.event_name
print("Total number of apps used: ", len(set(app_count))-4)
