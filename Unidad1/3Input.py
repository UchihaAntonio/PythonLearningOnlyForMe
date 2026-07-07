#Hasta ahora hemos aprendido a utilizar la función PRINT, para que nos muestre cosas en pantalla, pero 
#¿Cómo hacemos que el usuario de nuestro programa no dé la información?

#Pues para eso haremos uso de la función INPUT, para que el usuario se capáz de volcar información dentro de nuestro Programa
#Pero la función INPUT no puede ir sola, necesitamos que vaya acompañada de PRINT
#Veamos el ejemplo:

#Si solo ponemos print()
print("Dame tu Nombre: ")

#No nos deja hacer nada dentro del programa
#Pero si escribimos:

input("Dame tu Nombre: ")

#Ya nos pide datos, pero no podemos hacer nada con ese dato, solo lo pidió y ya
#Pero si queremos que el dato que acabamos de pedir, se imprima, entonces usamos las dos funciones.

print(input("Dame tu Nombre: ")) #------>Esto sigue la jerarquía de operaciones, es decir que se ejecuta primero de adentro hacía afuera

#Entonces, si quiero hacer un programa que me pida mi nombre y aparte lo muestre, ¡Debemos concatenar funciones!
print("Tu nombre es:  " + input("Dame tu Nombre: "))

#Ahora, si ya viste como funcionan las funciones, trata de explicarme lo que genera el siguiente código:

print("Tu nombre es: " + input("Dime tu Nombre: ") + " " + input("Dame tu apellido: "))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Ejercicios
#---------------------------------------------------------------------------------------------------------
#1.- Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

#¿Qué estás estudiando?

#El código debe poder imprimir en pantalla lo ingresado por el usuario

#---------------------------------------------------------------------------------------------------------
#2.- Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

#¿En qué país vives?

#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

#---------------------------------------------------------------------------------------------------------
#3.- Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:

#Escribe tu nombre:
#Escribe tu apellido:

#El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.