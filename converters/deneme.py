import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import pdf2docx

root = tk.Tk()
root.geometry("400x300")
root.configure(bg="#005b96")
root.title("PDF to DOCX")
root.iconbitmap("C:/Python/logo.ico")

def pdf_to_docx(pdf_file, docx_file):
    pdf2docx.convert(pdf_file, docx_file)

def select_file():
    pdf_file = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = [("PDF files", "*.pdf")])
    docx_file = os.path.splitext(pdf_file)[0] + ".docx"
    pdf_to_docx(pdf_file, docx_file)

button = tk.Button(root, text = "Select File", font=20,
        padx = 50, pady = 30, bg = "black", fg = "#005b96", command = select_file).place(relx=0.25, rely=0.3)

root.mainloop()
