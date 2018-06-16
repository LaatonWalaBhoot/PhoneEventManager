import pandas as pd
import numpy as np

#Counting Number of Phone Unlocks
df = pd.read_csv('Aishwarya - Problem Data - Sheet1.csv')
df = df.event_name
print(np.sum(df == "Phone_unlock"))