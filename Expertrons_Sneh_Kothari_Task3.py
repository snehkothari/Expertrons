"""
OUTPUT

{"operator":"BSNL","circle":"Tamil Nadu"}
{"operator":"Jio","circle":"Mumbai"}

"""



import requests
import os
import re

response = open("response.xml","r")
res=response.read()

n = str(re.findall(r'[>][7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][<]',res)).split(" ")
output=[]
for i in n:
	mobile_no=""
	for k in i:
		if(k.isdigit()):
			mobile_no=mobile_no+k
	URL="https://api.datayuge.com/v1/lookup/"+mobile_no
	print(requests.get(URL).text)



