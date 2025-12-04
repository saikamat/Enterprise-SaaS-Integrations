# import statements
from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

# get the github token
try:
    GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
except KeyError:
    raise ValueError("GITHUB_TOKEN not found in environment variables. Did you create a .env file?")

# get the slack bot token token
try:
    SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
except KeyError:
    raise ValueError("SLACK_BOT_TOKEN not found in environment variables. Did you create a .env file?")

# get the google API token token
try:
    GOOGLE_CLIENT_ID = os.environ['GOOGLE_CLIENT_ID']
except KeyError:
    raise ValueError("GOOGLE_CLIENT_ID not found in environment variables. Did you create a .env file?")

try:
    GOOGLE_CLIENT_SECRET = os.environ['GOOGLE_CLIENT_SECRET']
except KeyError:
    raise ValueError("GOOGLE_CLIENT_SECRET not found in environment variables. Did you create a .env file?")