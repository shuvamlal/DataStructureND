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

call_log = defaultdict(int)
for num in calls:
    call_log[num[0]] += int(num[3])                # adding from the senders side
        
    call_log[num[1]] += int(num[3])                # adding from the receivers side

max_val=0  
temp_key=0
for key, val in call_log.items():
    if max_val<val:
        max_val=val
        temp_key = key
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(temp_key, max_val))