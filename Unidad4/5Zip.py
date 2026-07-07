"""La funcion ZIP
El método zip() en Python se utiliza para combinar dos o más iterables (como listas, tuplas, etc.) 
en un solo iterable de tuplas. Cada tupla contiene elementos correspondientes de los iterables originales.
La función zip() toma iterables como argumentos y devuelve un iterador de tuplas, donde la i-ésima tupla 
contiene el i-ésimo elemento de cada uno de los iterables proporcionados. Si los iterables tienen longitudes diferentes, 
zip() detiene la combinación cuando se alcanza el final del iterable más corto."""


#ejemplo de uso de zip
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]

combinado = list(zip(nombres, edades))
print(combinado)  # Esto imprimirá: [('Ana', 25), ('Luis', 30), ('Carlos', 22)]

#Otro ejemplo 
colores = ['rojo', 'verde', 'azul']
cantidades = [10, 20, 15]
for color, cantidad in zip(colores, cantidades):
    print(f"Color: {color}, Cantidad: {cantidad}")

""" Ejercicios"""
#Ejercicio 1
print("-----Ejercicios de Zip-----")
print("Ejercicio 1")
"""Práctica Zip 1
Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín

Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]"""

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")


print("--------------------")
print("Ejercicio 2")
#Ejercicio 2
"""Práctica Zip 2
Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip."""
marcas = ['Nissan', 'Ford', 'Dodge', 'Toyota', 'Honda']
productos = ['Coupe', 'Crossroad', 'Pick up', 'Sedan', 'Mini']

mi_zip = zip(marcas, productos)

print(mi_zip)

print(list(mi_zip))  # Imprime la lista de tuplas formadas por zip

print("--------------------")

print("Ejercicio 3")
#Ejercicio 3
"""Práctica Zip 3
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]"""


espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one', 'two', 'three', 'four','five']

numeros = list(zip(espaniol, portugues, ingles))

print(numeros)

