from plugins import messages
from pyrogram import Client, filters
from pyrogram.types import Message
from vars import client


print('bot started ...')

messages()
client.run()