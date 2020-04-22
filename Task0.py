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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_record_texts = texts[0]
last_record_calls = calls[len(calls)-1]

text_incoming_number = first_record_texts[0]
text_answering_number = first_record_texts[1]
text_time = first_record_texts[2][11:20]

print('First record of texts, {0} texts {1} at time {2}'.format(*texts[0])) 

call_incoming_number = last_record_calls[0]
call_answering_number = last_record_calls[1]
call_during = last_record_calls[2]
call_time = last_record_calls[3]

print('Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'.format(*calls[-1]))