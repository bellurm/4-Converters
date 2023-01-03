from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image

def jpg_to_png(jpg_file, png_file):
    with Image.open(jpg_file) as image:
        image.save(png_file)

def select_file():
    try:
        jpg_file = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = [("JPG files", "*.jpg")])
        png_file = os.path.splitext(jpg_file)[0] + ".png"
        jpg_to_png(jpg_file, png_file)
        messagebox.showinfo("From Cyber Worm", "Converted successfully!\nThe file is in the same location.")
    except AttributeError:
        messagebox.showerror("From Cyber Worm", "You've not selected a file.")
