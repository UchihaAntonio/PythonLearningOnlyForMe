"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio
"""

def devolver_distintos(num1, num2, num3):
    total = 0
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    if suma >= 15:
        return max(lista)
    elif suma <= 10:
        return min(lista)
    elif suma >10 and suma <15:
        lista.sort()
        return lista[1]

#print(devolver_distintos(1,5,7))

"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""

def Palabra_Devolver():
    Palabra = "Payaso"
    listaSet = set(Palabra)
    lista = list(listaSet)
    lista.sort()
    return lista

#print(Palabra_Devolver())

"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def Comprobar_Numeros(*args):
    RecibirNumeros = input("Dame una lista de Números separados por espacios")
    RecibirNumeros = list(RecibirNumeros).split(" ")
    #Convertir a numeros
    #for i in RecibirNumeros:
    #   entero = int (i)
    return RecibirNumeros

print(Comprobar_Numeros())


"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla
todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""