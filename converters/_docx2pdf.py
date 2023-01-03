from tkinter import filedialog
from tkinter import messagebox
import os
from docx2pdf import convert

def select_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = [("docx files", "*.docx")])
    location = r""
    convert(file_path, location)
    if file_path == "":
        messagebox.showerror("From Cyber Worm", "You've not selected a file.")
        
    else:
        messagebox.showinfo("From Cyber Worm", "Converted successfully!\nThe file is in the same location.")
