import requests
import json

headers = {"Content-Type":'application/json'}
url = 'http://127.0.0.1:8000/studentapi/'

def getdata(id=None,token=None):
    headers = globals()['headers']
    if not verifytoken(token):
        print("Token is expired")
    if token is not None:
        headers={'Authorization': f'Bearer {token}'}
    r = requests.get(headers=headers, url=url)
    print(r.json())

def postdata(token):
    if not verifytoken(token):
        print("Token is expired")
    headers={'Authorization': f'Bearer {token}','Content-Type':'application/json'}
    data={
        'name':'Shiv',
        'roll':103,
        'city':'Kailash'
    }
    r = requests.post(headers=headers, url=url, data=json.dumps(data))
    print(r.json())

def deletedata(token):
    url = 'http://127.0.0.1:8000/studentapi/6'
    if not verifytoken(token):
        print("Token is expired")
    headers={'Authorization': f'Bearer {token}','Content-Type':'application/json'}
    r = requests.delete(headers=headers, url=url)
    if r.text:
        print(r.text)
    else:
        print("deleted the student")


def gettoken():
    tokenurl = 'http://127.0.0.1:8000/gettoken/'
    data = {
        'username': 'mahesh',
        'password': 'mahesh'
    }
    r = requests.post(headers=headers, url=tokenurl, data=json.dumps(data))
    print(r.json())
    return r.json().get('access'),r.json().get('refresh')

def refreshtoken(refresh):
    tokenurl = 'http://127.0.0.1:8000/refreshtoken/'
    # headers={'Authorization': f'token {refresh}'}
    data = {
        'refresh':refresh
    }
    r = requests.post(headers=headers, url=tokenurl,data=json.dumps(data))
    return r.json().get('access')

def verifytoken(token):
    tokenurl = 'http://127.0.0.1:8000/verifytoken/'
    data = {
        'token':token
    }
    # headers={'Authorization': f'token {token}'}
    r = requests.post(headers=headers, url=tokenurl,data=json.dumps(data))
    if r.json().get('code')=='token_not_valid':
        return False
    else:
        return True
    
access,refresh = gettoken()
print(verifytoken(access))
# postdata(token=access)
# deletedata(token=access)
getdata()
getdata()
getdata()
getdata()
getdata()
getdata()
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)
getdata(token=access)








# refresh='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzY4MjgwNywiaWF0IjoxNzA3NTk2NDA3LCJqdGkiOiJmMGMxMTg1MDI4Zjc0OTYwYWUzMWJiNjYwYTJjZTJlZCIsInVzZXJfaWQiOjF9.scnZMGoHZPWT6Nx7EkMezk5dAnbjGjlEvbDuVVvN8J4'
# access='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NTk2NzA3LCJpYXQiOjE3MDc1OTY0MDcsImp0aSI6ImM0ZTc0M2FkNWM3NjQ2M2I5ODFjZjczY2RjMDk0ODVhIiwidXNlcl9pZCI6MX0.RCx8wdmvahLTcvu0M1r6uNgYqVB8qKKBqTLO1Ppquu0'
# refreshtoken(refresh)
# getdata(token=access)
# CURL COMMAND

# curl_command = f'curl -X POST --header "Authorization:bearer {access}" http://127.0.0.1:8000/verifytoken/'
# import os
# os.system(curl_command)