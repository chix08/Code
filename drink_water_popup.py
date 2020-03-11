import tkinter
from tkinter import messagebox
import sys
import os

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
root = tkinter.Tk()
root.withdraw()
messagebox.showerror("Message", "Drink Water")

