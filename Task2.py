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

phone_calls = {}
for call in calls:
	#Adds total time to sending and receiving phones
	if call[0]  in phone_calls:
		phone_calls[call[0]] += int(call[3])
	else:
		phone_calls[call[0]] = int(call[3])
	if call[1]  in phone_calls:
		phone_calls[call[1]] += int(call[3])
	else:
		phone_calls[call[1]] = int(call[3])

max_phone_number = ''
max_total_time = 0
for phone in phone_calls:
	if phone_calls[phone] >= max_total_time:
		max_phone_number = phone
		max_total_time = phone_calls[phone]
print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(
		telephone_number = max_phone_number,
		total_time = max_total_time
	)
)