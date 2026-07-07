"""
Docstring para Unidad4.4Enumerador

En esta unidad aprenderás a usar la función enumerar (enumerate) en Python, que es muy útil cuando necesitas iterar sobre una 
secuencia y también necesitas un contador para rastrear la posición de cada elemento.

La función enumerate toma una secuencia (como una lista, tupla o cadena) y devuelve un objeto enumerado. Cada elemento del
objeto enumerado es una tupla que contiene un índice (la posición del elemento en la secuencia) y el valor del elemento.
"""

#Ejemplo básico de uso de enumerate
frutas = ['manzana', 'banana', 'cereza']
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

print("--------------------")
lista = list(enumerate(frutas))
print(lista)  # Esto imprimirá el objeto enumerate


""" Ejercicios"""
print("-----Ejercicios de Enumerador-----")
print("Ejercicio 1")
#Ejercicio 1
"""Práctica Enumerador 1
Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

Tip: utiliza loops!"""

#Solución Ejercicio 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print("--------------------")
print("Ejercicio 2")
#Ejercicio 2
"""Práctica Enumerador 2
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices ."""

#Solución Ejercicio 2
lista_indices = list(enumerate("Python"))

print(lista_indices)

print("--------------------")
print("Ejercicio 3")
#Ejercicio 3
"""Práctica Enumerador 3
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
"""

#Solución Ejercicio 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, elemento in enumerate(lista_nombres):
    if elemento.startswith("M"):
        print(indice)

print("--------------------")




"""
El método 'startswith()' se utiliza para verificar si una cadena comienza con un prefijo específico.

Sintaxis:
cadena.startswith(prefijo[, inicio[, fin]])

Parámetros:
- prefijo: La cadena o tupla de cadenas que se desea verificar como prefijo.
- inicio (opcional): Índice desde el cual comenzar a buscar (por defecto es 0).
- fin (opcional): Índice hasta el cual buscar (por defecto es el final de la cadena).

Valor de retorno:
Devuelve True si la cadena comienza con el prefijo especificado; de lo contrario, devuelve False.

Ejemplos:
1. Uso básico:
   texto = "manzana"
   resultado = texto.startswith("ma")  # Salida: True

2. Uso con índices:
   texto = "manzana"
   resultado = texto.startswith("an", 1)  # Salida: True

3. Uso con tuplas:
   texto = "manzana"
   resultado = texto.startswith(("ma", "ba"))  # Salida: True

Aplicación práctica:
Se puede utilizar en bucles para filtrar elementos en una lista. Por ejemplo:
mi_lista = ["manzana", "banana", "mora", "kiwi"]
for elemento in mi_lista:
    if elemento.startswith("m"):
        print(elemento)  # Imprime 'manzana' y 'mora'
"""