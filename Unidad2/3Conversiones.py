#----------------------------------------------------------------------------------------
#En python, una variable puede pasar por varias transformaciones
#Por ejemplo en una misma ejecución puede pasar por una variable INT, a STRING
#Y si se necesita volver a ser INT

#A este proceso se le conoce como **"CASTING" o "CASTEO"**
#Y Existe de 2 tipos ----------------------------------> IMPLICITO y EXPLICITO

#Implícita: Ocurre cuando python convierte el tipo de dato automáticamente en otro
            #Sin necesidad de que el usuario haga nada

#Explícitas: Es cuando python necesita que el usuario haga algo en el código para 
            #Convertir un tipo de dato a otro para la ejecución del código.
#----------------------------------------------------------------------------------------

#=======================================================================================
#Veamos unos ejemplos para que este proceso de "CASTEO" se vea más claro
num1 = 20
num2 = 30.5
print(type(num1))
print(type(num2))
#Esto nos imprime el respectivo tipo de dato que está almacenado en esa variable

#=======================================================================================
#¿Pero que pasaría sí en medio de la ejecución sobre escribimos el tipo de dato de num1?
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))
#Ahora esto nos imprime dos FLOATS, esto es una conversión IMPLICITA,
#Por que nosotros no hicimos nada, python lo hizo solito

#=======================================================================================
#¿Pero cómo haríamos para que sea una Conversión "explícita"?
#Veamos el siguiente ejemplo:
numero1 = 5.8
print(numero1)
print(type(numero1))

#Pero ahora exigiremos que este FLOAT se convierta en un INT
numero2 = int(numero1)
print(numero2)
print(type(numero2))
#Así es como casteamos una variable y la forzamos a ser del tipo que necesitemos.
#Pero debemos notar que esto no redondea, por que sinó lo hubiese redondeado a 6
#Sinó lo que hace es que quita los decimales para que sea un tipo de dato INT

#=======================================================================================
#Ahora recordemos el ejercicio que no pudimos realizar en ejercicios anteriores
edad = input("Dime tu edad: ")
print(type(edad)) #------------------------>Nos imprime el tipo de dato

edad = int(edad) #------------------------->Aquí debió cambiar el tipo de dato de STR a INT
print(type(edad)) #---->Comprobamos imprimiendo

nueva_edad = 1 + edad
print("Cumplirás: ", nueva_edad)
#Ahora gracias a este casteo podemos hacer operaciones con edad, Convertimos edad de ser 
#Un STRING a INT con un "CASTEO" explícito

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#EJERCICIOS

#1.- Convierte el valor de num1 en un int e imprime el tipo de dato que resulta
        #num1 = 8.8

#2.- Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
        #num2 = 8

#3.- Suma los valores de num1 y num2. No modifiques el valor de las variables ya declaradas, 
        #sino aplica las conversiones necesarias dentro de la función print().

