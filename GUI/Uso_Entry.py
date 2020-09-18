from tkinter import Tk, Frame, Entry, Label, Text, Scrollbar, Button, StringVar
import tkinter

# Creación de la raiz y el frame
root = Tk()
frame = Frame(root, width = 500, height = 450)

# Variable de control
nom = StringVar()

def click_Envio():
    nom.set("Guillermo")


# Creación de widgets
entry_nombre = Entry(frame, textvariable = nom)
entry_apellido = Entry(frame)
entry_contraseña = Entry(frame)
entry_direccion = Entry(frame)
lbl_nombre = Label(frame, text = "Nombre: ")
lbl_apellido = Label(frame, text = "Apellido: ")
lbl_contraseña = Label(frame, text = "Contraseña: ")
lbl_direccion = Label(frame, text = "Dirección: ")
lbl_comentario = Label(frame, text = "Comentarios:")
txt_comentario = Text(frame, width = 15, height = 5)
scroll_vert = Scrollbar(frame, command = txt_comentario.yview)
btn_envio = Button(frame, text = "Enviar", command = click_Envio)

txt_comentario.config(yscrollcommand = scroll_vert.set)

# Configuración del frame
frame.pack()

# Configuración de los widgets
lbl_nombre.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)
lbl_apellido.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)
lbl_contraseña.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)
lbl_direccion.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)
lbl_comentario.grid(row = 4, column = 0, sticky = "e", pady = 10)
entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10)
entry_apellido.grid(row = 1, column = 1, padx = 10, pady = 10)
entry_contraseña.grid(row = 2, column = 1, padx = 10, pady = 10)
entry_direccion.grid(row = 3, column = 1, padx = 10, pady = 10)
txt_comentario.grid(row = 4, column = 1, padx = 10, pady = 10)
scroll_vert.grid(row = 4, column = 1, pady = 10, sticky = "nse")

btn_envio.grid(row = 6, column = 1, pady = 15, sticky = "s")

entry_contraseña.config(show = "*")

root.mainloop()


    