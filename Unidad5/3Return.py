"""
Docstring for Unidad5.3Return

return es una palabra reservada en Python que se utiliza para finalizar la ejecución de una función y devolver un valor al lugar donde se llamó a la función. 
Cuando se ejecuta una declaración return, la función termina inmediatamente y el valor especificado después de return se devuelve al llamador.

Aquí hay un ejemplo de una función que utiliza return para devolver el resultado de una suma:
```python
def sumar(a, b):
    resultado = a + b
    return resultado

# Usando la función
print(sumar(3, 5))  # Esto imprimirá 8
print(sumar(10, 20)) # Esto imprimirá 30
"""

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

resultado = multiplicar(1, 2)
print(resultado)

#Ejercicio 1:
"""Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:"""

base = 2
exp = 3

def potencia(base, exp):
    return(base ** exp)
    
print(potencia(base, exp))

#Ejercicio 2:
"""Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y 
devuelva como resultado el monto equivalente en euros. 
A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.
Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros."""

dolares = 20

def usd_a_eur(dolares):
    return dolares * 0.9
    
print(usd_a_eur(dolares))

#Ejercicio 3:
"""Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el 
orden de sus caracteres y los devuelva de ese modo y en mayúsculas.
Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para 
sumisitrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos."""

word = "Python"
def invertir_palabra(word):
    word = word.upper()
    word = word[::-1]
    return word

print(invertir_palabra(word))

"""palabra = "hola"

def invertir_palabra(palabra):
    palabra = palabra.upper()
    palabra = palabra[::-1]
    print(palabra)


invertir_palabra(palabra)
"""

palabra = "hola"

def invertir_palabra(palabra):
    palabra = palabra.upper()
    palabra = palabra[::-1]
    return palabra


print(invertir_palabra(palabra))