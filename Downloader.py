import tkinter
#Several methods and functions to get certain information from your UI
import customtkinter
#Nicer UI
from pytube import YouTube
#Specific callback function you can use on the downloader

#ERRORS: AGE RESTRICTION ERROR
#   SOLUTION: CHANGE INNERTUBE CLASS LINE 223 CLIENT TO ANDROID_CREATOR INSTEAD OF ANDROID_MUSIC
#   Apparently Android_music and other clients resulted in being no streamingData in vid_info and ended up throwing an AgeRestrictedError
#   Location: PyTube - Main - InnerTube

def begin():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link,on_progress_callback=progressCall)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text = yt_object.title, text_color = "white")
        video.download()
        finishLabel.configure(text = "Download Complete")
    except Exception as e:
        finishLabel.configure(text = "Download Failed", text_color = "red")

#Chunks is a required parameter here or else it says download failed
def progressCall(stream, chunks, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size * 100
    per = str(int(percent_completed))
    percent.configure(text = per + "%")
    percent.update()

    #progress bar
    progress.set(float(percent_completed / 100))
    

#System Settings
customtkinter.set_appearance_mode("System")
#Dark Mode or Light Mode
customtkinter.set_default_color_theme("blue")

#Define app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx = 10, pady = 10)

#Link input
url_variable = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_variable)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress Percent
percent = customtkinter.CTkLabel(app, text = "0%")
percent.pack()

progress = customtkinter.CTkProgressBar(app, width = 400)
progress.set(0)
progress.pack(padx = 10, pady = 10)

#Download Button
download = customtkinter.CTkButton(app, text = "Download", command = begin)
download.pack(padx = 10, pady = 10)

#Run app
app.mainloop()