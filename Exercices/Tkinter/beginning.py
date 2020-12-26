from tkinter import *

def button_click():
    print('You clicked me!')

root = Tk() # creates a window
root.geometry('720x480') # widthxheight

title = Label(root, text='First Window', fg='#00ccFF', font=('', 32, 'bold'))
title.pack()


btn1 = Button(root, text='Click me!', command=button_click)
btn1.pack(side=TOP)
root.mainloop() # loops the window until we close!

