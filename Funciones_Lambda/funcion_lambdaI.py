if __name__ == "__main__":

    area = lambda base,altura : (base*altura)/2
    print(area(5.5, 4))

    cubo = lambda numero:pow(numero, 3)
    print(cubo(13))

    destacar_valor = lambda comision, extra:"$¡{0:.2f} -> ${1:.2f}!".format(comision, extra)
    print(destacar_valor(865.89657, 456.98575))