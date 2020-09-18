 
# Presidente
salarioPresidente = float(input(" >> Introduce salario Presidente: "))
print(" -> Salario presidente: {0:.2f} \n".format(salarioPresidente))

# Director
salarioDirector = float(input(" >> Introduce salario Director: "))
print(" -> Salario presidente: {0:.2f} \n".format(salarioDirector))

# Jefe de Área
salarioJefe = float(input(" >> Introduce salario Jefe Área: "))
print(" -> Salario presidente: {0:.2f} \n".format(salarioJefe))

# Administrativo
salarioAdministrativo = float(input(" >> Introduce salario Administrativo: "))
print(" -> Salario presidente: {0:.2f} \n".format(salarioAdministrativo))

if salarioAdministrativo < salarioJefe < salarioDirector < salarioPresidente:
    print(" >> Funciona correctamente \n")
else:
    print(" >> Algo anda mal")