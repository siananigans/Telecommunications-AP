import requests
import json
from concurrent.futures import ThreadPoolExecutor
api_token = ""
email = ""

def get_connections(user_id):
	connections = []
	check_url = "" + str(user_id) #insert private url here

	connections_json = requests.get(check_url)

	if connections_json.status_code != 200:
		print("Error")

	else:
		connection_dict = json.loads(connections_json.text)
		if connection_dict != []:
			for n in connection_dict:
				if n["connection_name"] != "Forward Only":
					connections.append(n["connection_id"])
			return(connections)


def get_api_token(user_id):
	user_url = "" + str(user_id) + "" #insert private url here
	
	user_json = requests.get(user_url)

	if user_json.status_code != 200:
		print("Error")
	
	else:
		user_dict = json.loads(user_json.text)
		if user_dict != []:
			api_token = user_dict[0]["api_token"]
			email = user_dict[0]["email"]
			return(api_token, email)

#Think about forward only conection
def update_connection(connection_id):
	headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'x-api-token': str(api_token),
		'x-api-user': str(email)
	}
	url = "https://api.telnyx.com/security/connections/" + str(connection_id)
	payload = {'active':'true'}
	response=requests.put(url, headers=headers, data = json.dumps(payload))
	return(response.status_code)




def main():
	global api_token, email
	user_id = "" #admin user id
	#c = get_connections(user_id)
	#print(c)
	result = get_api_token(user_id)
	api_token = result[0]
	email = result[1]
	connections = get_connections(user_id)
	with ThreadPoolExecutor(max_workers=8) as executor:
            for response_code in executor.map(update_connection, connections):
                print(response_code)


if __name__ == '__main__':
	main()
