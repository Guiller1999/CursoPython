from tkinter import Tk, Frame, Entry, Button, StringVar


root = Tk()
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)

# Variables de control
num = StringVar()

# Función de pulso de botones
def numero_pulsado(boton):

    num.set(num.get() + boton)

fr_north = Frame(root, bg = "White")
fr_south = Frame(root, bg = "White")


# Configuracion de frames
fr_north.grid(row = 0, column = 0, sticky = "nswe")
fr_north.grid_rowconfigure(0, weight = 1)
fr_north.grid_columnconfigure(0, weight = 1)

fr_south.grid(row = 1, column = 0, sticky = "nswe")
fr_south.grid_rowconfigure(0, weight = 1)
fr_south.grid_rowconfigure(1, weight = 1)
fr_south.grid_rowconfigure(2, weight = 1)
fr_south.grid_rowconfigure(3, weight = 1)
fr_south.grid_columnconfigure(0, weight = 1)
fr_south.grid_columnconfigure(1, weight = 1)
fr_south.grid_columnconfigure(2, weight = 1)
fr_south.grid_columnconfigure(3, weight = 1)

#-------------------- Pantalla ------------------------
entry_pantalla = Entry(fr_north, textvariable = num)
entry_pantalla.grid(row = 0, column = 0, sticky = "nswe", pady = 10, padx = 10)
"""relief = "solid", borderwidth = 2, """
entry_pantalla.config(relief = "flat", justify = "right", font = ("Helvetica", 16, "bold italic"))
entry_pantalla.rowconfigure(0, weight = 1)
entry_pantalla.columnconfigure(0, weight = 1)

#-------------------- Botones -------------------------

# Creando widgets
#---------- Fila 1 ---------------
btn_7 = Button(fr_south, text = "7", width = 5, height = 2, command = lambda:numero_pulsado("7"))
btn_8 = Button(fr_south, text = "8", width = 5, height = 2, command = lambda:numero_pulsado("8"))
btn_9 = Button(fr_south, text = "9", width = 5, height = 2, command = lambda:numero_pulsado("9"))
btn_dividir = Button(fr_south, text = "/", width = 5, height = 2)

#---------- Fila 2 ---------------
btn_4 = Button(fr_south, text = "4", width = 5, height = 2, command = lambda:numero_pulsado("4"))
btn_5 = Button(fr_south, text = "5", width = 5, height = 2, command = lambda:numero_pulsado("5"))
btn_6 = Button(fr_south, text = "6", width = 5, height = 2, command = lambda:numero_pulsado("6"))
btn_x = Button(fr_south, text = "x", width = 5, height = 2)

#---------- Fila 3 ---------------
btn_3 = Button(fr_south, text = "3", width = 5, height = 2, command = lambda:numero_pulsado("3"))
btn_2 = Button(fr_south, text = "2", width = 5, height = 2, command = lambda:numero_pulsado("2"))
btn_1 = Button(fr_south, text = "1", width = 5, height = 2, command = lambda:numero_pulsado("1"))
btn_resta = Button(fr_south, text = "-", width = 5, height = 2)

#---------- Fila 4 ---------------
btn_pt = Button(fr_south, text = ".", width = 5, height = 2, command = lambda:numero_pulsado("."))
btn_0 = Button(fr_south, text = "0", width = 5, height = 2, command = lambda:numero_pulsado("0"))
btn_igual = Button(fr_south, text = "=", width = 5, height = 2, bg = "#5DADE2", fg = "Black")
btn_suma = Button(fr_south, text = "+", width = 5, height = 2)

# Configurando botones

#---------- Fila 1 ---------------
btn_7.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_8.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_9.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_dividir.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")

#---------- Fila 2 ---------------
btn_4.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_5.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_6.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_x.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")

#---------- Fila 3 ---------------
btn_3.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_2.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_1.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_resta.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")

#---------- Fila 4 ---------------
btn_pt.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_0.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_igual.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")
btn_suma.config(relief = "flat", borderwidth = 2, font = ("Helvetica", 16, "bold italic"), justify = "center")

# Colocando botones

#---------- Fila 1 ---------------
btn_7.grid(row = 0, column = 0, sticky = "nswe")
btn_8.grid(row = 0, column = 1, sticky = "nswe")
btn_9.grid(row = 0, column = 2, sticky = "nswe")
btn_dividir.grid(row = 0, column = 3, sticky = "nswe")

#---------- Fila 2 ---------------
btn_4.grid(row = 1, column = 0, sticky = "nswe")
btn_5.grid(row = 1, column = 1, sticky = "nswe")
btn_6.grid(row = 1, column = 2, sticky = "nswe")
btn_x.grid(row = 1, column = 3, sticky = "nswe")

#---------- Fila 3 ---------------
btn_3.grid(row = 2, column = 0, sticky = "nswe")
btn_2.grid(row = 2, column = 1, sticky = "nswe")
btn_1.grid(row = 2, column = 2, sticky = "nswe")
btn_resta.grid(row = 2, column = 3, sticky = "nswe")

#---------- Fila 4 ---------------
btn_pt.grid(row = 3, column = 0, sticky = "nswe")
btn_0.grid(row = 3, column = 1, sticky = "nswe")
btn_igual.grid(row = 3, column = 2, sticky = "nswe")
btn_suma.grid(row = 3, column = 3, sticky = "nswe")


root.title("Calculadora")
root.mainloop()