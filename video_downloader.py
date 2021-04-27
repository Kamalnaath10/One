from pytube import YouTube
link = input("https://www.youtube.com/watch?v=Jt4Z1vwtXT0")
video = YouTube("https://www.youtube.com/watch?v=Jt4Z1vwtXT0")
if video:
    print("Yes")
stream = video.streams.get_highest_resolution()
if stream:
    print("Download initiated")
stream.download()
if stream.download():
    print("Completed")