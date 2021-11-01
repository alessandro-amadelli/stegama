"""
Script with the main GUI of the steganography application.

Author: Ama
"""

from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

from PIL import ImageTk, Image

from stegano import lsbset
from stegano.lsbset import generators

def Encode():
    img_chosen = ChooseImage("Choose an image to hide your secret text")
    if not img_chosen:
        return False
    img_file = ImgPathLabel["text"]
    secret_text = inp_text.get("1.0", END)

    if secret_text == "" or inp_text.compare("end-1c", "==", "1.0"):
        messagebox.showwarning("Empty text!", f"Insert a text in the text field...")
        return True

    out_image = "./secret_image.png"
    secret = lsbset.hide(img_file, secret_text, generators.eratosthenes())
    secret.save(out_image)

    #Text is cleared from the input field
    ClearText()

    messagebox.showinfo("Encoded", f"Secret text encoded in image: {out_image}")

def Decode():
    img_chosen = ChooseImage("Choose an image to reveal the secret text")
    if not img_chosen:
        return False
    img_file = ImgPathLabel["text"]
    decoded_text = lsbset.reveal(img_file, generators.eratosthenes())

    inp_text.delete("1.0", END)
    inp_text.insert("1.0", decoded_text)

    messagebox.showinfo("Decode", f"Secret text extracted from image")

def ChooseImage(title):
    #Allowed file types
    file_types = (
        ('PNG image', '*.PNG'),
        ('JPEG image', '*.JPEG'),
        ('JPG image', '*.JPG')
    )
    try:
        file_name = askopenfilename(parent=Screen, title=title,
        filetypes=file_types)
    except:
        messagebox.showerror("Error", f"Error opening image file.")
        return False
    ImgPathLabel["text"] = file_name

    return True

def ClearText():
    inp_text.delete("1.0", END)

#Initializing GUI screen
Screen = Tk()
Screen.title("Steganography python tool")
Screen.geometry("500x500")
Screen.resizable(False, False)
Screen.config(bg="#d3d3d3")

#Creating encode button
EncodeBtn = Button(text="Encode", command=Encode)
EncodeBtn.place(relx=0.1, rely=0.1)

#Label containing the path of the source image
ImgPathLabel = Label(Screen, width=60, anchor=W, text="")
ImgPathLabel.place(relx=0.1, rely=0.2)

#Creating frame to place textbox
frame = Frame(Screen)

#Textbox for input text
inp_text = Text(frame, width=35, height=10, wrap='word')
inp_text.pack(expand=True, side=LEFT)

#Scrollbar for the textbox
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
inp_text.config(yscrollcommand=sb.set)
sb.config(command=inp_text.yview)

frame.pack(expand=True)

DecodeBtn = Button(text="Decode", command=Decode)
DecodeBtn.place(relx=0.8, rely=0.1)

#Button to clear text
ClearButton = Button(text="Clear", command=ClearText)
ClearButton.place(relx=0.1, rely=0.6)

#Button to quit
QuitButton = Button(text="Quit application", command=Screen.destroy)
QuitButton.place(relx=0.1, rely=0.8)

#main tkinter event loop
mainloop()
