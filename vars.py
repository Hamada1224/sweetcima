from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
load_dotenv()

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
BOT_TOKEN = getenv('BOT_TOKEN')
Channel_ID = int(getenv('BIN_CHANNEL',None))
hostName = getenv('HOST')
port = int(getenv('PORT'))

DB_USERNAME = getenv('DB_USERNAME')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_NAME = getenv('DB_NAME')


if int(getenv('PROXY')) == 1 :

    proxy = {
        "scheme": "http",  # "socks4", "socks5" and "http" are supported
        "hostname": hostName,
        "port": port
}

    client = Client(
        "bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        proxy=proxy
    )
else :
    client = Client(
        "bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
)   
resolutions = ['1080', '720', '480', '360'] 