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

def printNumbersWhichCouldBeTelemarketers():
    callers = set()
    callReceivers = set()
    textReceivers = set()
    textSenders = set()

    for call in calls:
        caller = call[0]
        receiver = call[1]
        callers.add(caller)
        callReceivers.add(receiver)

    for text in texts:
        sender = text[0]
        receiver = text[1]
        textSenders.add(sender)
        textReceivers.add(receiver)

    callers = callers.difference(callReceivers)
    callers = callers.difference(textReceivers)
    callers = callers.difference(textSenders)

    telemarketers = list(callers)

    print("These numbers could be telemarketers: ")
    telemarketers.sort()
    for number in telemarketers:
        print(number)


printNumbersWhichCouldBeTelemarketers()

