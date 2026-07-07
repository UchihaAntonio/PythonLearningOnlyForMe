#-----------------------------------------------------------------------------------
#Los operadores matemáticos son simplemente aquellos simbolos que representan 
#Una operación aritmética, como lo son:  + - / *
#Veamos el siguiente ejemplo:

x = 6
y = 2

print(f"{x} mas {y} es igual a {x+y}")

#Okay Ahora hagamos todas las operaciones
print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} entre {y} es igual a {x/y}")

#Ahora pongamos una variable más
z = 7 #<-------------------------------- Se pueden declarar variables en CUALQUIER parte

#Ahora Haremos una división al Piso
#Esta lo que hace es que si un numero en una división tiene decimales
#Es decir que lo redondea al numero entero menor

print(f"{z} dividido al piso de {y} es igual a {z//y}") #<-----La doble barra es el operador

#Pero no solo eso, tambien tenemos el módulo, que lo que hace es devolver el residuo de 
#Una división, veamos

print(f"{z} modulo de {y} es igual a {z%y}")

#¡Y tambien podemos hacer potencias!
print(f"{x} elevado a la potencia de {y} es igual a {x**y}")
#Y lo podemos hacer sin variables también
print(f"{x} elevado a la potencia de {3} es igual a {x**3}")
#Y también tenemos raíces!
print(f"{x} raíz cuadrada es igual a {x**0.5}")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Ejercicios

#1.- Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.

#2.- Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.

#3.- Calcula y muestra en pantalla la raíz cuadrada de 783.
