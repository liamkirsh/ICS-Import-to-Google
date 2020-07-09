import subprocess
import sys
import tkinter
from tkinter import messagebox

def show_error(msg):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("Error", msg)

def show_info(msg):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Info", msg)

if len(sys.argv) < 2:
    show_error("Missing filename")
    sys.exit(1)

retval = subprocess.call(
        ["C:\\Users\\Liam\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\gcalcli.exe",
         "import",
         sys.argv[1],
         "--calendar",
         'Liam K.']
)
if retval == 0:
    show_info("Successful import")
else:
    show_error("Import failed")
