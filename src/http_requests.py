import requests
import mytoken

url = "https://discord.com/api/v10/applications/943668329871200258/commands"
command_id = "1017081667220938753"

json = {
    "name": "reset",
    "type": 1,
    "description": "Resets the game.",
    "options": [
        {
            "name": "card_set",
            "description": "Specifies the deck to use.",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Fate of the Hunter",
                    "value": 'hunter'
                },
                {
                    "name": "Saen'dal Arcana",
                    "value": "arcana"
                }
            ]
        }
    ]
}

headers = {
    "Authorization": f"Bot {mytoken.token}"
}

#post = requests.post(url, headers=headers, json=json)
#print(post.text)

get = requests.get(url, headers=headers)
print (get.text)

#delete = requests.delete(url, headers=headers)
#print(delete.text)