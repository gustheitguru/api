#Posting to REST API


import requests

api_endpoint = 'https://api.stripe.com'
api_secret_key = 'sk_test_Y3ooLmB75UVwxE5WCIlJ7iHf'
api_pub_key = 'pk_test_UGh3yxtQY9mGrm3FLuAWtdAs'

def create_customer():
	endpoint = '/v1/customers'
	user = api_secret_key
	description = 'some thing'
	email = 'gus@gustheitguru.com'
	final_api_endpoint = api_endpoint + endpoint
	rmethod = 'POST'
	print user, description, final_api_endpoint
	auth = (user, "")
	params = {
		"email":email
	}
	r = requests.post(final_api_endpoint, auth=auth, params=params)
	return r.json()
	

new_customer = create_customer()

'''
test json = new_customer['object-item-name']
'''

'''
	print r.status_code
	print r.text
	print r.json()
'''


def update_customer_description(cust_id, description):
	new_endpoint = api_endpoint + '/v1/customers/' + cust_id
	auth = (api_secret_key, "")
	params = {
		"description":description
	}
	r = requests.post(new_endpoint, auth=auth, params=params)
	return r.json()

updated_c = update_customer_description(new_customer['id'], "Here is a new one")

#Get Request


import requests

api_endpoint = 'https://api.stripe.com'
api_secret_key = 'sk_test_Y3ooLmB75UVwxE5WCIlJ7iHf'
api_pub_key = 'pk_test_UGh3yxtQY9mGrm3FLuAWtdAs'

s = requests.get('https://api.stripe.com/v1/customers' , auth=(api_secret_key, ''))
print s.json()
print s.text



#not working
#def get_customer(x):
#	r = requests.get(new_endpoint, auth=auth, params=params)
#	return r.json()





