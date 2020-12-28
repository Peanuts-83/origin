from tkinter import *
from style import *
import os; os.chdir('Tkinter/music_player')
import random, time

def get_music_files():
    files = os.listdir('files')
    return files

def run_music():
    while True:
        music_files = get_music_files()
        choosen_file = random.choice(music_files)
        os.startfile(os.path.join(os.curdir, 'files', choosen_file))
        print(choosen_file)
        time.sleep(30)

root = Tk() # creates a window
root.configure(bg=blue)
root.geometry('480x320')

title = Label(root, text='Music Player', 
                fg=yellow, bg=blue,
                font=(font_type, 36)
            )
title.pack()

sub_title =Label(root, text='Click the button to start playing music',
                fg=yellow, bg=blue,
                font=(font_type, 15)
            )
sub_title.pack()

play_button = Button(root, text='Push me!', 
                command=run_music,
                fg=yellow, bg=blue,
                font=(font_type, 21)
            )
play_button.pack(side=BOTTOM)



root.mainloop() # loops the window until we close!

