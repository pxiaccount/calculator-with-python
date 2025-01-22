from tkinter import *
import math

root = Tk()
root.title("Calculator")
display_frame = Frame(root)
display_frame.grid(column=0, row=0, columnspan=4, sticky="we")

display_text = StringVar()
display_text.set("0")

display_ui = Label(display_frame, textvariable=display_text, height=2, width=10, relief="sunken", anchor="e")
display_ui.pack(fill="x")

operator_text = "+-*/%"
dot = True

buttons = [
    ("C", 1, 0), ("←", 1, 1), ("√x²", 1, 2), ("+", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("/", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("%", 5, 2), ("=", 5, 3),
]

def update(x):
    current = display_text.get()
    
    if current == "0":
        display_text.set(x)
    else:
        display_text.set(current+x)

def operation(x):
    global dot
    dot = True
    current = display_text.get()
    
    if current[-1] != x and current[-1] not in operator_text:
        display_text.set(current+x)

def delete():
    current = display_text.get()
    
    if current == "0":
        return 0
    else:
        display_text.set(current[:-1])

def evaluation():
    current = display_text.get()
    
    result = eval(current)
    # print(result)
    display_text.set(result)

def clear():
    global dot
    display_text.set("0")
    dot = True

def add_root():
    current = display_text.get()
    
    result = math.sqrt(float(current))
    # print(result)
    display_text.set(result)

def add_dot():
    global dot
    current = display_text.get()
    
    if current[-1:] not in "." and dot:
        display_text.set(current + ".")
        dot = False
    else:
        display_text.set(current)

for (text, row, column) in buttons:
    if text in operator_text:
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), operation(t))).grid(row=row, column=column)
    elif text == "←":
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), delete())).grid(row=row, column=column)
    elif text == "=":
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), evaluation())).grid(row=row, column=column)
    elif text == "C":
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), clear())).grid(row=row, column=column)
    elif text == "√x²":
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), add_root())).grid(row=row, column=column)
    elif text == ".":
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), add_dot())).grid(row=row, column=column)
    else:
        Button(root, text=text, width=3, height=2, command= lambda t=text: (print(t), update(t))).grid(row=row, column=column)


root.mainloop()