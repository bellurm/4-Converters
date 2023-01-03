from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image

def png_to_ico(png_file, ico_file):
    with Image.open(png_file) as image:
        image.save(ico_file, "ico")

def select_file():
    try:
        png_file = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = [("PNG files", "*.png")])
        ico_file = os.path.splitext(png_file)[0] + ".ico"
        png_to_ico(png_file, ico_file)
        messagebox.showinfo("From Cyber Worm", "Converted successfully!\nThe file is in the same location.")
    except:
        messagebox.showerror("From Cyber Worm", "You've not selected a file.")
