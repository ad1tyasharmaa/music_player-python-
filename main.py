import tkinter as tk
import fnmatch
import os
from pygame import mixer
from PIL import Image, ImageTk

canvas = tk.Tk() 
canvas.title("Music Player") 
canvas.geometry("600x800") 
canvas.config(bg='black')

rootpath = "C:/Users/24adi/musicc"
pattern = "*.mp3"

mixer.init()

# Function to load and resize images
def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load and resize images
prev_img = load_image("prev.png", (50, 50))
stop_img = load_image("stop.png", (50, 50))
play_img = load_image("play.png", (50, 50))
pause_img = load_image("pause.png", (50, 50))
next_img = load_image("next.png", (50, 50))

def select():
    label.config(text= listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor" ))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0]+1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0]-1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song) 

def pause_song():
    if pauseButton["text"]== "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"   

frame = tk.Frame(canvas, bg='black')
frame.pack(padx=15, pady=15)

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listBox = tk.Listbox(frame, fg="maroon", bg="black", width=80, font=('DS-DIGITAL', 14), yscrollcommand=scrollbar.set)
listBox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listBox.yview)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('DS-DIGITAL', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command = play_prev)
prevButton.pack(pady=1, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command= stop)
stopButton.pack(pady=1, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=0, command = select)
playButton.pack(pady=1, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg='black', borderwidth=0, command = pause_song)
pauseButton.pack(pady=1, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth=0, command = play_next)
nextButton.pack(pady=1, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        file_path = os.path.join(root, filename)
        listBox.insert('end', filename)

canvas.mainloop()

