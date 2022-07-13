from sys import modules
def converter(fileName , highestResolution , message):

    import os
    from math import ceil
    from time import time
    from threading import Thread
    from vars import resolutions
    import uploader

    x = filter(lambda x : int(x) < int(highestResolution) , resolutions)
    
    
    for r in x :
    
        rawName   = fileName.split('.')[0]
        extention = fileName.split('.')[1]
        newName   = f"{rawName}_{r}.{extention}"
        aspect    = 16/9
        
        width = ceil( int(r) * aspect ) 
        

        os.system(f"ffmpeg -i {fileName} -c:v libx264 -crf 22 -vf scale={width}:{r}  {newName}")
        
        print(f"finished quailty {r}")
        uploader(newName,r,message)
        
        
        

modules[__name__] = converter