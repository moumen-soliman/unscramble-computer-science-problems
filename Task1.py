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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def add_only_unique_numbers(previous, phones):
	for phone in phones:
		previous.add(phone[0])
		previous.add(phone[1])
	return previous

unique_phones = set()
unique_phones = add_only_unique_numbers(unique_phones, texts)
unique_phones = add_only_unique_numbers(unique_phones, calls)

print("There are {count} different telephone numbers in the records.".format(count = len(unique_phones)))