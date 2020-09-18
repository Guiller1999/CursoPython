from tkinter import Tk
from interfaz.Interfaz import Calculadora

root = Tk()
fr_pr = Calculadora(master = root)
fr_pr.pack(fill = "both", expand = True)

root.title("Calculadora")
root.mainloop()