"""Para no dependender del metodo append de las listas,
vamos a crear una funcion que reciba una lista y un elemento
y devuelva una nueva lista con el elemento agregado al final."""

palabra = "Python"

lista = [letra for letra in palabra]
print("Lista original:", lista)

#Incluso podemos incluir condicionales
#Solo letras que no sean vocales
lista_sin_vocales = [letra for letra in palabra if letra.lower() not in "aeiou"]
print("Lista sin vocales:", lista_sin_vocales)

#Si tenemos una lista de numeros, podemos crear una nueva lista, por ejemplo si la elevamos al cuadrado
numeros = [1, 2, 3, 4, 5, 6, 9.5]
numeros_cuadrado = [numero ** 2 for numero in numeros]
print("Números al cuadrado:", numeros_cuadrado)

"""Ejercicios"""
#Ejercicio 1
print("--------------------------------------------------------------")
print("Ejercicio 1")
"""Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes 
aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte 
muy útiles en tu práctica profesional!

Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]"""

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valores ** 2 for valores in valores]

print(valores_cuadrado)

#Ejercicio 2
print("--------------------------------------------------------------")
print("Ejercicio 2")

"""Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]"""

valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [valores for valores in valores if valores % 2 < 1]

print(valores_pares)

#Ejercicio 3
print("--------------------------------------------------------------")
print("Ejercicio 3")
"""Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos 
mismos valores en una nueva lista de valores de temperatura en grados Celsius. 
La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius"""

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(temperatura_fahrenheit - 32)*(5/9) for temperatura_fahrenheit in temperatura_fahrenheit]

print(grados_celsius)