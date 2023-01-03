import jpg2png, png2ico ,_docx2pdf, _pdf2docx
from tkinter import *
from tkinter import messagebox
import webbrowser as web

root = Tk()
root.geometry("380x300")
root.configure(bg="#005b96")
root.title("Main Menu - Cyber Worm")
root.iconbitmap("C:/Python/logo.ico")
url = "https://blog-cyberworm.com"

def main(func):
    def contact():
        web.open(url)

    def convertJPG_PNG():
        jpg2png.select_file()

    def convertPNG_ICO():
        png2ico.select_file()
    
    def convertDOCX_PDF():
        _docx2pdf.select_file()
    
    def convertPDF_DOCX():
        _pdf2docx.select_file()

    if func == "convertJPG_PNG":
        return convertJPG_PNG
    elif func == "convertPNG_ICO":
        return convertPNG_ICO
    elif func == "convertDOCX_PDF":
        return convertDOCX_PDF
    elif func == "convertPDF_DOCX":
        return convertPDF_DOCX
    elif func == "contact":
        return contact
    else:
        messagebox.showerror("From Cyber Worm", "There is no selection.")
        root.quit()
    

#description = Label(root, text="Contact: https://blog-cyberworm.com", bg="#005b96", fg="#c1f9ff", padx=10, pady=10, font=("Arial", 16)).pack(side="top")
buttonContact = Button(root, text=f"Click to Contact.\n{url}", width=25, height=2, bg="#831e1a", fg="#ffffff", command=main("contact"))
buttonContact.place(relx=0.26)


frame_jpg_png = LabelFrame(root, text="JPG to PNG", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.09, rely=0.25)
frame_png_ico = LabelFrame(root, text="PNG to ICO", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.09, rely=0.6)
frame_docx_pdf = LabelFrame(root, text="DOCX to PDF", width=140, height=75 ,bg="#005b96", fg="#fefbf0").place(relx=0.56, rely=0.25)
frame_pdf_docx = LabelFrame(root, text="PDF to DOCX", width=140, height=75, bg="#005b96", fg="#fefbf0").place(relx=0.56, rely=0.6)
##########################################################################################################################################
button_jpg_png = Button(frame_jpg_png, text="Select file.", width=13, height=2, bg="#00b0ff", fg="#282102", command=main("convertJPG_PNG"))
button_jpg_png.place(relx=0.14, rely=0.33)

button_png_ico = Button(frame_png_ico, text="Select file.", width=13, height=2, bg="#00b0ff", fg="#282102", command=main("convertPNG_ICO"))
button_png_ico.place(relx=0.14, rely=0.68)
##########################################################################################################################################
button_docx_pdf = Button(frame_docx_pdf, text="Select file.", width=13, height=2, bg="#00b0ff", fg="#282102", command=main("convertDOCX_PDF"))
button_docx_pdf.place(relx=0.615, rely=0.33)

button_pdf_docx = Button(frame_pdf_docx, text="Select file.", width=13, height=2, bg="#00b0ff", fg="#282102", command=main("convertPDF_DOCX"))
button_pdf_docx.place(relx=0.615, rely=0.68)
##########################################################################################################################################


root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except TypeError:
        pass
