import requests
import json

headers = {"Content-Type":'application/json'}
url = 'http://127.0.0.1:8000/studentapi3/?ordering=name'

def getdata(id=None,token=None):
    r = requests.get(headers=headers, url=url)
    print(r.json())

def postdata():
    data={
        'name':'Shiv',
        'roll':103,
        'city':'Kailash'
    }
    r = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(r.json())

def deletedata():
    url = 'http://127.0.0.1:8000/studentapi/6'
    r = requests.delete(headers=headers, url=url)
    if r.text:
        print(r.text)
    else:
        print("deleted the student")

getdata()


# curl_command = f'curl -X POST --header "Authorization:bearer {access}" http://127.0.0.1:8000/verifytoken/'
# import os
# os.system(curl_command)