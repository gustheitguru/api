import requests

food2fork_endpoint = 'http://food2fork.com/api/search'
all_recipe_endpoint = 'http://food2fork.com/api/get'
api_key = '736e3acd4a98dbe7fec05d8a244fbc0a'

#function to search food2fork.com
def food_search(query):
	params = {
		"key":api_key,
		"q":query,
	}
	r = requests.get(food2fork_endpoint, params=params)
	lists = []
	f2f_url = []
	for items in r.json()['recipes']:
		lists.append(items['title'])
		f2f_url.append(items['f2f_url'])
		return lists, f2f_url
#need to add continues step iteration


#enter in food to search for
x = raw_input('Enter in ingerdients seperated by a common: ')
	# add input to list
	# combine list with commons
	

#run food_search function
food_search(x)




