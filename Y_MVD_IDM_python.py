from pytube import YouTube

SAVE_PATH = "F:/CODING/Python_Project"

link1, link2 = input("Enter a two value (with separate comma): ").split()
video = YouTube(link1, link2)
stream = video.streams.get_highest_resolution()
stream.download(SAVE_PATH)
