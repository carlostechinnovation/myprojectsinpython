"""
Ejemplos de operaciones habituales.
Si tengo alguna duda, puedo verlas rápidamente sin ir a Internet.
"""

import argparse
import numpy as np

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
    print("tiposDedatos...")
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
    print("cadenas...")
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
    mySeparator = "TEST"
    x = mySeparator.join(midiccionario)
    print(x)


def otrosTiposDeDato():
    print("otrosTiposDeDato...")
    # Boolean
    print(bool("Hola"))  # True
    # False -->Son false: cadenas vacias, Listas vacías, numero 0, None...
    print(bool(""))
    print(3 > 1)

    print(isinstance(200, int))  # comprueba si un numero es un INT


def listas():
    print("listas...")
    # Lists: primer elemento tiene indice 0, tienen ORDEN, los elementos se añaden por detras (append), son mutables, permiten elementos duplicados
    thislist = ["apple", "banana", "cherry"]
    thislist.append("apple")
    print(thislist)
    # creada con el constructor explícito (dobles parentesis)
    listaHeterogenea = list(("abc", 34, True, 40, "male"))
    print(listaHeterogenea)
    print(listaHeterogenea[-1])  # indices empezando por detrás
    if "male" in listaHeterogenea:
        print("Yes, 'male' is in the list")

    listaHeterogenea[0] = "otro"  # Cada elemento es mutable
    # Se pueden METER VARIOS elementos donde antes habia solo UNO!!!:
    listaHeterogenea[1:2] = ["carlos", "laura"]
    print(listaHeterogenea)

    # y se pueden sustituir VARIOS elementos por UNO solo:
    thislist = ["apple", "banana", "cherry"]
    thislist[1:3] = ["watermelon"]
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)

    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)

    # meter una tupla dentro de una lista
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)  # mete CUALQUIER ITERABLE
    print(thislist)
    thislist.pop(1)  # quita un elemento segun el indice
    print(thislist)
    del thislist[0]  # borra un elemento
    print(thislist)
    thislist.clear()  # vacía la lista (sin borrarla)
    del thislist  # borra la lista entera
    if 'thislist' not in locals():
        print("La lista no existe ya")

    thislist = ["banana", "apple", "cherry"]
    for x in thislist:
        print(x)
    for i in range(len(thislist)):
        print(thislist[i])

    # list comprehension: newlist = [expression for item in iterable if condition == True]
    newlist = [x for x in thislist if "a" in x]
    print(newlist)
    newlist.sort(reverse=False)
    print(newlist)


def listasAvanzado():
    print("listasAvanzado...")

    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)

    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key=str.lower)  # ordena case-insensitive
    print(thislist)

    # Para COPIAR el contenido de una lista en otra lista NUEVA, no se hace lista2=lista1 (eso apunta a la misma referencia), sino:
    lista2 = thislist.copy()  # opcion1
    lista3 = list(thislist)  # opcion2
    print(lista2)
    print(lista3)

    concatenada = lista2+lista3  # nueva lista
    lista2.extend(lista3)  # lista 2 ampliada
    print(concatenada)
    print(lista2)

    # Meter/sacar indicando indice: insert, pop
    # sacar indicando valor: remove


def tuplas():  # son NO MUTABLES!!!!!!!!!!!
    print("tuplas...")
    # Tuples
    thistuple = ("apple", "banana", "cherry",)  # termina en coma!!!
    print(thistuple)
    thistuple = ("apple",)  # termina en coma!!!
    print(type(thistuple))
    thistuple = ("apple")  # No es una tupla porque no termina en coma!!!
    print(type(thistuple))
    # puede contener elementos de varios tipos
    tuple1 = ("abc", 34, True, 40, "male")
    print(tuple1)
    # note the double round-brackets
    thistuple = tuple(("apple", "banana", "cherry"))
    print(thistuple)

    print("Como las TUPLAS son INMUTABLES, si queremos añadir elementos hay que convertirlas en listas o crear una nueva tupla con elementos añadidos:")
    thistuple = ("apple", "banana", "cherry")
    thistuple += ("orange",)  # termina en coma
    print(thistuple)

    print("Como las TUPLAS son INMUTABLES, si queremos borrar elementos hay que convertirlas en listas:")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)
    print(thistuple)

# me llego en: https://www.w3schools.com/python/python_tuples_update.asp


def sets():
    print("sets...")
    # Sets


def diccionarios():
    print("Dictionaries...")
    # Dictionaries


def operadores():
    print("operadores...")
    # https://docs.python.org/3/library/operator.html
    print(11 % 1)  # modulo
    print(10**2)  # exponente
    print(51//2)  # Division y FLOOR

    # MATRICES
    a = np.array([[1, 0], [0, 1]])
    b = np.array([[4, 1], [2, 2]])
    productoMatrices = np.matmul(a, b)
    # El operador @ es equivalente a la funcion np.matmul
    productoMatrices2 = a @ b
    print(productoMatrices)
    print(productoMatrices2)

    # Comparaciones de igualdad
    print(2 == 3)
    print(2 != 3)


def main(parametros):
    print("===== MAIN.INICIO =====")
    # variable global, creada dentro de una función. Exige poner global
    global unaNuevaVariableGlobal
    unaNuevaVariableGlobal = 100
    variablesTiposCastingsEtc()
    tiposDedatos()
    cadenas()
    otrosTiposDeDato()
    operadores()
    listas()
    listasAvanzado()
    tuplas()
    sets()
    diccionarios()
    print("===== MAIN.FIN =====")


# Si el código python se ejecuta desde un script con comando, se entra por aquí y se pueden capturar los parámetros fácilmente
if __name__ == '__main__':
    params = procesarParametros()
    main(parametros=params)
