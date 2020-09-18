from tkinter import Tk, Frame, Label, PhotoImage

# Creacion de Raíz, Frame y Label
root = Tk()
frame = Frame(root, width = "500", height = "400")
label1 = Label(frame, text = "Hola Mundo!!")

# Configurando Raiz
root.iconbitmap("Img\\aprobar.ico")
root.title("Uso Label")

img = PhotoImage(file = "Img\\EnConstruccion.png")

# Configurando Label
label1.config(bg = "White", image = img)
label1.place(x = 100, y = 200)

""" Sintaxis alterna:

    Label(frame, text = "Hola").place(x = 100, y = 200)
"""

# Configurando el Frame
frame.config(bg = "White")
frame.pack(fill = "both", expand = "True")

root.mainloop()
