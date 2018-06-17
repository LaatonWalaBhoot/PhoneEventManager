# PhoneEventManager
Phone Event Analysis

Approach:
1. For unlock_count simply get the column from the dataframe and take sum of values with dataframe == "Phone_unlock"

2. For total number of apps used, get the unique set from the event_name dataframe. Print length of the set and reduce it by 4 for 'Screen_off', 'Screen_on', 'Phone_unlock' and 'android' which is configuration changed.

3. For calculating longest time spent away from phone get the first occurence of "Screen_off" and append time differences in array between that and the next occurence of "Screen_on" or "Phone_unlock". After the iteration is complete simply print the max of the array

4. For calculating total time spent on phone do the above step with "Screen_off" replaced with "Screen_on" or "Phone_unlock" and vice versa. After the iteration is complete simply print the sum of the time_deltas

5. For printing time of each app get the unique set from event_name dataframe. Iterate over the set to look for matching values in event_name and on matching look for change in event_name and append time diffrence on change. Do this iteartion over the event_name dataframe for every app until we get a time_delta array for each app. On iteration finish print sum of the time delta array for each app.
