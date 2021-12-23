from pymsgbox import alert
from tkinter import *
from pytube import YouTube

def main():
    global url
    global path
    main = Tk()
    title = main.title("YouTube Downloader")
    text = Label(main, text='Hi! This is a simple YouTube Video Downloader\r\nEnter YouTube Video URL:\r\n').pack()
    url = StringVar()
    path = StringVar()
    input_url = Entry(main, textvariable=url).pack()
    text2 = Label(main, text='\r\nIf you entered a URL, then enter download path:\r\n').pack()
    input_path = Entry(main, textvariable=path).pack()
    button_DownloadVideo = Button(text="Download Video", command=YouTubeVideoDownloader).pack()
    main.mainloop()

def YouTubeVideoDownloader():
    try:
    	YT = YouTube(url.get())
    	alert(text=f"The video exists:\nTitle of the video: {YT.title}\nChannel of the video: {YT.author}\nViews of the video: {YT.views}", title="YouTube Downloader")
    except:
    	alert(text="ERROR : video " + url.get() + " doesnt exist", title="ERROR")
    	return
    try:
    	Vid = YT.streams.get_highest_resolution()
    	Vid.download(path.get())
    	
    except:
    	alert(text="ERROR: directory" + path.get() + " doesn't exist")
    	return
  
main()