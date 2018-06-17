import pandas as pd
import datetime as dt
from dateutil.parser import parse


#Reading CSV
df = pd.read_csv('Aishwarya - Problem Data - Sheet1.csv')

#Counting Number of Phone Unlocks
unlock_count = df.event_name
print("Total number of times phone was unlocked: ",sum(unlock_count == "Phone_unlock"))

#Counting number of Apps Used
app_count = df.event_name
print("Total number of apps used: ", len(set(app_count))-4)

#Calculating longest time spent away from phone
time_away = []
i = df.event_name.size - 1
while i > 0:
    if (df.event_name.iloc[i] == "Screen_off"):
        for j in range(i - 1, -1, -1):
            if (df.event_name.iloc[j] == "Screen_on" or df.event_name.iloc[j] == "Phone_unlock"):
                time_away.append(parse(df.timestamp.iloc[j]) - parse(df.timestamp.iloc[i]))
                i = j - 1
                break
    else:
        i = i - 1
print("Longest time spent away from phone: ",max(time_away))

#Calculating total time spent on phone
time_on = []
i = df.event_name.size - 1
while i > 0:
    if (df.event_name.iloc[i] == "Screen_on" or df.event_name.iloc[i] == "Phone_unlock"):
        for j in range(i - 1, -1, -1):
            if (df.event_name.iloc[j] == "Screen_off"):
                time_on.append(parse(df.timestamp.iloc[j]) - parse(df.timestamp.iloc[i]))
                i = j - 1
                break
    else:
        i = i - 1
print("Longest time spent on phone: ",max(time_on))
print("Total time spent on phone: ",sum(time_on, dt.timedelta()))

#Calculating time for each app
apps = set(df.event_name)
count = 0
print(len(apps))
for app in apps:
    time = []
    for i in range(df.event_name.size-1,-1,-1):
        if(df.event_name.iloc[i] == app):
            if(count==0):
                count = 1
                start_time = df.timestamp.iloc[i]
        else:
            if(count==1):
                count = 0
                end_time = df.timestamp.iloc[i]
                time.append(parse(end_time) - parse(start_time))

    if(count == 1):
        count = 0
    print("Total time spent on ",app," - ",sum(time,dt.timedelta()))
