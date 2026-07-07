"""Las funciones son bloques de código reutilizables que realizan una tarea específica.

En Python, las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden contener parámetros. El código dentro de la función se indenta para indicar que pertenece a esa función.

Aquí hay un ejemplo básico de una función que suma dos números:

```python
def sumar(a, b):
    resultado = a + b
    return resultado
    
    # Usando la función
    # print(sumar(3, 5))  # Esto imprimirá 8
    # print(sumar(10, 20)) # Esto imprimirá 30
"""
"""La estructura de una función en Python es la siguiente:

```python
def nombre_de_la_funcion(parámetros):
    # Código de la función
    return valor_de_retorno
```"""


def saludar_persona():
    print("Hola")

saludar_persona()  # Esto imprimirá "Hola"

def saludar_persona(nombre):
    print("HOla!!!" + nombre)


saludar_persona("Juan")
saludar_persona("NOSE XD")

#Ejercicios:

#Ejercicio 1: 
"""Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"
Solo debes definir la función, no debes invocarla luego."""

def saludar():
    print("¡Hola mundo!")

#Ejercicio 2:
"""Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, 
y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
Solo debes definir la función y crear la variable, no debes invocar la función luego."""

nombre_persona = "Juan"

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

bienvenida(nombre_persona)

#Ejercicio 3:
"""Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, 
imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.
Solo debes definir la función y crear la variable, no debes invocar la función luego."""

un_numero = 16

def cuadrado(un_numero):
    print(un_numero * un_numero)

cuadrado(un_numero)

