from pytube import YouTube

SAVE_PATH = "F:/CODING/Python_Project"

link = input("inter the link: ")
video =  YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download(SAVE_PATH)