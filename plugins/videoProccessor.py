from sys import modules
from pyrogram.types import Message 
from vars import client
from time import time
from math import ceil
from plugins import converter
from os import system


def videoProccessor (message : Message , highestResolution , id):
    
    # first Download the file

    messageToKeepUserUpdated = message.reply('Downloading ...')
    
    start = time()
    filePath = message.download()
    
    newName = f"downloads/{ceil(time())}.mp4"
    system(f"mv {filePath} {newName}")
    
    filePath = newName

    messageToKeepUserUpdated.reply(f"Download finished in {ceil(time() - start)}s")
    
    converter(filePath,highestResolution,message , id)

modules[__name__] = videoProccessor