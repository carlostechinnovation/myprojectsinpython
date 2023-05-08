"""Operaciones habituales con PANDAS
"""
import matplotlib.pyplot as plt
import pandas as pd

print(pd.__version__)

print("SERIE + LABEL:")
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

print("Objetos clave/valor interpretados como Series:")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

print("MULTIDIMENSIONAL - DataFrame:")
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print("Dataframes con indices explícitos:")
myvar2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(myvar2)
print(myvar2.loc["day2"])

print("Leer ficheros estructurados (CSV) y crear un dataFrame con sus datos:")
df = pd.read_csv("C:\\apps\\pandas001.csv")
print(df.to_string())  # pinta el dataframe completo
print(df)  # pinta las primeras y últimas 5 filas

print("Leer un fichero y cargar sus datos en un dataframe:")
df = pd.read_json("C:\\apps\\pandas002.json")
print(df)

print("INFO (hace conteo de los no nulos):")
print(df.info())

print("Limpieza de filas con algun campo nulo:")
# df.dropna(inplace=True) #borra filas
# df.fillna(130, inplace=True)  # rellena filas con algo
# df["Calories"].fillna(130, inplace = True) #rellena solo ciertas columnas y donde haya nulo

print("...rellenar con la mediana...")
caloriasmediana = df["Calories"].median()
df["Calories"].fillna(caloriasmediana, inplace=True)

print("...rellenar con la moda (value that appears most frequently)...")
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(df)


print("Formatos/castings:")
# https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
data = {"fecha": ['2020/10/02', '2020/10/02', 'NaN', 20201225]}
df = pd.DataFrame(data)
df['fecha'] = pd.to_datetime(df['fecha'])  # casting a fecha
print(df)  # Si el casting a fecha no se consigue, se obtiene NaT (Not a Time), que es un valor vacío (empty)
# df.dropna(subset=['fecha'], inplace = True) #otra opcion es borrar todas las filas con NULL en la columna fecha

print("Reparar outliers:")
data = {"dato": [20, 20, 40, 55188, 12, 25]}
df = pd.DataFrame(data)
for x in df.index:
    if df.loc[x, "dato"] > 100:
        df.loc[x, "dato"] = 100  # si supera 100, fija 100

print(df)

print("Duplicados:")
print(df.duplicated())  # buscarlos
df.drop_duplicates(inplace=True)  # borrarlos, dejando solo uno.
print(df)

print("Correlaciones: corr()")

print("Plotting:")
df = pd.read_csv("C:\\apps\\pandas003.csv")
# df.plot()
# plt.show()
# df.plot(kind='scatter', x='Duration', y='Calories')
# plt.show()
df["Duration"].plot(kind='hist')
plt.show()
