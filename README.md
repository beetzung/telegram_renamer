# Telegram Renamer

This app will rename your Telegram account with random 32 chars string with a period of an hour (by default)   

## Quickstart
To use it, install Telethon lib

    pip3 install telethon

and then simply run main.py

    python3 main.py

Program will ask you once for API id and hash (you can get them [here](https://my.telegram.org/)), phone number and SMS-code


## Two-factor authentication
If you have 2FA enabled in your settings, use this command to log in with your password:

    python3 main.py -p [password]

## Other settings
You can set frequency in seconds using this:

    python3 main.py -s 3600
