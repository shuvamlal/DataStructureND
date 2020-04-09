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

texts_numbers = []
for i in texts:
    texts_numbers.append(i[0])
    texts_numbers.append(i[1])
print("There are {} different telephone numbers in the record of texts.".format(len(texts_numbers)))
calls_numbers = []
for i in calls:
    calls_numbers.append(i[0])
    calls_numbers.append(i[1])
print("There are {} different telephone numbers in the record of calls.".format(len(calls_numbers)))

temp = []
for i in texts_numbers:
    if i in calls_numbers:
        temp.append(i)
print("There are {} different telephone numbers in the records.".format(len(temp)))