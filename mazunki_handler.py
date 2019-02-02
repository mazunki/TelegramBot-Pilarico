"""
A file dedicated to handle a JSON item of Telegram's API according to mazunki's bot.

This file will check for the type of message which has been received, and redirect the
item to the correspondent function depending on the action to be held by it, defined
here.

Actions such as checking for a query is also handled in this file.

The return value of handle_message is the update_id for this message, allowing
us to state this message as read and handled.
"""

def handle_message(item):
    for item_key, item_value in item.items():
        if item_key == "message":
            for message_key, message_value in item_value.items():
                if message_key == "message_id":
                    print("id:", message_value, sep="")
                elif message_key == "text":
                    print("text:", message_value, sep="")
                else:
                    pass
            print()
        else:
            print(key, item_value)
