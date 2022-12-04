import os


from tkinter import *
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

icon = "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"

app = customtkinter.CTk()
app.geometry("320x350")
app.title("Downloader [@TFC]")
photo = PhotoImage(data=icon)
app.iconphoto(False, photo)

videos = []

#region functions
def button_function():
    try:
        text = inputfield.get()
        print(text)
        videos.append(text)
        textbox.configure(state='normal')
        textbox.insert("0.0", text + "\n")
        textbox.configure(state='disabled')
        inputfield.delete(0, 'end')
    except:
        pass

def button3_function():
    videos.clear()
    textbox.configure(state='normal')
    textbox.delete("0.0", 'end')
    textbox.configure(state='disabled')
    textboxerror.configure(state='normal')
    textboxerror.delete('0.0', "end")
    textboxerror.configure(state='disabled')

def button2_function():
    try:
        for download in videos:
            textboxerror.configure(state='normal')
            textboxerror.delete('0.0', "end")
            textboxerror.insert("0.0", "Downloading...")
            textboxerror.configure(state='disabled')
            yt = YouTube(download)
            video = yt.streams.filter(abr='160kbps').last()
            out_file = video.download(output_path="./Downloaded")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded.")
            textboxerror.configure(state='normal')
            textboxerror.delete('0.0', "end")
            textboxerror.insert("0.0", "Downloaded!")
            textboxerror.configure(state='disabled')
        videos.clear()
        textbox.configure(state='normal')
        textbox.delete("0.0", 'end')
        textbox.configure(state='disabled')
    except FileExistsError:
        textboxerror.configure(state='normal')
        textboxerror.delete('0.0', "end")
        textboxerror.insert("0.0", str(out_file) + " File exists!")
        textboxerror.configure(state='disabled')
        os.remove(out_file)
    except RegexMatchError:
        textboxerror.configure(state='normal')
        textboxerror.delete('0.0', "end")
        textboxerror.insert("0.0", "URL Error! Check URL list")
        textboxerror.configure(state='disabled')

#endregion

#region fields
inputfield = customtkinter.CTkEntry(master=app, placeholder_text="Paste URL...")
inputfield.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=app, text="Add to list", command=button_function)
button.pack(pady=5, padx=10)

button2 = customtkinter.CTkButton(master=app, text="Download list", command=button2_function)
button2.pack(pady=5, padx=10)

button3 = customtkinter.CTkButton(master=app, text="Clear list", command=button3_function)
button3.pack(pady=5, padx=10)

textbox = customtkinter.CTkTextbox(master=app, width=200, height=100)
textbox.configure(state='disabled')
textbox.pack(pady=10, padx=10)

textboxerror = customtkinter.CTkTextbox(master=app, width=200, height=10)
textboxerror.configure(state='disabled')
textboxerror.pack(pady=10, padx=10)
#endregion

app.mainloop()
