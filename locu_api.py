import requests

api_key = 'c98c4429c7dfef30a0d4f7d0bd51c9628b8f6646'

api_endpoint = 'https://api.locu.com/v1_0/venue/'

def venue_details(venue_id):
	venue_point = api_endpoint + venue_id + '/'
	params = {
		"api_key":api_key,
	}
	r = requests.get(venue_point, params=params)
	obj = r.json()
	print r.url
	return obj['objects'][0]['name'], obj['objects'][0]['has_menu']

def search_r(locality):
	search_point = api_endpoint + 'search/'
	params = {
		"api_key":api_key,
		"category": "restaurant",
		"locality":locality,
	}
	r = requests.get(search_point, params=params)
	objects = r.json()["objects"]
	names = []
	for item in objects:
		names.append(item['id'])
		print venue_details(item['id'])
	return names

print search_r("Denver")


print search("lakewood")


print search("Englewood")

# #Starting Test Code
# params = {
# 	"api_key":api_key,
# 	"categories":"restaurant",
# 	"locality":"Newport Beach",
# }

# r = requests.get(api_endpoint, params=params)
# print r.url
# print r.json()


# objects = r.json()["objects"]

# for item in objects:
# 	print item['name']