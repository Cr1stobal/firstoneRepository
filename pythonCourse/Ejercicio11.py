"""

Calcula el area de un rectangulo
pide base y altura al usuario

"""

while True:
    Base = int(input("Introduce el valor de la base (o 0 para salir):  "))
    if Base == 0:
        break

    Altura = int(input("Introduce el valor de la altura:  "))

    Resultado = Base * Altura

    print("El area del rectangulo es: ", Resultado)



