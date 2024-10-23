import requests

add_URL = "http://localhost:5001/add"
sub_URL = "http://localhost:5001/subtract"
a = 5
b = 6
data = {"a":a, "b":b }
response = requests.post(sub_URL, json=data)

print(f"the answer is {response.json()['result']}")