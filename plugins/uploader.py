from sys import modules
from pyrogram.types import Message
from plugins.database import update

def uploader(path,res,message : Message , id ):
    
    
    from plugins.uploadFileMessageProcess import get_name , get_hash
    from urllib.parse                     import quote_plus
    from vars                             import client , Channel_ID
    from time                             import time
    from math                             import ceil
    from os                               import remove
    
    start = time()
    
    _       = message.reply_document(path)
    resFile = _.forward(Channel_ID)
    
    
    link = f"{resFile.id}/{quote_plus(get_name(_))}?hash={get_hash(resFile)}"
    
    update(id, res, link)

    _.delete()
    remove(path)
    
    message.reply(f"Resolution {res} uploaded in {ceil(time() - start)}s")


modules[__name__] = uploader