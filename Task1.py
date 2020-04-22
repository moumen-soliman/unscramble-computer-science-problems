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
def unique_phone_count(calls):        
    combined = set() 
    
    for call in calls: 
        outgoing_calls, incoming_calls = call[0], call[1]
        combined.add(outgoing_calls)
        combined.add(incoming_calls)

    for text in texts:
        outgoing_texts, incoming_texts = text[0], text[1]
        combined.add(outgoing_texts)
        combined.add(incoming_texts)

    return len(combined)

unique_phone_count(calls) # 570
count = unique_phone_count(calls) 
print('There are', count, 'different telephone numbers in the records.')