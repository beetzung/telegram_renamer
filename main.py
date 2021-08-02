import json
import os
import random
import string
import time
from datetime import datetime, timedelta
import sys

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.account import UpdateUsernameRequest


def get_json(name, message, cast=str):
    file_name = 'api.json'
    value = None
    data = {}
    if os.path.isfile(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
            value = data.get(name)
    if value is None:
        value = cast(input(message))
        data[name] = value
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file)
    return value


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return random.choice(string.ascii_letters) + ''.join(random.choice(chars) for _ in range(size - 1))


def rename_user(client):
    with client:
        username = id_generator(size=32)
        print("renaming to " + username)

        def execute():
            try:
                client.loop.run_until_complete(client(UpdateUsernameRequest(username)))
            except FloodWaitError as e:
                seconds = e.seconds + 5
                print("Too often requests, waiting {} seconds...".format(seconds))
                time.sleep(seconds)
                execute()

        execute()
        print("success")


api_id = get_json("TG_API_ID", "Enter API ID: ", cast=int)
api_hash = get_json("TG_API_HASH", "Enter API hash: ")
bot = TelegramClient("anon", api_id, api_hash)
bot.start(password=lambda: get_json('TG_2FO_PASS', 'Enter the 2FO password: '))

if len(sys.argv) > 1:
    arg = sys.argv[1]
    try:
        secs = int(arg)
    except ValueError:
        print(arg + " is not a number")
        secs = 60 * 60
else:
    secs = 60 * 60


while True:
    rename_user(bot)
    time.sleep(secs)
