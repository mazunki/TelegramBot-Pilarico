"""
A file dedicate uniquely to send a text message through a Telegram bot, with different parameters,
called by mazunki_handler, allowing multiple parameters as per Telegram's API.

Returns no value, since none are required, as for now. 
"""

import requests

bot_token = "334487382:AAHaUSXMSOoJJ4HRzX09z8NyGqaPs04NpxI" # Will be replaced with a configuration file
tg_link = "https://api.telegram.org/bot" + bot_token + "/" # Will be replaced with a conf file

def send_message(msg, where, reply=None, notifications=False):
    data = {"text": msg,
            "chat_id": int(where),
            "reply": reply,
            "disableNotifications": not notifications  # Inverting because more intuitive parameter
            }

    response = requests.get(tg_link + "sendMessage", data)
