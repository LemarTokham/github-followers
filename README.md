# GitHub API Project
Interacts with the GitHub API to perform various operations such as returning how many repos the user has, whether or not they follow another specified GitHub user, checking which one of their followers doesn't follow them back.

# Setup
1. Clone this repo
2. Create a virtual environment and activate it
3. Install required packages: `pip install -r requirements.txt` 
4. Obtain Github OAuth Credentials:
    - Go to GitHub Settings -> Developer Settings -> OAuth Apps -> New OAuth App
    - Give your application a name
    - Set homepage URL to `http://localhost:8000` or whatever local server you want it to run on
    - Set Authorization callback URL to `https://httpbin.org/anything`
5. Create a `.env` file with your GitHub Client ID and Secret key
    Structure of .env:
    - CLIENT_ID=your_client_id_here
    - CLIENT_SECRET=your_client_secret_here 
6. Run the script: `python3 app.py`

**Notes**
Further organisation of the code is underway, will make separate files with the different functionalities.