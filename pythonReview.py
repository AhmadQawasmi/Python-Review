def  create_youtube_video(title, descreption):
    dict_video = {"title": title, "descreption": descreption, "likes" : 0, "dislikes" : 0, "conmments" : {"username" : ""}, }
    return dict_video

def likes(video):
       if likes in video:
        video["likes"] = video["likes"] + 1
        
        return video

def dislikes(video):
    if dislikes in video:
        video["dislikes"] = video["likes"] + 1
        
    return video

def add_comment(youtubevideo, username, comment_text):
    youtubevideo["comments"][username] = comment_text

    return youtubevideo

video = create_youtube_video("i saw ronaldo see what happend !!! ","ronaldo is the best : https://jirjx/gerert/wwrw")