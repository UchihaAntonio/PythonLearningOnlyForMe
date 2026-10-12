"""
Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada 
de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""

def suma_cuadrados(*args):
    total = 0
    j = 0
    for i in args:
        j = i
        j = pow(j, 2)
        print(j)
        total= total+j
    return total

"""
Práctica sobre Argumentos Indefinidos (*args) 2

Crea una función llamada suma_absolutos, que tome un conjunto de argumentos 
de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, 
que tome los valores sin signo y los sume, o lo que es lo mismo, los considere 
a todos -negativos y positivos- como positivos).
"""

def suma_absolutos(*args):
    j = 0
    for i in args:
        if i <= 0:
            i = abs(i)
        j = j + i
    return j


"""
Práctica sobre Argumentos Indefinidos (*args) 3

Crea una función llamada numeros_persona que reciba, 
como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

def numeros_persona(Nombre, *args):
    suma = 0 
    for i in args:
        suma = i + suma
    return f"{Nombre}, la suma de tus números es {suma}"

print(numeros_persona("Juan", 1,2,3))