import requests

#api key or auth or oauth

oauth_token = 'BQ54OD2QAXRYGCRFV5CPZVYOAR2IEIA3PHUW1EENTAR0OHNS'

api_endpoint = 'https://api.foursquare.com/v2/venues/search'

params = {
	"oauth_token": oauth_token,
	"ll": "41, -74",
	"v":20150816,
}
r = requests.get(api_endpoint, params=params)
print r.url

for item in r.json()['response']['venues']:
	print item['name']


