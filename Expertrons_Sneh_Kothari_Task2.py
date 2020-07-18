"""
OUTPUT

https://www.nytimes.com/article/juneteenth-food-black-chefs.html
https://www.nytimes.com/2020/03/31/books/review/new-this-week.html
https://www.nytimes.com/2020/03/25/world/asia/india-lockdown-coronavirus.html
https://www.nytimes.com/2005/03/06/travel/hotel-indigo-in-atlanta.html
https://www.nytimes.com/2010/12/05/travel/05indigo-checkin.html
https://www.nytimes.com/1997/06/05/arts/a-new-shade-of-indigo.html
https://www.nytimes.com/video/movies/100000003008786/movie-review-mood-indigo.html
https://www.nytimes.com/2013/02/08/arts/design/blues-for-smoke-at-the-whitney-museum.html
https://tmagazine.blogs.nytimes.com/2015/05/26/toogoods-tiina-laakkonen-indigo-amagansett/
https://campaignstops.blogs.nytimes.com/2012/04/11/the-dusted-indigo-period/

"""


import requests
import json
from requests.compat import quote_plus

search = "Indigo"

URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={}&api-key="

api_key = "############################"

response = requests.get(URL.format(quote_plus(search))+api_key)
print(URL.format(quote_plus(search))+api_key)
res = json.loads(response.text)['response']['docs']


for link in res:
	print(link['web_url'])