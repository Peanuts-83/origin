from tkinter import *

# beginning the window
root = Tk()
root.geometry('720x480')

entry1_var = StringVar() # ou IntVar() ou DoubleVar() > float!
entry1 = Entry(root, font=('', 24), textvariable=entry1_var)
entry1.pack()
button1 = Button(root, text='Grab info')
button1.pack(side=BOTTOM, fill=X)

def grab_info():
    print(entry1_var.get())
button1.configure(command=grab_info)



root.mainloop()
# ending the window