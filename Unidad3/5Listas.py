#Vaya, se vienen los tipos de datos complejos, pero creo que estas List@ para manejarlo
#Así que comencemos con las LISTAS

"""Una lista es una secuencia ordenada de Objetos."""

"""Dicha colección de objetos puede ser asignada a una variable, y el contenido  
de la misma puede contener cualquier tipo de datos de los que hemos visto 
hasta el momento, incluso puede contener distintos tipos de dato en una misma
lista al mismo tiempo"""

"""Debe estar escrita entre corchetes y sus elementos deben estar separados por
comas, algo así 

Lista = [0,1,2,3,4,"Hola", "Mundo"]     <-----------------"""

"""Una de las herramientas más poderosas de python es que nos dá la posibilidad
de anidar las listas, es decir, construir una lista de listas, mira el ejemplo"""
#Lista de Listas
Lista = [[1,2,3,4,5], ["Hola", "Mundo"]]  #<--- Los números son la sublista 1
#Y el texto es nuestra sublista 2

#Y ambas listas son el contenido de nuestra Lista que guardamos en la variable
#--------> Lista

"""Las listas comparten muchos métodos con los strings, como lo son:
Index
Slicing
len
Que son las principales.

Pero aquí viene su principal diferencia de los string.

LAS LISTAS NO SON INMUTABLES (Lo que nos permite modificar su contenido)"""

#Así que pasemos a algunos detalles importantes de las listas
#Primero identifiquemos como se ve su tipo de dato en la consola

mi_lista = ["A", "B", "C", "a", "b", "c"]
print(type(mi_lista)) #<------ Se debe imprimir el tipo de dato

#Tambien podemos preguntar a python el tamaño de nuestra lista
print(len (mi_lista))

#Veamos como se usa el INDEX en una lista
print(mi_lista[2]) #<--- Esto debe imprimir el caracter en la posición 3
#Recuerda que en informatica contamos desde el 0

#Otro Ejemplo
print(mi_lista[0:2])  #<---Recuerdas esto verdad?

#Incluso podemos CONCATENAR las listas, observa bien 
mi_lista2 = ["X", "Y", "Z", "x", "y", "z"]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)#<---- Esto nos creará una sola lista con todos
#los elementos de las 2 listas anteriores

"""Pero como te lo había comentado antes, la diferencia
principal de los strings es que podemos modificar su contenido"""
#Intentemos cambiar el contenido de la lista 3

mi_lista3[0] = "Alfa" 
print(mi_lista3)
#Lo notaste?

"""En las listas tendremos nuevos métodos para trabajar con estas, por ejemplo
Append"""

mi_lista3.append("Epsilon")
print(mi_lista3) #Entonces lo que hace append es agregar un elemento a la lista
#Con la que estemos trabajando

"""Ahora vamos con uno de los métodos más importantes en cualquier lenguaje de programación

--- POP ---

ES una cosa muy sencilla, lo que hace es que elimina un elemento de la línea
Python cuenta con ese método por defecto, pero en otros lenguajes de programación, C, 
por ejemplo,tu tienes que crear ese método desde 0"""

#Intentemos eliminar "Alfa"
mi_lista3.pop(0) #<-- Si dejas vaciós los paréntesis, python interpretará que solo quieres
#eliminar el último elemento de la lista. En cambio, si pones el índice, este método eliminará
#el elemento que corresponda al índice
print(mi_lista3)

"""Python es muy bondadoso y nos permite guardar las cosas que hayamos borrado, por si queremos
manipular esa información más adelante, así que podemos hacer algo como esto"""

eliminado = mi_lista3.pop(0)
print(mi_lista3)
print(eliminado) #Sencillo no? Imagina las posibilidades para esto

"""Otro de los métodos interesantes de las listas es uno que nos deja ordenarla"""
Listilla = ["k", "z", "a", "t", "p", "r"] #(Una lista desordenada)

#Ordenamos con SORT
Listilla.sort()
print(Listilla)  #<-- La imprime ya ordenada

#Esto lo hace independientemente el tipo de datos, ya sea int, string o float

###Importante, el método Sort no devuelve nada, es decir, que cuando lo usas no puedes 
###Asígnarlo a una variable, por que sí lo haces te mostrará la variable como vacía
"""YA QUE SORT NO FUNCIONA DE ESA MANERA"""

#Sort lo hace de orden alfabético o de mayor a menor, así que hay otro método.
#Se llama REVERSE, pero creo te imaginas que es lo que hace, inténtalo y me dices.

"""---------------------------------------------------------------------------------------"""
"""Ejercicios"""

#1.-Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

#2.-Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
"""medios_transporte = ["avión", "auto", "barco", "bicicleta"]"""
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método 
# apropiado de listas para añadir un nuevo elemento.

#3.-Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, 
# y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin 
# alterar la línea de código ya suministrada.
"""frutas = ["manzana", "banana", "mango", "cereza", "sandía"]"""