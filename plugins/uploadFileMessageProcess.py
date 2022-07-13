from sys import modules

def get_name(media_msg, video = False):

    if video :
        return media_msg.video.file_name or ""
    
    else :
        return media_msg.document.file_name or ""
def get_hash(media_msg,video = False):

    if video :
        media = media_msg.video
    else :
        media = media_msg.document
    
    return getattr(media, "file_unique_id", "")[:6]


