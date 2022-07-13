from sys import modules
from vars import client , Channel_ID , resolutions
from pyrogram import filters , Client
from pyrogram.types import  Message , ReplyKeyboardMarkup 
from plugins import videoProccessor
from time import time
from math import ceil
from urllib.parse import quote_plus
from plugins.uploadFileMessageProcess import get_name , get_hash
import hashlib
from plugins.database import insert  , current_domain
from json import dumps

class messages:

    customKeyboardMessage = None
    
    adding = False
    name   = ''

    
    waitingForResolution = False
    highestResolution = None
    movieId = None

    links = []
    
    
    waitingForFile = False
    
    def __init__ (self):
        self.start()
        self.add()
        self.reset()
        self.text()
        self.movieFile()
        

    def start (self):
        @client.on_message(filters.command("start"))
        async def start(client : Client , message : Message):
            
            await message.reply("Welcome to Sweetcima Resolution Converter Bot")
            

  
    def add (self):
        @client.on_message(filters.command("add"))
        async def add(client, message : Message):
            
            if self.adding == False:
                await message.reply("Ok , Send me Movie Name")
                self.adding = True

            else:
                await message.reply("Complete last movie first")

            

    def reset (self):
        @client.on_message(filters.command("reset"))
        async def reset(client , message : Message):
            
            self.status = None
            self.adding = False
            
            await message.reply("Reseted")
                
    def text(self):
        @client.on_message(filters.text & filters.private)
        async def text(client, message : Message):
            
            # add command 
            if self.adding and not self.waitingForResolution and not self.waitingForFile :
                
                await self.movieName(message)
                self.waitingForResolution = True
            
            # send resolution
            elif self.waitingForResolution and message.text in resolutions :
                
                self.highestResolution = message.text
                await message.reply("Highest Resolution is : " + self.highestResolution)
                await message.reply("Now , Send me the movie file")
                
                self.waitingForResolution = False
                self.waitingForFile = True
                await self.customKeyboardMessage.delete()

    async def movieName(self , message : Message) :
        
        self.name = message.text

        await message.reply("Movie Name is : " + self.name)
        self.customKeyboardMessage = await message.reply(
            "Now , what is Highest Resolution ? " , 
        reply_markup=ReplyKeyboardMarkup([resolutions], one_time_keyboard=True ))

    def movieFile(self ) :
        
        @client.on_message(filters.private & filters.video)
        def movieFile(client, message : Message):
            
            if (self.waitingForFile and not self.waitingForResolution ) or True:
                
                #forward the file to channel
                
                frowardedMessage = message.forward(chat_id=Channel_ID)
                
                txt = f"{time()}"
                id = hashlib.md5(txt.encode()).hexdigest()


                link = f"{frowardedMessage.id}/{quote_plus(get_name(frowardedMessage,True))}?hash={get_hash(frowardedMessage,True)}"
                
                links  = [{
                        'res'   : self.highestResolution ,
                        'link' : link 
                    }]

                
                insert(id, links, self.name)

                domain = current_domain()

                message.reply(f"http://{domain}/index.php?id={id}")


                

                self.movieId = id
                
                self.waitingForFile = False
                self.adding = False
                self.status = None
                self.waitingForResolution = False
                self.waitingForFile = False
                
                # message.reply(f"Done , its Link is {link}")
                # message.reply("Done , Now Proccessing the movie")

                # now proccess it 

                videoProccessor(message , self.highestResolution , id)
                
                
            
        
modules[__name__] = messages