import requests
import json

url = 'http://127.0.0.1:8000/studentapi9/'

headers = {"Content-Type":'application/json'}


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(headers=headers, url=url, data=json_data)
    result = r.json()
    print(result)

def post_data():
    data = {
        'name': 'Ram',
        'roll': 111,
        'city': 'ayodhya'
    }
    r = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(r.json())

def update_data(pk=1):
    data = {
        'id': 3,
        'name': 'Bhishma',
        'roll': 456,
        'city': 'Hastinapur'
    }
    r = requests.put(headers=headers, url=url, data=json.dumps(data))
    print(r.json())

def delete_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    r = requests.delete(headers=headers, url=url, data=json.dumps(data))
    print(r.json())


# post_data()
# update_data()
# delete_data(3)

# get_data(2)   


###################Code For API Token authentication#########################

#Curl command for checking the Token genration
# curl_command = 'curl -X POST -d "username=mahesh&password=mahesh" http://127.0.0.1:8000/getcustomtoken/'
# import os
# os.system(curl_command)

#POST method for checking the Token generation  
def gettoken():
    tokenurl = 'http://127.0.0.1:8000/getcustomtoken/'
    data = {
        'username': 'mahesh',
        'password': 'mahesh'
    }
    r = requests.post(headers=headers, url=tokenurl, data=json.dumps(data))
    print(r.json())
    return r.json().get('token')
token = gettoken()

curl_command = f'curl --header "Authorization:token {token}" http://127.0.0.1:8000/studentapi10/'
import os
os.system(curl_command)

#Get command to get the details with token authentication
def getdata():
    tokenurl = 'http://127.0.0.1:8000/studentapi10/'
    headers={'Authorization': f'token {token}'}
    r = requests.get(headers=headers, url=tokenurl)
    result = r.json()
    print(result)
# getdata()