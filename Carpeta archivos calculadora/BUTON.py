import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
def Formas():
    control_subventanas = Tk()
    control_subventanas.title("Prueba")
    control_subventanas.config(bg="blue")
    subven_1 = Frame(control_subventanas)
    subven_1.pack(fill='y', expand=0)
    fondo = Image.open('formulas.png')
    fondo = fondo.resize((300, 400), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo = ImageTk.PhotoImage(fondo)
    subven_1_label = Label(subven_1, image=fondo)
    subven_1_label.place(x=0, y=0)
    subven_1.config(width="300", height="400", bg="Grey")
    control_subventanas.mainloop()
Formas()

subven_1 = Frame(control_subventanas)
subven_1.pack(fill='y', expand=0)
fondo = Image.open('formulas.png')
fondo = fondo.resize((300, 400), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
fondo = ImageTk.PhotoImage(fondo)
subven_1_label = Label(subven_1, image=fondo)
subven_1_label.place(x=0, y=0)