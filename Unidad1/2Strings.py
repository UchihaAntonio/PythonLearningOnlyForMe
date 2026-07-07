#En python tenemos muchos tipos de datos, es decir que python maneja muchos tipos de datos y muy distintos, hoy 
#veremos el tipo de dato string, que significa una cadena de texto, es por eso que ponemos comillas,
#Para indicarle a python donde comienza la cadena y donde termina.
#Pero no solo puede contener texto, todos los datos que se encuentren dentro de este dato serán tomados como texto
#Espacios, signos, numeros, es decir que no se pueden hacer operaciones con este tipo de dato
#Mira el siguiente ejemplo

print("100 + 50")

#Esa línea de texto no hace nada, por que es una cadena de texto (STRING)
#No puede hacer nada por que python lo interpreta como si solo fuera texto 

#Aunque antes te he mencionado que no se pueden hacer operaciones aritmeticas con estos datos, hay una operación que sí se puede
#realizar. Esta se llama la CONCATENACION, es decir, que "Sumamos" algo, en este caso no las sumamos, lo que hacemos es ponerl
#Un string a un lado del otro.

print("Hola MI nombre es " + "Juan Antonio")

#Pero además de eso python nos ofrece algunas funciones especiales, como lo son las funciones dentro de string
#Para acceder a ellas tenemos que usar la barra Invertida (---> \ <---) y con esa barra podemos hacer que python tenga nuevas funciones
#Como por ejemplo que salte de renglón. Mira:

print("Hola Mi Nombre es\nJuan Antonio")

#Y podemos usar una tabulación o un espacio, mira este ejemplo:

print("\tEstoy mas de lado!")  #<----- Es como aplicar una sangría

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Ejercicios
#1.- Crea un código que imprima en pantalla la siguiente expresión (pero usando print una sola vez):
#Línea 1
#Línea 2
#Línea 3

#2.- Crea un código que imprima en pantalla la siguiente expresión.
#A	B	C
#D	E	F
#G	H	I

#3.- Crea un código que imprima en pantalla la siguiente expresión:
#Barra Normal: /
#Barra Invertida: \