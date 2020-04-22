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

def potential_telemarketers(calls, texts): 
    qualified_telemarketers_set = set()
    non_qualified_numbers_set = set()
    
    for call in calls:
        outgoing_calls, incoming_calls = call[0], call[1] 
        qualified_telemarketers_set.add(outgoing_calls)
        non_qualified_numbers_set.add(incoming_calls)
            
    for text in texts:
        outgoing_text, incoming_text = text[0], text[1] 
        non_qualified_numbers_set.add(outgoing_text)
        non_qualified_numbers_set.add(incoming_text)
 
    difference = qualified_telemarketers_set - non_qualified_numbers_set  
    result = sorted(difference)

    print("These numbers could be telemarketers: \n")
    print('\n'.join(result))
    
potential_telemarketers(calls, texts)