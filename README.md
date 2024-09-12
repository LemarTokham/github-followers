# GitHub API Project
Interacts with the GitHub API to perform various operations such as returning how many repos the user has, whether or not they follow another specified GitHub user, checking which one of their followers doesn't follow them back.

# Setup
1. Clone this repo
2. Create a virtual environment and activate it
3. Install required package: `pip install -r requirements.txt` 
4. Create a `.env` file with your GitHub Client ID and Secret key
5. Obtain Github OAuth Credentials:
    - Go to GitHub Settings -> Developer Settings -> OAuth Apps -> New OAuth App
   - Register a new application and get your Client ID and Client Secret
6. Run the script: `python3 app.py`

**Notes**
Further organisation of the code is underway, will make separate files with the different functionalities.