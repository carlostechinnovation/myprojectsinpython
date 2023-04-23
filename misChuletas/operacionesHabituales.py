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

    print("Como las TUPLAS son INMUTABLES, si queremos AÑADIR elementos hay que convertirlas en listas o crear una nueva tupla con elementos añadidos:")
    thistuple = ("apple", "banana", "cherry")
    thistuple += ("orange",)  # termina en coma
    print(thistuple)

    print("Como las TUPLAS son INMUTABLES, si queremos BORRAR elementos hay que convertirlas en listas:")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)
    print(thistuple)

    print("Volcar tupla en variables (se llama UNPACKING) y se puede usar el asterisco para coger los restantes:")
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *otros) = fruits
    print(green)
    print(yellow)
    print(otros)
    (primero, *intermedios, ultimo) = fruits
    print(primero)
    print(intermedios)
    print(ultimo)

    print("Bucle para ver elementos:")
    for i in range(len(fruits)):
        print(fruits[i])


def tuplasAvanzado():
    print("tuplasAvanzado...")
    print("JOIN:")
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)

    print("Repetir elementos (duplica, triplica...):")
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2
    print(mytuple)


def sets():
    print("Sets...")
    print("No garantizan el orden de los elementos. Sus elementos se pueden meter/sacar, pero no modificar. Los elementos DUPLICADOS se ignoran (y los elementos True y 1 se consideran iguales).")
    thisset = {"apple", "banana", "cherry", "apple", True, 1}
    print(thisset)
    thisset = set(("apple", "banana", "cherry"))  # Constructora explícita
    print(thisset)

    print("Recorrer elementos del set:")
    for x in thisset:
        print(x)
    print("Comprobar si el set contiene un elemento:")
    print("banana" in thisset)

    print("Añadir un elemento (ADD) y añadir varios elementos (UPDATE):")
    thisset = {"apple", "banana", "cherry"}
    thisset.add("orange")
    # Esto puede ser cualquier iterable: set, list...
    tropical = list(("pineapple", "mango", "papaya"))
    thisset.update(tropical)
    print(thisset)

    print("Quitar elementos con remove (lanza error si no existe) o discard (no lanza error si no existe):")
    thisset.discard("banana")
    print(thisset)
    # pop() quita un elemento al azar y lo devuelve

    print("Vaciar con clear y borrar con del:")
    thisset.clear()
    del thisset


def setsAvanzado():
    print("Juntar dos sets con union() o update():")
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)  # UNION devuelve un NUEVO set
    print(set3)
    set1.update(set2)  # UPDATE actualiza el set, no crea uno nuevo
    print(set1)

    print("Extraer interseccion de dos sets (elementos compartidos):")
    x = {"manzana", "platano", "cdereza"}
    mascara = {"google", "microsoft", "manzana"}
    x.intersection_update(mascara)  # Set x se queda con lo filtrado
    print(x)
    x = {"manzana", "platano", "cdereza"}
    z = x.intersection(mascara)
    print(z)

    print("La operacion NOT IN hecha con sets:")
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.symmetric_difference_update(y)
    print(x)
    x = {"apple", "banana", "cherry", True}
    y = {"google", 1, "apple", 2}
    z = x.symmetric_difference(y)  # True y 1 son lo mismo
    print(z)

    # isdisjoint()	Returns whether two sets have a intersection or not
    # issubset()	Returns whether another set contains this set or not
    # issuperset()	Returns whether this set contains another set or not


