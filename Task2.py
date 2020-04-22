"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
import json

# build dictionary or a map of key as calls and value as duration
phone_dict = defaultdict(list)

def phone_call_duration(calls):
    
    for call in calls:
        phone1, phone2 = call[0], call[1]
        duration = call[3]
        
        if phone_dict.keys() == phone1:
            phone_dict[phone1] = [duration]
        else:
            phone_dict[phone1].append(duration)

        if phone_dict.keys() == phone2:
            phone_dict[phone2] = [duration]
        else:
            phone_dict[phone2].append(duration)
            
    # print(json.dumps(phone_dict, indent=1))

phone_call_duration(calls)


# build another dictionary for total sum of value duration for each key           
phone_duration = {}
for key, value in phone_dict.items():
    phone_duration[key] = sum(map(int, value))

# get max value of values in new duration dictionary and print out key and value
max_time = max(phone_duration, key=phone_duration.get)  
print(max_time, 'spent the longest time,', phone_duration[max_time], 'seconds, on the phone during September 2016.')