"""
A file to handle each cycle of bot's actions. Starts loop by finding last loop, and saves last query each time
a new item is handled. This avoids duplicate responses, in case program is halted.

Bot is based on Telegam's official and native API calls, instead of webhooks, in this version, since it's easier to develop.
Works for Telegram as per 26 January 2019 on stable releases.

The bot is modularised by files, where each file handles one type of action, allowing ease of updating, and expansion.

For a further reference to the bot's support, see README.md.
"""

from mazunki_handler import *
#from mazunki_getupdates import *
#from mazunki_sendmessages import *

import requests # URL calls, replaces obsolete webbrowser
import json # Content of url calls is in JSON format, allowing us to make dictionaries, instead of working with strings.

bot_token = "334487382:AAHaUSXMSOoJJ4HRzX09z8NyGqaPs04NpxI" # Given by @BotFather, selecting bot with /mybots, and asking for API token.
tg_link = "https://api.telegram.org/bot" + bot_token + "/" # Main API calls are based on this hyperlink

for _ in range(1):
    try:
        with open("lastQuery.ini", "r") as file:
            lastQuery_id = int(file.read())
    except FileNotFoundError:
        print("< No last query found, ignoring. >")

    data = {"offset": lastQuery_id}  # Setting data as a variable in order to easily change it
    response = requests.get(tg_link+"getUpdates", data)
    print(tg_link+"getUpdates", data, sep="")
    json_response = response.json()  # Dictionary!
    # print(json.dumps(json_response, indent=2))


    if len(json_response.keys()) == 2 and "result" in json_response.keys(): # "ok", "result"
        if len(json_response["result"]) > 0: # at least 1 new message
            for item in json_response["result"]:
                try:
#                    print(item["message"]["message_id"], item["message"]["text"])
                    handle_message(item)  # This file will handle it! Trust me!
                except BaseException as e:
                    print(e)
                    print("<unsupported message type>:", end="")
                    print(json.dumps(item, indent=2))
                with open("lastQuery.ini", "w+") as file:
                     try:
                         last_id = json_response["result"][-1]["update_id"]
                         file.write(str(last_id))
                         print(last_id, "printed to file")
                     except BaseException as e:
                         print(item, e)
                         print("< Failed at writing to file, please check. >")
                         exit()
