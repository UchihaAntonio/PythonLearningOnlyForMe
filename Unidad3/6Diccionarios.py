"""Bueno, vamos con un concepto muy interesante, los Diccionarios

En python podemos pensar en un diccionario como un diccionario de la vida real
Ya que seún una clave, osea una palabra, esta va asociada con una definición, 
es decir un contenido para esa palabra.

Un diccionario es una colección de Pares. y cada par tiene una clave y un 
valor asociado a esa Clave. Estas claves no pueden repetirse, deben ser unicas

Un diccionario en python se escribe de la siguiente manera:

Mi_Diccionario = { 'Clave1': 'Valor1','Clave2': 'Valor2','Clave3': 'Valor3'}"""
#A diferencia de las listas los diccionarios no tienen un índice, por lo que no 
#podremos utilizar el metodo índex

"""En los diccionarios, a python no le importa el orden y a nosotros tampoco,
así que no te preocupes por el orden en el que lo escribas, python no le puede
dar un orden ni nada por el estilo, entonces no sirve de nada que los ordenes
Además de que no podremos utilizar ninguno de los métodos de ordenamiento que 
conoces hasta este momento"""

#A python lo que le importa es la relación de la clave y su contenido

#Entonces, se utilizan los diccionarios para guardar el contenido de algo sin 
#Saber su ubicación, mediante el uso de una clave.

#Así que vamos a crear nuestro primer diccionario

Diccionario = {"Clave1" : "Valor1", "Clave2" : "Valor2"}
#Para ver su contenido sería de la siguiente manera

print(Diccionario) #Una cosa que puede pasar, es que lo valores sí se pueden 
#repetir, las Claves NO!

#Pero que pasa si solo quiero que me imprima lo que tenemos en 
#la clave 2, sencillo, lo almacenamos en una variable y 
#la imprimimos

resultado = Diccionario["Clave2"]
print(resultado)

#Pero ahora veamos un caso de la vida Real
#Supongamos que queremos guardar todos los datos de un cliente

Cliente = {"Nombre":"Juan", "Apellido":"Aragón", "Peso":75, "Talla":175.5}
#Y ahora nosotros podremos hacer consultas como si se tratase de una base de
#Datos

Consulta = Cliente["Nombre"]
print(Consulta)

"""Incluso dentro de los diccionarios podemos almacenar listas"""
"""Y tambien podemos tener un poco de recursividad, que es otro de las 
grandes bonanzas que tiene python, esto nos quiere decir que podemos 
almacenar un diccionario dentro de otro diccionario"""

DIC = {"Clave1":55, "Clave2":[10,12,13,154,6000], "Clave3":11.1, "Clave4":{"SubClave1":"SubValor1"}}
#En el diccionario de Arriba tenemos un valor INT, un FLOAT, una LISTA
#Y un diccionario
#Podemos hacer consultas de una clave dentro del diccionario, así 
#Como consultar una posición de la lista en específico o 
#Consultar una clave del diccionario que están dentro de nuestro primer 
#Diccionario

print(DIC["Clave2"])
# y así llamamos la lista en la posición 2
print(DIC["Clave2"][1])
#Y así accedemos a la subclave 1 del diccionario recursivo
print(DIC["Clave4"]["SubClave1"])

#Tomando de ejemplo el diccionario DIC, si quiero agregar más elementos se 
#Hace de la siguiente manera

DIC["Clave5"] = "ESTE ES EL VALOR 5!!!!!"
print(DIC) #Se agregó hasta el final del Diccionario

#Pero que pasa si quiero sobre escribir el valor de la clave 2?

DIC["Clave2"] = "AhoraEstaeslaClave2"
print(DIC)

"""ASí como los demás tipos de datos, este tipo de datos tiene sus propios Métodos
Como el método KEYS, que muestra todas las claves dentro del diccionario"""

print(DIC.keys()) 

"""ASí como tambien podemos mostrar solo los valores con el siguiente método"""
print(DIC.values()) 

#Prueba que hace el método Items y averigualo tu mism@

"""---------------------------------------------------------------------------------------"""
"""Ejercicios"""

#1.-Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

"""nombre: Karen

apellido: Jurgens

edad: 35

ocupacion: Periodista""" "Imprime el diccionario"

#2.-Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que 
#se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves 
#y/o índices según corresponda.
"""mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}"""

#3.- mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
"""Actualiza la información de nuestro diccionario llamado mi_dic
(reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" 
(sin tilde). 

Los nuevos datos son:

nombre: Karen
apellido: Jurgens
edad: 36
ocupacion: Editora
pais: Colombia

para ello, no debes cambiar la línea de código ya escrita, sino actualizar 
los valores mediante métodos de diccionarios."""