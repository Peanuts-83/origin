from tkinter import *

# beginning the window
root = Tk()
root.geometry('720x480')

radio_var = StringVar()
radio_var.set('Male')
def grab_selection():
    print(radio_var.get())

r1 = Radiobutton(root, text='Male', font=('', 24), variable=radio_var,
                value='Male', command=grab_selection)
r1.pack(anchor=W) # W,E,N,S
r2 = Radiobutton(root, text='Female', font=('', 24), variable=radio_var,
                value='Female', command=grab_selection)
r2.pack(anchor=W) # W,E,N,S
r3 = Radiobutton(root, text='Other', font=('', 24), variable=radio_var,
                value='Other', command=grab_selection)
r3.pack(anchor=W) # W,E,N,S



root.mainloop()
# ending the window