from tkinter import Tk, Frame, Label, Entry, Button, Text, Scrollbar, StringVar, IntVar
import tkinter

# Creación de la raiz y el frame principal
root = Tk()
fr_principal = Frame(root, bg = "white")

# Variables de Control
nombre = StringVar()
apellido = StringVar()
edad = IntVar()

# Función asociada al boton btn_enviar
def enviar_datos():

    nombre.set("Guillermo")
    apellido.set("Rivera Reyes")
    edad.set(20)

# Creación de Frames Secundarios
fr_top = Frame(fr_principal, bg = "white")
fr_bottom = Frame(fr_principal, bg = "white")
fr_text = Frame(fr_bottom, borderwidth = 1, relief = "sunken")

# Creación de Labels
lbl_nombre = Label(fr_top, text = "Nombre: ", bg = "white")
lbl_apellido = Label(fr_top, text = "Apellidos: ", bg = "white")
lbl_edad = Label(fr_top, text = "Edad: ", bg = "white")
lbl_comentario = Label(fr_bottom, text = "Comentarios: ", bg = "white")

# Creación de Entrys
entry_nombre = Entry(fr_top, textvariable = nombre)
entry_apellido = Entry(fr_top, textvariable = apellido)
entry_edad = Entry(fr_top, textvariable = edad)

# Creación de Button
btn_enviar = Button(fr_bottom, text = "Enviar", fg = "white", bg = "dark blue", command = enviar_datos)

# Creación del Text y Scrollbar
txt_comentario = Text(fr_text, width = 15, height = 6, wrap = tkinter.NONE)
scrollx = Scrollbar(fr_text, orient = "horizontal", command = txt_comentario.xview)
scrolly = Scrollbar(fr_text, orient = "vertical", command = txt_comentario.yview)

# Configurando el Text
txt_comentario.config(xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

# Colocando Labels
lbl_nombre.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "e")
lbl_apellido.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "e")
lbl_edad.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "e")
lbl_comentario.pack(side = "left", fill = "both", expand = True, padx = 10, pady = 10)

# Colocando Entry
entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10)
entry_apellido.grid(row = 1, column = 1, padx = 10, pady = 10)
entry_edad.grid(row = 2, column = 1, padx = 10, pady = 10)

# Colocando el Text y los Scrollbar
txt_comentario.grid(row = 0, column = 0, sticky = "nsew")
scrolly.grid(row = 0, column = 1, sticky = "ns")
scrollx.grid(row = 1, column = 0, sticky = "ew")

# Colocando el Button
btn_enviar.pack(side = "bottom", padx = 10, pady = 10)
btn_enviar.config(relief = "flat")

fr_text.grid_rowconfigure(0, weight=1)
fr_text.grid_columnconfigure(0, weight=1)

# Colocando Frames
fr_top.pack(side = "top")
fr_bottom.pack(side = "bottom")
fr_text.pack(side = "right")
fr_principal.pack(fill = "both", expand = True)

# Configurando la raiz
root.title("Prueba Scrollbar")
root.mainloop()
