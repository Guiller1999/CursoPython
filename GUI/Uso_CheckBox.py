from tkinter import Tk, Label, Checkbutton, PhotoImage, StringVar, IntVar

root = Tk()
root.title("Uso de CheckButton")

# Variables de control
travel_beach = IntVar()
travel_mountain = IntVar()
travel_rural = IntVar()

# Funcion que permite visualizar en un label la opcion seleccionada en 
# un Radiobutton
def travel_options():

    option = ""
    if travel_beach.get() == 1:
        option += " Playa"
    if travel_mountain.get() == 1:
        option += " Montaña"
    if travel_rural.get() == 1:
        option += " Turismo rural"
    
    lbl_msg.config(text = option)

# ------------------------------- Creando widgets --------------------------------

# Creando Labels de la parte superior de la interfaz
img = PhotoImage(file = "Img\\avion.gif")
lbl_image = Label(root, image = img, width = 150, height = 100, bg = "White")

lbl_instruction = Label(root, text = "Elige destinos: ", bg = "White", fg = "dark blue")
lbl_instruction.config(font = ("Century Schoolbook", 11, "bold italic"), justify = "left")

# Creando Checkbutton
chk_btnBeach = Checkbutton(
    root,
    text = "Playa", 
    bg = "White",
    variable = travel_beach,
    onvalue = 1,
    offvalue = 0, 
    command = travel_options)
chk_btnBeach.config(font = ("Century Schoolbook", 11, "bold italic"))

chk_btnMontain = Checkbutton(
    root, text = "Montaña", 
    bg = "White", 
    variable = travel_mountain,
    onvalue = 1,
    offvalue = 0,
    command = travel_options)
chk_btnMontain.config(font = ("Century Schoolbook", 11, "bold italic"))

chk_btnRural = Checkbutton(
    root, text = "Turismo Rural", 
    bg = "White",
    variable = travel_rural,
    onvalue = 1,
    offvalue = 0,
    command = travel_options)
chk_btnRural.config(font = ("Century Schoolbook", 11, "bold italic"))

# Creando Label
lbl_msg = Label(root, text = "", bg = "White", fg = "dark blue")
lbl_msg.config(font = ("Century Schoolbook", 11, "bold italic"))

# -------------------- Colocando widgets -----------------------
lbl_image.pack(padx = 10, pady = 20)
lbl_instruction.pack(padx = 10, pady = 5)
chk_btnBeach.pack(pady = 5) 
chk_btnMontain.pack(pady = 5)
chk_btnRural.pack(pady = 5)
lbl_msg.pack(side = "bottom", pady = 10)

# Configurando la raiz
root.config(bg = "White")
root.geometry("400x350")
root.mainloop()