def diccionarios():
    print("Dictionaries...")
    print("Hasta python 3.6 eran desordenados. Desde python 3.7 garantizan el ORDEN.")
    thisdict = {"brand": "Ford",  "model": "Mustang",  "year": 1964,
                "year": 2020,
                "colors": ["red", "white", "blue"]}  # pueden contener listas, etc
    print("No permiten claves duplicadas; si aparecen, se coge el ultimo valor encontrado (ej. year=2020)")
    print(thisdict)
    print(thisdict["brand"])  # buscar por clave
    print(thisdict.get("brand"))  # buscar por clave
    print(len(thisdict))
    claves = thisdict.keys()
    print(claves)

    print("Constructora (no usa doble parentesis):")
    thisdict = dict(name="John", age=36, country="Norway")
    print(thisdict)

    print("La referencia a las CLAVES se actualiza (añade nueva clave):")
    claves = thisdict.keys()
    print(claves)
    thisdict["propietario"] = "Carlos"  # NUEVA clave añadida
    print(claves)

    print("La referencia a los VALORES se actualiza:")
    valores = thisdict.values()
    print(valores)
    thisdict["name"] = "Ferrari"
    print(valores)

    print("Si de trae la lista de elementos (ITEMS) y hay un cambio posterior, se actualiza (puntero por REFERENCIA):")
    elementos = thisdict.items()
    print(elementos)
    thisdict["name"] = "Mercedes"
    print(elementos)
    print("name" in thisdict)

    print("Update:")
    thisdict.update({"name": "BMW"})
    print(thisdict)

    print("Sacar elementos --> pop() por clave, popitem() al azar y del por clave")
    thisdict.pop("name")
    print(thisdict)
    del thisdict["propietario"]
    print(thisdict)
    print("vaciar diccionario -->clear()")
    print("borrar diccionario -->del")

    print("Itera claves:")
    for x in thisdict:
        print(x)
    print("iterar valores:")
    for x in thisdict:
        print(thisdict[x])
    print("iterar por claves y valores:")
    for x, y in thisdict.items():
        print(x, y)

    print("Utilizar un nuevo diccionario que sea copia del primero (no referencia):")
    mydict = thisdict.copy()
    mydict = dict(thisdict)  # Esta es otra forma equivalente
    print(mydict)

    print("Diccionarios ANIDADOS: un diccionario contiene varios diccionarios:")
    myfamily = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus", "year": 2011}
    }
    print("Nombre del hijo 2: " + myfamily["child2"]["name"])


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


def buclesFuncionesEtc():
    print("buclesFuncionesEtc...")
    print("if...else:")
    if (5 != 3 and 3 == 3):
        print("if-else dentro")
    elif (3 < 4 or not 3 == 7):
        print("if-else dentro2")
    else:
        print("otro")

    print("if...else comprimido:")
    print("A") if 3 > 5 else print("B")
    print("A") if 3 > 5 else print("=") if 2 == 2 else print("B")

    print("saltar con pass:")
    if 5 < 3:
        pass

    print("bucles:")
    i = 1
    while i < 6:
        print(i)
        i += 1
        if i > 3:
            # continue #itera, sin leer lo siguiente que haya
            break
    else:  # se ejecuta despues del while!!!!!
        print("Al salir del while")


def funcionPrueba1(*kids):
    print("The youngest child is " + kids[2])
    return 1000  # se puede devolver un valor


def funcionPrueba2(child3="Carlos", child2="", child1=""):  # con valor default
    print("The youngest child is " + child3)


def funcionPrueba3(**kid):
    print("His last name is " + kid["lname"])


def funcionVacia():
    pass  # se pone pass para evitar q haya error


def funcionesLambda():
    print("funcionesLambda...")
    def miFuncionLambda(a, b): return a * b
    print(miFuncionLambda(5, 6))


def listasUsadasComoArrays():
    print("listasUsadasComoArrays...")
    cars = ["Ford", "Volvo", "BMW"]
    numElementos = len(cars)
    cars.append("Honda")
    cars.pop(1)
    # cars.remove("Volvo")
    for x in cars:
        print(x)


class Persona:
    def __init__(self, nombre, age):  # INIT (constructora): el primer parametro siempre es self
        self.nombre = nombre
        self.age = age

    def __str__(self):  # STR: el primer parametro siempre es self
        return f"{self.nombre}({self.age})"

    def printarNombre(self):  # funcion custom: el primer parametro siempre es self
        print("Hello my name is " + self.nombre)


class Estudiante(Persona):  # herencia
    def __init__(self, nombre, apellidos, edad, estudios):
        super().__init__(nombre, edad)  # constructora del padre
        self.estudios = estudios

    def printarNombre(self):  # Sobreescribe la funcion del padre
        print("Estudiante: " + self)


