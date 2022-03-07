import requests
import os

APP_ID = os.environ.get('APPLICATION_ID')
TOKEN = os.environ.get('BOT_TOKEN')
SERVER_ID = "476818108896772109"

url = f"https://discord.com/api/applications/{APP_ID}/guilds/{SERVER_ID}/commands"

# This is an example USER command, with a type of 2
json = {
    "name": "newgame",
    "type": 1,
    "description": "Creates a new game"
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {TOKEN}"
}


# r = requests.post(url, headers=headers, json=json)
r = requests.get(url, headers=headers)
print(r)
print(r.reason)
print(r.text)