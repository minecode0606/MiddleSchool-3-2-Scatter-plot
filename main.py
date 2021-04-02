#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")
win.geometry("640x480")
win.resizable(False, False)
# Modify adding a Label
a_label = ttk.Label(win, text="주어진 데이터 세트를 입력하세요 :")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me():
    global dataset
    dataset = name.get()
    print(dataset)


# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=1, row=0)

# Adding a Button
action = ttk.Button(win, text="입력", command=click_me)
action.grid(column=2, row=0)

#======================
# Start GUI
#======================
win.mainloop()