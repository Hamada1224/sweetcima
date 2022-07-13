from sys import modules
from pyrogram.types import Message
from urllib.parse import quote_plus
from plugins.uploadFileMessageProcess import get_name , get_hash
def uploader(path,res,message : Message):
    
    from vars import client , Channel_ID

    print('upload get invoked')
    _ = message.reply_document(path)
    resFile = _.forward(Channel_ID)
    
    link = f"{resFile.id}/{quote_plus(get_name(_))}?hash={get_hash(resFile)}"
    _.delete()
    message.reply(f"Resolution {res} has a link of {link}")


modules[__name__] = uploader