"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


suspected_telemarketer_list = set()
for call in calls:
	suspected_telemarketer_list.add(call[0])

#Remove incoming
for call in calls:
	if call[1] in suspected_telemarketer_list:
		suspected_telemarketer_list.remove(call[1])

for text in texts:
	if text[0] in suspected_telemarketer_list:
		suspected_telemarketer_list.remove(text[0])
	if text[1] in suspected_telemarketer_list:
		suspected_telemarketer_list.remove(text[1])

#Sort 
telemarketer_list = list(suspected_telemarketer_list)
telemarketer_list.sort()
print("These numbers could be telemarketers: ")
for telemekarter in telemarketer_list:
	print(telemekarter)
