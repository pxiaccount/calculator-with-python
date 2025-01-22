from tkinter import *
import math

root = Tk()
root.title("Calculator")
display_frame = Frame(root)
display_frame.grid(column=0, row=0, columnspan=5, sticky="we")
# root.geometry("292x465")


display_text = StringVar()
display_text.set("0")

display_ui = Label(display_frame, textvariable=display_text, height=2, width=10, relief="sunken", anchor="e", bg="#d8f0d8")
display_ui.pack(fill="x")

operator_text = "+-*/%"
dot = True

root.resizable(False, False)

buttons = [
    ("C", 1, 0), ("←", 1, 1), ("x²", 1, 2), ("+", 1, 3), ("π", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3), ("√x²", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("√x³", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("/", 4, 3), ("%", 4, 4),
    ("0", 5, 0), ("(", 5, 1), (")", 5, 2), (".", 5, 3), ("=", 5, 4),
]

def update(x):
    current = display_text.get()
    
    if current == "0":
        display_text.set(x)
    elif current == "Error Divided By Zero":
        display_text.set("0")
    else:
        display_text.set(current+x)

def operation(x):
    global dot
    dot = True
    current = display_text.get()
    
    if current[-1] != x and current[-1] not in operator_text:
        if current == "Error Divided By Zero":
            display_text.set("0")
        else:
            display_text.set(current+x)

def delete():
    current = display_text.get()
    
    if current == "0":
        return 0
    else:
        if current == "Error Divided By Zero":
            display_text.set("0")
        else:
            display_text.set(current[:-1])

def evaluation():
    current = display_text.get()
    
    try:
        result = float(eval(current))
    except ZeroDivisionError:
        result = "Error Divided By Zero"
    except ValueError:
        result = "Error"
    
    # print(result)
    
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    display_text.set(result)

def clear():
    global dot
    display_text.set("0")
    dot = True

def add_root():
    global dot
    dot = False
    current = display_text.get()
    
    try:
        result = math.sqrt(float(current))
    except ValueError:
        result = current
    # print(result)
    
    display_text.set(result)

def add_3_root():
    global dot
    dot = False
    current = display_text.get()
    
    try:
        result = math.cbrt(float(current))
    except ValueError:
        result = current
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

def bind(x):
    key = x.char
    if key.isdigit():
        update(key)
    elif key in operator_text:
        operation(key)
    elif key == "C" or key == "c":
        clear()
    elif key == "=" or x.keysym == "KP_Enter" or x.keysym == "Return":
        evaluation()
    elif key == ".":
        add_dot()
    elif key == "(":
        update("(")
    elif key == ")":
        update(")")

def square():
    current = display_text.get()

    display_text.set(float(current)**2)

def add_pi():
    current = display_text.get()

    if current == "0":
        display_text.set(str(math.pi))
    elif current[-1:] in "01234567989.":
        display_text.set(current+"*"+str(math.pi))
    else:
        display_text.set(current+str(math.pi))

root.bind("<BackSpace>", lambda event: delete())
root.bind("<Key>", bind)

for (text, row, column) in buttons:
    if text in operator_text:
        Button(root, bg="#abe0ff", text=text, width=9, height=5, command= lambda t=text: (print(t), operation(t))).grid(row=row, column=column)
    elif text == "←":
        Button(root, bg="#ffdcab", text=text, width=9, height=5, command= lambda t=text: (print(t), delete())).grid(row=row, column=column)
    elif text == "=":
        Button(root, bg="#b6abff", text=text, width=9, height=5, command= lambda t=text: (print(t), evaluation())).grid(row=row, column=column)
    elif text == "C":
        Button(root, bg="#ffabab", text=text, width=9, height=5, command= lambda t=text: (print(t), clear())).grid(row=row, column=column)
    elif text == "√x²":
        Button(root, bg="#f799f6", text=text, width=9, height=5, command= lambda t=text: (print(t), add_root())).grid(row=row, column=column)
    elif text == "x²":
        Button(root, bg="#ffdcab", text=text, width=9, height=5, command= lambda t=text: (print(t), square())).grid(row=row, column=column)
    elif text == "√x³":
        Button(root, bg="#f799f6", text=text, width=9, height=5, command= lambda t=text: (print(t), add_3_root())).grid(row=row, column=column)
    elif text == ".":
        Button(root, bg="#abe0ff", text=text, width=9, height=5, command= lambda t=text: (print(t), add_dot())).grid(row=row, column=column)
    elif text == "π":
        Button(root, bg="#f799f6", text=text, width=9, height=5, command= lambda t=text: (print(t), add_pi())).grid(row=row, column=column)
    else:
        Button(root, bg="#abffac", text=text, width=9, height=5, command= lambda t=text: (print(t), update(t))).grid(row=row, column=column)


root.mainloop()