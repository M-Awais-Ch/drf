import requests
import json
# URL='http://127.0.0.1:8000/teachinfo/'
# r=requests.get(url=URL)
# data=r.json()
# print(data)
# # print(r)
# URL='http://127.0.0.1:8000/teachinfo/'
URL='http://127.0.0.1:8000/stucreate/'
data={
    'roll':1,
    'name':'Muhammad Awais',
    'city':"Lahore",
    'dep' : 'DS'
}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
print(r)