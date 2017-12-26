__author__ = 'haaroony'

'''
This script reads the CCC phonebook json, parses it, returning a list of phonenumbers that 
you can use to register your GSM sim. 
It is a quick script so dont cry if it breaks or if the number was wrong. 
'''

import requests
from pprint import pprint

url = "https://eventphone.de/guru2/phonebook?event=34C3&format=json"
phonebookreq = requests.get(url)
phonebook = phonebookreq.json()

usedNumbers = set([])
# free numbers are 2100 and 8999
# parse all numbers into a set
for phone in phonebook:
    # {"extension":"01990","name":"EPVPN","phone_type":"0","location":""},{"extension":"1000","name":"Projektleitung","phone_type":"2","location":""}
    if 2100 <= int(phone["extension"]) <= 8999:
        usedNumbers.add(int(phone["extension"]))

# create a set of all phone numbers
count = 2100
allNumbers = set([])
while(count <= 8999):
    allNumbers.add(count)
    count += 1

# set difference to get the numbers which arent included
unused = allNumbers.difference(usedNumbers)
print("unused")
pprint(unused)

# find pretty numbers, e.g. numbers which have the same digit more than once
print("all numbers")
pretty = set([])
evenPrettier = set([])
for number in unused:
    count = 0
    cur = str(number)[0]
    for digit in str(number)[1:]:
        if cur == digit:
            pretty.add(number)
            count += 1
        else:
            cur = digit
    if count > 2:
        evenPrettier.add(number)

pprint("Pretty numbers")
pprint(pretty)

pprint("Even prettier")
pprint(evenPrettier)