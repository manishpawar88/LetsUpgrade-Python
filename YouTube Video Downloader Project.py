import pytube
from pytube import YouTube
from tkinter import *

def downloadVideo():
    url = var.get()
    ytVideo = YouTube(url).streams.filter(file_extension="mp4").order_by('resolution').desc().first()
    ytVideo.download(r"D:\LetsUpgrade\Python\Downloaded Youtube Videos") 

root = Tk()

root.geometry("400x150")
root.title("YouTube Video Downloader")

l1 = Label(root,text="YouTube Video Link",fg="Red",font=("bold",20))
l1.place(x=70,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=20,y=60)

b1 = Button(root,text="Download",command=downloadVideo,bg="green",width=20,fg="White")
b1.place(x=120,y=90)

root.mainloop()
