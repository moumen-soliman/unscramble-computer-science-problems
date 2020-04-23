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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def is_bangalore_fixed_phone(phone):
	return phone[0:5] == '(080)'

def get_phone_prefix(phone):
	#Landline case
	if phone[0:2] == "(0": #Landline always starts with (0
		closing_bracket_position = phone.index(")") + 1
		return phone[0:closing_bracket_position] #Sometimes code is bigger

	#Telemarketer
	if phone[0:3] == "140":
		return phone[0:3] #Always 140

	#All other cases are mobile phones
	if phone.index(" ") != -1:
		return phone[0:4]
	return phone

bangalore_called_phones = []
bangalore_sorted_called_phones_prefix = set()
for call in calls:
	if is_bangalore_fixed_phone(call[0]):
		bangalore_called_phones.append(call[1])
		bangalore_sorted_called_phones_prefix.add(get_phone_prefix(call[1]))

bangalore_sorted_called_phones_prefix = list(bangalore_sorted_called_phones_prefix)
bangalore_sorted_called_phones_prefix.sort()
#First Part
print("The numbers called by people in Bangalore have codes:")
for phone in bangalore_sorted_called_phones_prefix:
	print(phone)

#Second part
count = 0
for phone in bangalore_called_phones:
	if is_bangalore_fixed_phone(phone):
		count += 1 	
print()
print("{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
		percentage = round(count / len(bangalore_called_phones)*100, 2)
	)
)