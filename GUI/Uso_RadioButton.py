from tkinter import Tk, Radiobutton, Label, IntVar, Button

root = Tk()
root.title("Uso de radio Buton")

# ---------------- Variables de control ---------------
opcion = IntVar()


# Funcion
def get_genero():

    if opcion.get() == 1:
        lbl_msj["text"] = "Has eleigido: Masculino"
    else:
        lbl_msj["text"] = "Has elegido: Femenino"

# ------------------------- Creacion de widgets ------------------------------------
lbl_genero = Label(root, text = "Género:", justify = "left")
lbl_genero.config(bg = "White", font = ("Century Schoolbook", 14, "bold italic"))

lbl_msj = Label(root, text = "", justify = "center", bg = "White")
lbl_msj.config(fg = "dark blue", font = ("Century Schoolbook", 10, "bold italic"))

rdBtn_masculino = Radiobutton(root, text = "Masculino", variable = opcion, value = 1, command = get_genero)
rdBtn_masculino.configure(bg = "White", font = ("Century Schoolbook", 12, "bold italic"))

rdBtn_femenino = Radiobutton(root, text = "Femenino", variable = opcion, value = 2, command = get_genero)
rdBtn_femenino.configure(bg = "White", font = ("Century Schoolbook", 12, "bold italic"))

lbl_genero.pack(padx = 15, pady = 10)
rdBtn_masculino.pack(padx = 15, pady = 5)
rdBtn_femenino.pack(padx = 15, pady = 5)
lbl_msj.pack(side = "bottom", padx = 15, pady = 15)

root.config(bg = "White")
root.geometry("300x250")
root.mainloop()