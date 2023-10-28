import requests
import re
import os


data_input = input(">> ")
data = {
    "user": "user",
    "query": data_input
    + ",the command should be the last word(s) of the single sentence and in double quotes",
}

post_response = requests.post("http://localhost:8080/", json=data)

post_response_json = post_response.json()

print(post_response_json)


import re

text = post_response_json


pattern1 = '^(.*) "(.*)" command.'
pattern2 = '^(.*) "(.*)"'
pattern3 = '^(.*) "(.*)"\.'

m1 = re.search(pattern1, text)
m2 = re.search(pattern2, text)
m3 = re.search(pattern3, text)


if m1:
    found = m1.group(2)
    print("Pattern 1 match: ", found)
#  os.system(found)
elif m2:
    found = m2.group(2)
    print("Pattern 2 match: ", found)
#  os.system(found)
elif m3:
    found = m3.group(2)
    print("Pattern 3 match: ", found)
#  os.system(found)
else:
    print("No match found.")
