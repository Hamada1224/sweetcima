from sys import modules
from pyrogram.types import Message 
from vars import client
from time import time
from math import ceil
from plugins import converter


def videoProccessor (message : Message , highestResolution):
    
    # first Download the file

    messageToKeepUserUpdated = message.reply('Downloading ...')
    
    start = time()
    filePath = message.download()
    
    print(f"Download finished in {ceil(time() - start)}s")
    
    messageToKeepUserUpdated.edit(f"Downloaded , Now Proccessing the video")
    converter(filePath,highestResolution,message)

modules[__name__] = videoProccessor