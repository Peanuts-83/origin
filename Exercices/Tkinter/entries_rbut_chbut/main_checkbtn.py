from tkinter import *

# beginning the window
root = Tk()
root.geometry('720x480')

# user interface:
options = ['Videos', 'Music', 'Docs', 'Pictures', 'Sheets']
check_buttons = []
for option in options:
    check_btn_var = IntVar()
    check_btn = Checkbutton(root, text=option, font=('', 24),
                             variable=check_btn_var, onvalue=1, offvalue=0)
    check_btn.pack(anchor=W)
    check_buttons.append((check_btn, check_btn_var))

btn_info = Button(root, text='Grab info', font=('', 24))
btn_info.pack(side=BOTTOM, fill=X)

# Functionality:
def grab_check_btn_status():
    for check_btn, check_btn_var in check_buttons:
        print(check_btn.cget('text'), check_btn_var.get())
btn_info.configure(command=grab_check_btn_status)


root.mainloop()
# ending the window