from tkinter import filedialog
from tkinter import messagebox
import os
from pdf2docx import Converter

def select_file():
    try:
        pdf_file = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = [("PDF files", "*.pdf")])
        docx_file = os.path.splitext(pdf_file)[0] + ".docx"
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        messagebox.showinfo("From Cyber Worm", "Converted successfully!\nThe file is in the same location.")
    except:
        messagebox.showerror("From Cyber Worm", "You've not selected a file.")
