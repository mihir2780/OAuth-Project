import requests # handling HTTP requests
import json # storing token in json file
from datetime import datetime # for timestamps handling

def save_user(name, token_data):
    #saving user details in this logic
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Adding timestamp to the filename
    filename = f"{name}_access_details_{timestamp}.json" # filename
    details_to_save = { #required data saved in the file
        'name': name,
        'access_token': token_data['access_token'],
        'scopes': token_data['scopes'],
        'expires_in': token_data['expires_in'],
        'timestamp': str(datetime.now())
    }
    try:
        with open(filename, 'w') as file:
            json.dump(details_to_save, file)
        print(f"User details saved to {filename}.")
    except IOError as e:
        print(f"Failed to save user details: {e}")

def obtain_access_token(username, password, oauth_server_url):
   # Logic for obtaining token from the OAuth server
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'} # header declared to HTTP post request form submission

    try:
        response = requests.post(oauth_server_url, data=data, headers=headers)
        response.raise_for_status()

        token_data = response.json()
        access_token = token_data.get('access_token')

        if access_token:
            print("Access token successfully obtained.")
            user_name = token_data.get('name', username)
            save_user(user_name, token_data)  # Save only the user's full name
            print("User is authenticated successfully to the third-party application.")
            return True
        else:
            print("Access token not found in response.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Failed to obtain access token due to an error: {e}")
        return False

if __name__ == '__main__':
    print("Get your access token for third-party application login")
    oauth_server_url = 'http://localhost:5000/token'
    
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if obtain_access_token(username, password, oauth_server_url):
            choice = input("Do you want to obtain another access token? (yes/no): ").lower()
            if choice != 'yes':
                break