def ejemplosConClases():
    print("Clases...")
    p1 = Persona("John", 36)  # usa __init__()
    print(p1.nombre)
    print(p1.age)
    print(p1)  # usa __str__()
    p1.printarNombre()

    # cambiar o borrar propidades de objetos:
    p1.age = 40
    del p1.age
    del p1  # borrar el objeto entero


def herencia():
    print("Herencia...")
    e1 = Estudiante(nombre="pepe", apellidos="viyuela",
                    edad=1, estudios="infantil")
    print(e1)


class MiIteradorDeNumeros:
    def __iter__(self):
        self.a = 1  # Inicializado
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


def iteradores():
    print("iteradores (objetos que implementan metodos __iter__ y __next__)...")

    print("Objetos iterABLES de los que obtenemos objetos iteradores:")
    miTupla = ("apple", "banana", "cherry")
    miIterador = iter(miTupla)

    print("usando next:")
    print(next(miIterador))
    print(next(miIterador))
    print(next(miIterador))

    print("usando for:")
    for x in miTupla:
        print(x)

    print("Ejemplo de iterador custom, que genera numeros y para cuando es >=3:")
    miObjeto = MiIteradorDeNumeros()
    iterador = iter(miObjeto)
    for x in iterador:
        print(x)


class Vehiculo:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehiculo):
    pass


class Boat(Vehiculo):
    def move(self):
        print("Sail!")


class Plane(Vehiculo):
    def move(self):
        print("Fly!")


def polimorfismo():
    print("Polimorfismo de funciones...")
    print("Un ejemplo es la funcion len(), que calcula la longitud o numero de elementos de muchos tipos de objetos.")
    print(len("hola"))  # caracteres de una cadena
    print(len(("apple", "banana", "cherry")))  # elementos de una tupla

    print("Polimorfismo de clases (y herencia)...")
    car1 = Car("Ford", "Mustang")  # Create a Car class
    boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
    plane1 = Plane("Boeing", "747")  # Create a Plane class
    for x in (car1, boat1, plane1):
        x.move()


def scope():
    print("scope...")
    print("local (intrafuncion) y global (fuera de funcion) scope. Cuidado porque dos variables con el mismo nombre pueden convivir. La palabra reservada 'global' fuerza a que sea global")

    def miFuncion1():
        global x
        x = 200

    print("Antes de invocar la funcion, la variable no existe x. ¿Existe?=" +
          str('x' in locals()))
    miFuncion1()
    print("Despues de invocar la funcion, la variable es global y vale: x="+str(x))


def modules():
    print("modules (liberias, paquetes)...")
    import miModulo as mm
    mm.greeting("Carlos")

    a = mm.person1["age"]
    print(a)

    import platform  # este es un modulo built-in que se carga en el environment base
    print(str(platform.system()))
    print("Las funciones y variables dentro del modulo miModulo son:")
    print(dir(mm))

    from miModulo import person1 as diccionarioP1  # importar solo el diccionario
    print(diccionarioP1["age"])  # aqui no hay que poner mm. ni miModulo.


def fechas():
    print("fechas...")

    # https://www.w3schools.com/python/python_datetime.asp


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
    tuplasAvanzado()
    sets()
    setsAvanzado()
    diccionarios()
    buclesFuncionesEtc()
    funcionPrueba1("Emil", "Tobias", "Linus")  # numero variable de parametros
    funcionPrueba2(child1="Emil", child2="Tobias",
                   child3="Linus")  # parametros clave=valor
    funcionPrueba3(fname="Tobias", lname="Refsnes")
    funcionVacia()
    funcionesLambda()
    listasUsadasComoArrays()
    ejemplosConClases()
    herencia()
    iteradores()
    polimorfismo()
    scope()
    modules()
    fechas()

    print("===== MAIN.FIN =====")


# Si el código python se ejecuta desde un script con comando, se entra por aquí y se pueden capturar los parámetros fácilmente
if __name__ == '__main__':
    params = procesarParametros()
    main(parametros=params)
