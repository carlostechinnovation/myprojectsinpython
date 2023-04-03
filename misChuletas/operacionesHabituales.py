"""
Ejemplos de operaciones habituales.
Si tengo alguna duda, puedo verlas rápidamente sin ir a Internet.
"""

import argparse

miVariableGlobal = 56  # global


# ----- TIPOS DE DATOS
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


def procesarParametros():
    parser = argparse.ArgumentParser(
        description='Parámetros de entrada del script con operaciones habituales')
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    return args


def variablesTiposCastingsEtc():
    print("variablesTiposCastingsEtc...")

    # para poder modificar la variable global existente, debo ponerla con global dentro de esta función
    global unaNuevaVariableGlobal
    unaNuevaVariableGlobal = 3

    x = 5
    y = "John"
    z = 'Carlos'  # los string tambien permiten comillas simples
    Z = 25  # es case-sensitive
    print("x es del  tipo" + str(type(x)))
    print("y es del tipo" + str(type(y)))
    print("z es del tipo" + str(type(z)))
    print("Z es del tipo" + str(type(Z)))

    # Nomenclatura
    variable = 3
    _variable = 4
    miVariable = 5
    a, b, c = 1, 2, 3

    # Desglosar de una lista a variables
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    # mete espacios  --> No exige convertir a STRING --> Es mejor que usar el operador +
    print(x, y, z)
    print(x + y + z)  # concatena cadenas

    # Castings
    x = int(1)   # x will be 1
    y = int(2.8)  # y will be 2
    z = int("3")  # z will be 3
    w = float("4.2")  # w will be 4.2
    z = str(3.0)  # z will be '3.0


def tiposDedatos():
    x = "Hello World"  # str
    x = 20  # int
    x = 20.5  # float
    x = 1j  # complex
    x = ["apple", "banana", "cherry"]  # list
    x = ("apple", "banana", "cherry")  # tuple
    x = range(6)  # range
    x = {"name": "John", "age": 36}  # dict
    x = {"apple", "banana", "cherry"}  # set
    x = frozenset({"apple", "banana", "cherry"})  # frozenset
    x = True  # bool
    x = b"Hello"  # bytes
    x = bytearray(5)  # bytearray
    x = memoryview(bytes(5))  # memoryview
    x = None  # NoneType

    x = 3+5j
    print("Real=" + str(x.real) + " y parte imag=" + str(x.imag))

    import random
    print(random.randrange(1, 10))  # numero random en un rango


def cadenas():
    # multilinea
    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)

    # los strings son arrays de caracteres (el indice empieza por 0)
    print(a[1])

    for x in "carlos":
        print(x)

    txt = "The best things in life are free!  "
    print("free" in txt)
    print("free" not in txt)
    print(txt[2:5])
    print(txt[:5])
    print(txt[-5:-2])
    print(txt.strip())  # Es la operacion TRIM
    print(txt.replace("f", "C"))

    # Formatear cadenas
    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))

    txt = "We are the so-called \"Vikings\" from the north.\nOtra linea."
    print(txt)

    # funciones con strings: https://www.w3schools.com/python/python_strings_methods.asp

    # Busqueda
    txt = "Hello, welcome to my world."
    print(txt.find("q"))  # si no lo encuentra, devuelve -1
    print(txt.index("w"))  # si no lo encuentra, lanza excepcion

    # Otras funciones
    midiccionario = {"name": "John", "country": "Norway"}
    # mySeparator = "TEST"
    # x = mySeparator.join(midiccionario)
    # print(x)


def main(parametros):
    print("===== INICIO =====")
    # variable global, creada dentro de una función. Exige poner global
    global unaNuevaVariableGlobal
    unaNuevaVariableGlobal = 100
    variablesTiposCastingsEtc()
    tiposDedatos()
    cadenas()
    print("===== FIN =====")


# Si el código python se ejecuta desde un script con comando, se entra por aquí y se pueden capturar los parámetros fácilmente
if __name__ == '__main__':
    params = procesarParametros()
    main(parametros=params)
