"""
Práctica Funciones Dinámicas 1

Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, y 
False si al menos uno de los valores es negativo. Crea una lista 
llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
"""

lista_numeros = [1,-2,3,4,5]

def todos_positivos(lista_numeros):
    for i in lista_numeros:
        if i < 0:
            return False
    return

print(lista_numeros)

print(todos_positivos(lista_numeros))


"""
Práctica Funciones Dinámicas 2

Crea una función (suma_menores) que sume los números de una lista 
(almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 
y menores a 1000, y devuelva el resultado de dicha suma.
"""

lista_numeros = [1,2,3,4,5,1,1000,2333,0,4000000,900]

def suma_menores(lista_numeros):
    total = 0
    for i in lista_numeros:
        if i > 0 and i < 1000:
            total = total + i
    return total

print(lista_numeros)
print(suma_menores(lista_numeros))

"""
Práctica Funciones Dinámicas 3

Crea una función (cantidad_pares) que cuente la cantidad de números 
pares que existen en una lista (lista_numeros), y devuelva 
el resultado de dicha cuenta.
"""

lista_numeros = [1, 50, 502, 755, 34]

def cantidad_pares(lista_numeros):
    pares = 0
    contpares = 0
    for i in lista_numeros:
        if i % 2 == 0:
            pares = pares + i
            contpares = contpares + 1
    return (contpares, pares)

print(lista_numeros)
print(cantidad_pares(lista_numeros))