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
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | public repositories: {public_repos_count}"
    )
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
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


# Check who you follow
def get_your_following():
    endpoint = f'https://api.github.com/users/LemarTokham/following'
    response = requests.get(endpoint).json()
    following_amount = len(response)
    following_users = []
    for i in range(following_amount):
        following = response[i]["login"]
        following_users.append(following)
    return following_users

# Check who follows you
def get_your_followers():
    endpoint = f'https://api.github.com/users/LemarTokham/followers'
    response = requests.get(endpoint).json()
    followers_amount = len(response)
    follower_users = []
    for i in range(followers_amount):
        follower = response[i]["login"]
        follower_users.append(follower)
    return follower_users


def compare_following_followers(following_you, your_followers):
    not_following_back = []
    for follower in your_followers:
        if follower not in following_you:
            not_following_back.append(follower)
    return not_following_back



users_you_follow = get_your_followers()
print(f"Followers: {len(users_you_follow)}")
your_followers = get_your_following()
print(f"Following: {len(your_followers)}")
not_following_back = compare_following_followers(following_you=users_you_follow, your_followers=your_followers)
for user in not_following_back:
    print(f"{user} doesn't follow you back :(")
            