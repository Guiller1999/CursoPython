from tkinter import StringVar, Label

class Evento():

    # Constructor
    def __init__(self):
        # Variables de control
        self.texto = StringVar() # Esta variable se conecta al label que muestra la expresion matematica
        self.resultado = StringVar() # Esta variable se conecta al label que muestra el resultado
        
        # Variable que sirve para almacenar el resultado de la expresión matemática ingresada
        # con el fin de poder recuperarla en cualquier momento el resultado anterior
        self.memoria = ""

    # Metodo para ingresar parentesis a la expresión matematica ingresada
    # con el fin de evitar errores en el calculo
    def __insertar_parentesis(self, boton):

        texto = self.texto.get()
        texto_acortado = texto[len(texto) -1 : len(texto)]

        if boton == "(":
            if texto_acortado.isdigit():
                self.texto.set(self.texto.get() + "*" + boton)
            else:
                self.texto.set(self.texto.get() + boton)
        else:
            self.texto.set(self.texto.get() + boton + "*")

    # Metodo para ingresar la constante PI a la expresión matematica ingresada
    # con el fin de evitar errores en el calculo
    def __insertar_PI(self, boton):

        texto = self.texto.get()
        texto_acortado = texto[len(texto) - 1 : len(texto)]

        # Verificamos si el valor anterior al numero PI es un numero
        # Si lo es antes de colocar el numero PI se coloca el simbolo de multipicacion
        # con el fin de evitar errores en el calculo
        if texto_acortado.isdigit():
            self.texto.set(self.texto.get() + "*" + boton)
        else:
            self.texto.set(self.texto.get() + boton)
    
    def __insertar_cero(self, boton):

        texto = self.texto.get()
        texto_acortado = texto[len(texto) - 1 : len(texto)]

        if texto_acortado == "0" and boton == "0":
            print("C3.1")
        if "." in texto:
            self.texto.set(self.texto.get() + boton)
            print("C3.2")
        elif texto_acortado == "0" and boton != "0" and boton.isdigit():         
            print("C3.3")
            nueva_expr = self.texto.get()
            nueva_expr = nueva_expr[0: len(nueva_expr) - 1]
            self.texto.set(nueva_expr + boton)
        else:
            self.texto.set(self.texto.get() + boton)


    # Metodo que sirve para ir guardando los valores pulsados en la calculadora 
    # y mostrarlos en el label de la expresion matematica 
    def push_btn(self, boton):

        # Explicacion de las condicionales:
        # 1era. Condicional: Se asegura que se inserte de manera correcta el numero PI en la
        # presion matematica
        # 2da. condicional: Se evita que se escriban mas de un cero al inicio de un numero 
        # 3era. condicional: Se evita que se operen con números que tienen a la izquierda ceros
        # sin tener un punto decimal(001 o 01 => No se puede operar con estos valores). Por lo 
        # que se convierten estos por ej: si se tiene 001 se transforma a 1

        if len(self.texto.get()) > 0 and boton == "3.1415926":
            self.__insertar_PI(boton)
        elif len(self.texto.get()) > 0 and boton == "(" or boton == ")":
            self.__insertar_parentesis(boton)
        elif self.texto.get() == "0" and len(self.texto.get()) > 0:
            self.__insertar_cero(boton)
        else:
            self.texto.set(self.texto.get() + boton)

    # Metodo que se encarga de evaluar la expresion matematica y obtiene un resultado
    # de dicha expresion
    def push_resultado(self):

        try:
            
            valor_resultante = eval(self.texto.get()) # Se evalua la expresion y se obtiene un resultado
            self.resultado.set(str(valor_resultante))

            # Se establece un limite a los digitos a mostrar en el resultado
            # Si el resultado tiene una longitud de caracteres mayor a 50
            # Se envía un mensaje a la pantalla
            if len(self.resultado.get()) >= 50:
                self.resultado.set("Math Error")
            else:
                self.memoria = self.resultado.get()
        except SyntaxError: # Excepcion que se lanza cuando no se puede realizar una operacion
            self.texto.set("Syntaxis Error")
        except ZeroDivisionError: # Excepcion que se lanza si se va a dividir por 0 
            self.texto.set("Math Error")
        except TypeError:
            self.texto.set("Type Error")
        except SyntaxWarning:
            self.texto.set("Syntaxis warning")
    
    # Metodo que limpia la pantalla de la calculadora
    def limpiar_pantalla(self):
        self.texto.set("")
        self.resultado.set("")
    

    # Metodo que elimina el ultimo caracter de la expresion matematica
    def eliminar_caracter(self):

        if len(self.texto.get()) <= 1 :
            self.texto.set("")
        else:
            expresion = self.texto.get()
            expresion = expresion[0:len(self.texto.get()) - 1]
            self.texto.set(expresion)
    

    # Metodo que permite enviar como mensaje a la pantalla el resultado de 
    # la expresion anteriormente realizada
    def get_anteriorResultado(self):

        if len(self.texto.get()) > 0:
            self.texto.set(self.texto.get() + self.memoria)
        else:
            self.texto.set(self.memoria)