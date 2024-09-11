# github.py
from dotenv import load_dotenv
import requests
import os

# loading up private keys
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

REDIRECT_URI = "https://httpbin.org/anything"

# creating the url that will direct the user to the Github Website to authorise access to our app
def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope":"user",
        "response_type":"code",
    }

    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params)
    return response.url


# Allow the code we get from the above authentication to be exchanged for an access token
# The code and client_secret is needed so github can validate your application
def exchange_code_for_access_token(code=None):
    params ={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri":REDIRECT_URI,
        "code":code,
    }

    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]

# Link user follows to connect this app to their github and be given a code to be exchanged for an access token
link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("Github code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")


def print_user_info(access_token=None):
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    public_repos_count = response["public_repos"]
    print(
        f"{name} ({username}) | public repositories: {public_repos_count}"
    )

print_user_info(access_token=access_token)

def check_following(username):
    endpoint = f'https://api.github.com/users/LemarTokham/following/{username}'
    response = requests.get(endpoint)
    if response.status_code == 204:
        print(f"You are following {username}")
    elif response.status_code == 404:
        print(f"You are not following {username}") 

user = input("Enter User: ")
check_following(user)

