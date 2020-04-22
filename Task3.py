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

def get_phone_type(phone):
    if phone.startswith('(080)'):
        return 'bangalore'
    elif phone.startswith('140'):
        return 'telemarketer'
    elif phone.startswith('(0'):
        return 'fixed_lines'
    else:
        return 'mobile_number'

def bangalore_receiver_codes(calls):
    receiver_list = []
    codes = []  
    
    for call in calls:
        caller, receiver = call[0], call[1]
        caller_type = get_phone_type(caller)

        if caller_type == 'bangalore':
            receiver_list.append(receiver)
          
    for phone in receiver_list:
        if get_phone_type(phone) == 'bangalore': 
            codes.append(phone[1:4])
        elif get_phone_type(phone) == 'telemarketer': 
            codes.append(phone[:3])
        elif get_phone_type(phone) == 'fixed_lines': 
            codes.append(phone.split('(', 1)[1].split(')')[0])
        else:
            codes.append(phone[:4]) # mobile: first 4 digits
    
    print("The numbers called by people in Bangalore have codes:\n")
    print('\n'.join(sorted(set(codes))))

bangalore_receiver_codes(calls)

def fixed_percent(calls):
    from_fixed = 0         
    from_fixed_to_fixed = 0

    for call in calls:
        caller, receiver = call[0], call[1]
        caller_type = get_phone_type(caller)
        receiver_type = get_phone_type(receiver)

        if caller_type == 'bangalore':
            from_fixed += 1             # counter 

        if caller_type == 'bangalore' and receiver_type == 'bangalore': 
            from_fixed_to_fixed += 1   # counter 
    
    answer = from_fixed_to_fixed / from_fixed * 100
    percent = round(answer, 2) 
    print(percent, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.\n")

fixed_percent(calls)