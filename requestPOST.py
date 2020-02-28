import requests #request library
import json

username = input("Masukan username : ")
password = input("Masukan password : ")
#input

#request POST
URL = "http://intapi.oomph.co.id/dolanin/login_by_msisdn"
PARAMS	= {'msisdn':username, 'password':password}
request = requests.post(URL, PARAMS)
result 	= request.json()
if request.status_code == 200:
	data 	= result['result']
	for row in data:
		print("MSISDN : "+row['msisdn'])
		print("Registered at : "+row['created_at'])
else:
	print(request.text)