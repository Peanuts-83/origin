from tkinter import *
from style import *
import math, re

# pack - Place the widget at the nearest position (side=TOP/BOTTOM/LEFT/RIGHT)
# grid - Grids the widget to (column=, row=) pos
# place - Locates the widget at the given (x=, y=)point


# beginning the window
root = Tk()
# button2 = Button(root, text='Click me2!')
# button2.grid(column=0, row=1)
# button1 = Button(root, text='Click me1!')
# button1.place(x=30, y=50)
# root.geometry('740x480')
# frame1 = Frame(root, bg='red')
# frame1.pack(side=LEFT, expand=YES, fill=BOTH)
# button1 = Button(frame1, text='Click me!')
# button1.pack()

# user interface:
root.geometry('720x480')
numbers_frame = Frame(root, bg='black')
numbers_frame.pack(side=LEFT, expand=YES, fill=BOTH)
results_frame = Frame(root, bg='grey')
results_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

result_screen = Label(results_frame, text='', **result_screen_style)
result_screen.pack(side=TOP)
name = Label(results_frame, text='Calculator 8000 fx/4G-Py', **name_style)
name.pack(side=TOP)

numbers = list(range(1, 10))
for num in numbers:
    btn_num = Button(numbers_frame, text=num, **btn_style)
    if num%3 != 0:
        btn_num.grid(column=num%3, row=math.ceil(num/3))
    else:
        btn_num.grid(column=3, row=math.ceil(num/3))
btn_num0 = Button(numbers_frame, text=0, **btn_style)
btn_num0.grid(column=2, row=4)
btn_clean = Button(numbers_frame, text='C', **btn_style)
btn_clean.grid(column=1, row=4)
btn_equals = Button(numbers_frame, text='=', **btn_style)
btn_equals.grid(column=3, row=4)

btn_plus = Button(numbers_frame, text='+', **btn_style)
btn_plus.grid(column=4, row=1)
btn_minus = Button(numbers_frame, text='-', **btn_style)
btn_minus.grid(column=4, row=2)
btn_multiply = Button(numbers_frame, text='*', **btn_style)
btn_multiply.grid(column=4, row=3)
btn_divide = Button(numbers_frame, text='/', **btn_style)
btn_divide.grid(column=4, row=4)

# functionality:
def update_result_screen(clicked_btn):
    current_text = str(result_screen.cget('text'))
    updated_text = current_text + str(clicked_btn.cget('text'))
    result_screen.configure(text=updated_text)

# print(numbers_frame.winfo_children())
for widget in numbers_frame.winfo_children():
    widget_text = widget.cget('text')
    if type(widget_text) == int or widget_text in ['+', '-', '*', '/']:
        widget.configure(command= lambda widget=widget: update_result_screen(widget))

def clean_screen():
    result_screen.configure(text='')
btn_clean.configure(command=clean_screen)

def equals():
    screen_text = result_screen.cget('text')
    if len(re.findall("[-+*/]", screen_text)) > 0:
        operator = re.findall("[-+*/]", screen_text)[0]
        first_num, second_num = screen_text.split(operator)
        result = round(eval(first_num + operator + second_num),3)
    result_screen.configure(text=result)
btn_equals.configure(command=equals)


root.mainloop()
# ending the window