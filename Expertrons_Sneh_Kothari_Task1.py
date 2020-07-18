import requests
import json
from requests.compat import quote_plus

def print_top10(response):
	res = json.loads(response)
	if(len(res['articles'])==0):
		print("No news")
	else:
		i=0
		for responses in res['articles']:
			if(i<10):
				print("News: " + str(i+1))
				print(responses)
			else:
				break
			i+=1

search = input("Enter search term: ")

choice = int(input("Input choice \n1: Query \n2: Source "))

URL_SOURCE = "https://newsapi.org/v2/top-headlines?sources={}&apiKey=21e7ec9556e54e369033662e53fa1117" 
URL= "https://newsapi.org/v2/top-headlines?q={}&apiKey=21e7ec9556e54e369033662e53fa1117" 
URL_DATE ="https://newsapi.org/v2/top-headlines?q={}&from={}&apiKey=21e7ec9556e54e369033662e53fa1117" 
if(choice==1):
	date = input("Enter date: YYYY-MM-DD\nOtherwise enter N:")
	if(date=='N'):
		response = requests.get(URL.format(quote_plus(search)))
		print_top10(response.text)
	else:
		print(URL_DATE.format(quote_plus(search),date))
		response = requests.get(URL_DATE.format(quote_plus(search),date))
		print_top10(response.text)

elif(choice==2):
	response = requests.get(URL_SOURCE.format(quote_plus(search)))
	print_top10(response.text)
else:
	print("Invalid choice")