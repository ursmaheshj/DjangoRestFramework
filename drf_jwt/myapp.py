import requests
import json

headers = {"Content-Type":'application/json'}

def getdata(id=None,token=None):
    url = 'http://127.0.0.1:8000/studentapi/'
    if not verifytoken(token):
        print("Token is expired")
    headers={'Authorization': f'Bearer {token}'}
    r = requests.get(headers=headers, url=url)
    print(r.json())

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
getdata(token=access)








# refresh='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzY4MjgwNywiaWF0IjoxNzA3NTk2NDA3LCJqdGkiOiJmMGMxMTg1MDI4Zjc0OTYwYWUzMWJiNjYwYTJjZTJlZCIsInVzZXJfaWQiOjF9.scnZMGoHZPWT6Nx7EkMezk5dAnbjGjlEvbDuVVvN8J4'
# access='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NTk2NzA3LCJpYXQiOjE3MDc1OTY0MDcsImp0aSI6ImM0ZTc0M2FkNWM3NjQ2M2I5ODFjZjczY2RjMDk0ODVhIiwidXNlcl9pZCI6MX0.RCx8wdmvahLTcvu0M1r6uNgYqVB8qKKBqTLO1Ppquu0'
# refreshtoken(refresh)
# getdata(token=access)
# CURL COMMAND

# curl_command = f'curl -X POST --header "Authorization:bearer {access}" http://127.0.0.1:8000/verifytoken/'
# import os
# os.system(curl_command)