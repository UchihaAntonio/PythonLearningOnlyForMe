"""Joder, vamos a empezar a programar en serio, desde ahora en adelante las cosas se van a poner feas

Así que comencemos con una de las herramientas mas poderosas que tienen todos los lenguajes de programación
Los Loops o ciclos.

Un ciclo es una sección de código que se repetirá de dos maneras, de manera definida por el usuario
O de manera indefinida.

Pero comenzaremos por la primera, el ciclo For

El ciclo for existe en todos los lenguajes de programación, la diferencia radica en su manera de operar
En nuestro caso en pyton tenemos un ciclo For poderoso, por que podemos hacer cosas que veremos más adelante


En primera instancia nosotros debemos conocer su estructura, en la asignación de classroom te dejé un 
PDF donde se explica de mejor manera como funciona el ciclo FOR, dale una leída, una anotada y después vuelves

¿Qué te parece?

Ahora veamos con un poco de práctica como funciona específicamente."""

#Primero crearemos una lista

ListaFor = ["a", "b", "c", "d"]

#Ahora definamos un for que muestre cada letra de nuestra Lista

for Letra in ListaFor:
    print(Letra)

#Lo que hace aquí nuestro ciclo es que por cada iteración, guarda el valor del índice 0
#En la Variable "Letra", después la imprime y vuelve a la lista 
#Encuentra el nuevo valor de Letra, que ahora es el índice 1, cuyo valor es: "b"
#Y lo imprime, hasta que no encuentra nada más que imprimir, entonces termina el ciclo

#Es por eso que python es un ciclo definido

"""Un apunte que considero importante, notaste que estamos usando una variable dentro de la 
estructura del FOR, esa variable es una variable que se denomina Local, existe dentro 
de nuestro programa, pero python por cuestiones de ahorro de memoria solo la tomará en cuenta
dentro del contexto del ciclo FOR, por lo que no existe fuera de ella, a no ser que lo indiquemos
así"""

#Ahora, suponiendo que entendiste a la perfección, podemos aplicar todo lo que previamente 
#has aprendido para hacer un ciclo for más complejo

for letter in ListaFor:
    NumLetra = ListaFor.index(letter) + 1
    print(f"Letra {NumLetra}: {letter}")

#Sí entiendes como es que esto funciona???

#Si no entiendes el por que de esto, llama a tu profe por que es muy importante que lo entiendas para poder avanzar

"""Veamos otro ejemplo para que te quede más claro"""

numeros = [1,2,3,4,5,6]
Mi_Valor = 0

for valor in numeros:
    Mi_Valor = Mi_Valor + valor

print(Mi_Valor)


#Pero Ahora que pasaría si quitamos el print de abajo y lo metemos al ciclo
#Es de lo que tienes que cuidar más dentro de tu programación

#Veamos otro ejemplo copn un string

Palabra = "Hola Mundo"

for z in Palabra:
    print(z) #Python lo que hace aquí es que nos imprimer cada elemento de 
    #nuestra cadena

#Pero tambien podemos hacer que python haga más cosas, como que por ejemplo
#Pasarle directamente la cadena, lista o diccionario al ciclo for, en vez de declararlo
#En otra línea. Mira

for Animales in "Mamiferos, Reptiles":
    print(Animales)

#Listas

for listaas in [1,2,3,4,5]:
    print(listaas)

#Lista de Listas
for listillas in [[1,2], [3,4]]:
    print(listillas)#Aquí nos imprime el valor de cada iteración de la variable listillas, pero
    #Pero podemos hacer que nos imprima en una variable el valor de cada elemento de la lista
    
for listillas1, listillas2 in [[1,2], [3,4]]:
    print(listillas1)
    print(listillas2)    #Aquí básicamente lo que hace es que guarda cada elemento en una lista
    #Primero el valor 1 de la primera lista
    #Luego el valor 2 de la primer lista
    #Luego el valor 1 de la 2da lista
    #Y finaliza con el valor 2 de la 2da Lista

#Con diccionarios
dic = {"Clave 1":"a", "Clave 2":"b", "Clave 3":"C"}
for Dic in dic:
    print(Dic) #Aquí solo se van a imprimir las claves

#Si queremos que se muestre completo sería de esta manera, haciendo uso de la propiedad .items

for Dic1 in dic.items():
    print(Dic1)

#Si ahora quiero que solo se muestren los valores lo puedo hacer con .values
for Dic2 in dic.values():
    print(Dic2)

#Hora de Practicar 
"""---------------------------------------------------------------------------------------"""
"""Ejercicios"""

#1.-Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
#Por ejemplo: "Hola María"
"""alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]"""

#2.-Dada la siguiente lista de números, realiza la suma de todos los números utilizando 
# loops For y almacena el resultado de la suma en una variable llamada suma_numeros
"""lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]"""

#3.- Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por 
# separado en las variables suma_pares y suma_impares respectivamente:

"""lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]"""

#*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar
"""
num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)
"""