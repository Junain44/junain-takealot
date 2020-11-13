from tkinter import *
import pygame
import os


class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")

        pygame.init()

        pygame.mixer.init()

        self.track = StringVar()

        self.status = StringVar()

songframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="Navyblue", fg="white", bd=5,
                       relief=GROOVE)
songframe.place(x=0, y=0, width=600, height=100)
songframe = Label(songframe, textvariable=self.track, width=20,
                  font=("times new roman", 24, "bold"), bg="Orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
songstatus = Label(songframe, textvariable=self.track)

# CREATING BUTTON FRAME
buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5,
                         relief=GROOVE)
buttonframe.place(x=0, y=100, width=600, height=100)


# Defining Play Song Function
def playsong():
    # Displaying Selected Song title
    track.set(playlist.get(ACTIVE))

    # Displaying Status
    status.set("-Playing")

    # Loading Selected Song
    pygame.mixer.music.load(playlist.get(ACTIVE))

    # Playing Selected Song
    pygame.mixer.music.play()


def stopsong():
    # Displaying Status
    status.set("-STOPPED")
    # Stopped Song
    pygame.mixer.music.stop()


def pausesong():
    # Displaying Status
    self.status.set("-Paused")

    # Paused Song
    pygame.mixer.music.pause()


def unpausesong():
    # Displaying Status
    self.status.set("-Playing")

    # Playing back Song
    pygame.mixer.music.unpause()


# INSERTING PLAY BUTTON
playbtn = Button(buttonframe, text="PLAYSONG", command="playsong", width=10, height=1,
                 font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10, pady=5)
# INSERTING PAUSE BUTTON
pausebtn = Button(buttonframe, text="PAUSE", command="pausesong", width=8, height=1,
                  font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10, pady=5)
# INSERTING UNPAUSE BUTTON
unpausebtn = Button(buttonframe, text="UNPAUSE", command="unpausesong", width=8, height=1,
                    font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10,
                                                                                         pady=5)
# INSERTING STOP BUTTON
stopbtn = Button(buttonframe, text="STOPSONG", command="stopsong", width=8, height=1,
                 font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10, pady=5)

# CREATING PLAYLIST FRAME
songframe = LabelFrame(text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5,
                       relief=GROOVE)
songframe.place(x=600, y=0, width=400, height=200)

# Inserting scrollbar
scroll_y = Scrollbar(songframe, orient=VERTICAL)

# Inserting Playlist listbox
playlist = Listbox(songframe, yscrollcommand=scroll_y.set, selectbackground="gold", selectmode=SINGLE,
                   font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
# Applying Scrollbar to listbox
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)

# Changing Directory for fetching Songs
os.chdir("/home/user/PycharmProjects/Music-Player/music")

# Fetching Songs
songtracks = os.listdir()

# Inserting Songs into Playlist
for track in songtracks:
    playlist.insert(END, track)

root = Tk()
MusicPlayer(root)
root.mainloop()
