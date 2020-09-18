from tkinter import Tk, Menu, messagebox

def create_submenu(text, menu, options):

    if len(options) > 0:        
        for opc, action in options.items():
            if opc == "":
                menu.add_separator()
            else:
                menu.add_command(label = opc, command = action)
            
    menu_options.add_cascade(label = text, menu = menu)


def create_popupAbout(title = None, text = None):

    messagebox.showinfo(message = text, title = title)


def create_popupLicense(title = None, text = None):

    messagebox.showwarning(title = title, message = text)


def create_popupExit(title = None, text = None, root = None):

    answer = messagebox.askquestion(title = title, message = text)
    
    if answer == messagebox.YES:
        root.destroy()
    else:
        pass


def create_popupClose(title = None, text = None, root = None):

    answer = messagebox.askretrycancel(title = title, message = text)

    if answer == False:
        root.destroy()


root = Tk()
# ------------------------- Creación de Menu ------------------------
menu_options = Menu(root)


option_file = Menu(menu_options, tearoff = 0)
""" ------------ Creación de submenu para Archivo ----------------"""
create_submenu("Archivo", option_file, 
    {   "Nuevo" : None, 
        "Guardar" : None, 
        "Guardar como" : None, 
        "" : None, 
        "Cerrar": lambda:create_popupClose(title = "Reintentar", text = "No es posible cerrar el documento", root = root), 
        "Salir": lambda:create_popupExit(title = "Salir", text = "¿Desea salir?", root = root)
    }
)

option_edit = Menu(menu_options, tearoff = 0)
""" ------------ Creación de submenu para Editar ----------------"""
create_submenu("Editar", option_edit, 
    {
        "Copiar": None, 
        "Cortar": None, 
        "Pegar": None
    }
)

option_tool = Menu(menu_options, tearoff = 0)
create_submenu("Herramientas", option_tool, {})

option_help = Menu(menu_options, tearoff = 0)
""" ------------ Creación de submenu para Ayuda ----------------"""
create_submenu("Ayuda", option_help, 
    {
        "Licencia": lambda:create_popupLicense(title = "Licencia", text = "Producto bajo licencia GNU"), 
        "Acerca de...": lambda:create_popupAbout(title = "Procesador de texto", text = "Procesador versión 2020")
    } 
)

root.title("Uso Menu")
root.config(menu = menu_options, width = 300, height = 300)
root.mainloop()