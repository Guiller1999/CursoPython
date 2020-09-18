from tkinter import Tk, Frame, Label, Button, StringVar
from interfaz.Operaciones_calculadora import Evento

class Calculadora(Frame):

    def __init__(self, master = None):

        super().__init__(master)
        
        # Variables de control
        self.e = Evento()
        self.texto_pantalla = self.e.texto
        self.resultado = self.e.resultado

        self.crear_widgets()
        self.configurar_expansion(2, 1, 1, 1)


    def crear_widgets(self):

        self.__fr_north = Frame(self, bg = "White")
        self.__fr_south = Frame(self, bg = "Blue")
        self.__fr_north.grid(row = 0, column = 0, sticky = "nswe")
        self.__fr_south.grid(row = 1, column = 0, sticky = "nswe")
        self.configurar_expansion(1, 1, 1, 1, widget = self.__fr_north)
        self.configurar_expansion(4, 4, 1, 1, widget = self.__fr_south)

        #--------------------- Creando y configurando widget Label -----------------------
        # Estos dos label servirán como pantalla para la calculadora
        # El primer label muestra la expresión matemática que se está realizando
        self.__lblExpresion = Label(self.__fr_north, justify = "right", textvariable = self.texto_pantalla)
        self.__lblExpresion.config(bg = "White", bd = 2, relief = "flat", font = ("Helvetica", 20, "italic bold"))
        self.__lblExpresion.grid(row = 0, column = 0, sticky = "e", ipadx = 10)

        # Este label se encarga de mostrar el resultado de la expresión matemática mostrada en el primer
        # label
        self.__lbl_resultado = Label(self.__fr_north, justify = "left", state = "normal", textvariable = self.resultado, width = 10)
        self.__lbl_resultado.config(bg = "White", bd = 2, relief = "flat", font = ("Helvetica", 18, "italic bold"))
        self.__lbl_resultado.grid(row = 1, column = 0, sticky = "nswe", ipadx = 10)

        # Botones de la calculadora
        #---------------------------- Fila 1 ---------------------------------
        self.colocarBotones("EXP", 5, 2, 0, 0, expansion = "nswe", comando = lambda:self.e.push_btn("**("))
        self.colocarBotones("^2", 5, 2, 0, 1, expansion = "nswe", comando = lambda:self.e.push_btn("**2"))
        self.colocarBotones("ANS", 5, 2, 0, 2, expansion = "nswe", comando = lambda:self.e.get_anteriorResultado())
        self.colocarBotones("π", 5, 2, 0, 3, expansion = "nswe", comando = lambda:self.e.push_btn("3.1415926"))

        #---------------------------- Fila 2 ---------------------------------
        self.colocarBotones("(", 5, 2, 1, 0, expansion = "nswe", comando = lambda:self.e.push_btn("("))
        self.colocarBotones(")", 5, 2, 1, 1, expansion = "nswe", comando = lambda:self.e.push_btn(")"))
        self.colocarBotones("DEL", 5, 2, 1, 2, expansion = "nswe", comando = lambda:self.e.eliminar_caracter())
        self.colocarBotones("AC", 5, 2, 1, 3, expansion = "nswe", comando = lambda:self.e.limpiar_pantalla())

        #---------------------------- Fila 3 ---------------------------------
        self.colocarBotones("7", 5, 2, 2, 0, expansion = "nswe", comando = lambda:self.e.push_btn("7"))
        self.colocarBotones("8", 5, 2, 2, 1, expansion = "nswe", comando = lambda:self.e.push_btn("8"))
        self.colocarBotones("9", 5, 2, 2, 2, expansion = "nswe", comando = lambda:self.e.push_btn("9"))
        self.colocarBotones("/", 5, 2, 2, 3, expansion = "nswe", comando = lambda:self.e.push_btn("/"))

        #---------------------------- Fila 4 ---------------------------------
        self.colocarBotones("4", 5, 2, 3, 0, expansion = "nswe", comando = lambda:self.e.push_btn("4"))
        self.colocarBotones("5", 5, 2, 3, 1, expansion = "nswe", comando = lambda:self.e.push_btn("5"))
        self.colocarBotones("6", 5, 2, 3, 2, expansion = "nswe", comando = lambda:self.e.push_btn("6"))
        self.colocarBotones("x", 5, 2, 3, 3, expansion = "nswe", comando = lambda:self.e.push_btn("*"))

        #---------------------------- Fila 5 ---------------------------------
        self.colocarBotones("1", 5, 2, 4, 0, expansion = "nswe", comando = lambda:self.e.push_btn("1"))
        self.colocarBotones("2", 5, 2, 4, 1, expansion = "nswe", comando = lambda:self.e.push_btn("2"))
        self.colocarBotones("3", 5, 2, 4, 2, expansion = "nswe", comando = lambda:self.e.push_btn("3"))
        self.colocarBotones("-", 5, 2, 4, 3, expansion = "nswe", comando = lambda:self.e.push_btn("-"))

        #---------------------------- Fila 6 ---------------------------------
        self.colocarBotones(".", 5, 2, 5, 0, expansion = "nswe", comando = lambda:self.e.push_btn("."))
        self.colocarBotones("0", 5, 2, 5, 1, expansion = "nswe", comando = lambda:self.e.push_btn("0"))
        self.colocarBotones("=", 5, 2, 5, 2, expansion = "nswe", comando = lambda:self.e.push_resultado())
        self.colocarBotones("+", 5, 2, 5, 3, expansion = "nswe", comando = lambda:self.e.push_btn("+"))
            

    # Funcion que se encarga de crear y ubicar los botones de la calculadora
    def colocarBotones(self, rotulo, ancho, altura, fila, columna, tp_bd = "flat", expansion = None, comando = None):

        boton = Button(self.__fr_south, text = rotulo, width = ancho, height = altura, justify = "center")
        boton.grid(row = fila, column = columna, sticky = expansion)
        boton.config(relief = tp_bd, font = ("Helvetica", 16, "bold italic"), borderwidth = 2, command = comando)


    # Funcion que se encarga de adaptar los widgets Frame a los cambios en la pantalla
    def configurar_expansion(self, num_row, num_column, weight_row, weight_column, widget = None):

        # Este for se encarga de configurar cada fila del frame cuando se expande la pantalla
        for i in range(num_row):
            
            # Si el valor del widget es None significa que se va a configurar la expansion
            # del objeto de esta clase
            if widget == None: 
                self.rowconfigure(i, weight = weight_row)
            else:                                               # Caso contrario entonces se configura la 
                widget.rowconfigure(i, weight = weight_row)     # expansion del widget pasado como parametro
        
        # Este for se encarga de configurar cada columna del frame cuando se expande la pantalla
        for i in range(num_column):
            
            if widget == None:
                self.columnconfigure(i, weight = weight_column)
            else:
                widget.columnconfigure(i, weight = weight_row)