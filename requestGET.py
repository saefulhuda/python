import requests #request library
import json


#input
start = input("Masukan Start Row Data : ")
limit = input("Masukan Limit Row Data : ")

# request GET
URL 	= "http://intapi.oomph.co.id/dolanin/get_prize_list"
PARAMS	= {'start':start, 'limit':limit}
# HEADERS = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}
request = requests.get(url = URL, params = PARAMS)
# request = requests.get(url = URL, headers = HEADERS)
# print (request.headers)
result 	= request.json()
if request.status_code == 200:
	data 	= result['result']
	for row in data:
		iD 	= row['id']
		name = row['name']
		image = row['image_url']
		needed = row['point_needed']
		amount = row['amount']
		print(iD, name, image, needed, amount)
else:
	print(request.text)