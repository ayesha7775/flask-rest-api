import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"api1")
response = requests.get(BASE+"api2")

response = requests.post(BASE+"api3/1",{"name": "Anita", "dept": "CSE"})
response = requests.post(BASE+"api3/2",{"name": "Alisha", "dept": "ECE"})
response = requests.post(BASE+"api3/3",{"name": "Afifa", "dept": "BBA"})
response = requests.put(BASE+"api3/2",{"name": "Alisha", "dept": "CSE"})
response = requests.get(BASE+"api3/2")
print(response.json())
response =  requests.delete(BASE+"api3/3")
print(response)
