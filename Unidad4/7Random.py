"""
Para esta tema primero necesitamos importar el módulo random que contiene funciones para generar números aleatorios.

que es randint (Random Integer)

Pero que es importar?

Importar es traer funciones o variables de otros módulos o bibliotecas para usarlas en nuestro código actual. 
En este caso, al importar el módulo random, podemos utilizar sus funciones para generar números aleatorios.

La función randint(a, b) del módulo random genera un número entero aleatorio entre los valores a y b, ambos inclusive.

from random import randint
# Generar un número entero aleatorio entre 1 y 10
numero_aleatorio = randint(1, 10)
print(numero_aleatorio)  # Salida: Un número entero aleatorio entre 1 y 10

Y si queremos importar todas las funciones del módulo random, podemos usar:
from random import *
El asterisco (*) indica que queremos importar todo el contenido del módulo random.

En este modulo en especifico, utilizaremos 

randint()
uniform()
choice()
random()
shuffle()
"""

from random import randint, uniform, choice, random, shuffle    


from random import *


random = randint(1, 50)
print(random)

randomdecimal = uniform(1, 5)
print(randomdecimal)  # Salida: Un número decimal aleatorio entre 1 y 5

#Que se puede redondear un numero decimal
#redondear = round(randomdecimal, 2), lo que nos daria 2 decimales

#El metodo random() genera un número decimal aleatorio entre 0.0 y 1.0
#decimal_aleatorio = random()
#print(decimal_aleatorio)  # Salida: Un número decimal aleatorio entre 0.0 y 1.0

#EL metodo Choice() selecciona un elemento aleatorio de una secuencia (como una lista o una tupla)
#elementos = ['manzana', 'banana', 'cereza', 'naranja']
#fruta_aleatoria = choice(elementos)
#print(fruta_aleatoria)  # Salida: Una fruta aleatoria de la lista

#El metodo Shuffle() mezcla aleatoriamente los elementos de una lista in situ
#numeros = [1, 2, 3, 4, 5]
#shuffle(numeros)
#print(numeros)  # Salida: La lista de números mezclada aleatoriamente

"""Ejercicios"""

#Ejercicio 1 
"""Implementa la función randint() de la librería random que te permita 
obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio"""

print("------------------------------------------------")
print("Ejercicio 1")

from random import randint

aleatorio = randint(1,10)
print(aleatorio)

#Ejercicio 2
"""Implementa la función random() de la librería random que te permita 
obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio"""
print("------------------------------------------------")
print("Ejercicio 2")

from random import random

aleatorio = random()
print(aleatorio)

#Ejercicio 3
"""Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y 
almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]"""

print("------------------------------------------------")
print("Ejercicio 3")

from random import choice

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)
print(sorteo)