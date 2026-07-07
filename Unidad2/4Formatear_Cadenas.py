#-----------------------------------------------------------------------------------
#Suponiendo que tenemos la información de varios datos en una cadena
#Y queremos representar de manera que los datos estén juntos, hasta ahora lo que
#Teníamos que hacer es hacer "CASTING" a los datos para poder concatenarlos
#Pero en python tenemos dos metodos para Formatear las cadenas.

#Por ejemplo: Si tenemos los siguientes datos:

    #color_auto = "ROJO"
    #matricula = 2356

    #Y queremos imprimir lo siguiente:
        #print("MI auto es "ROJO" y la matricula es 2356")

        #Tendríamos que hacer concatenaciones muy largas
            #print("Mi auto es color", + color_auto, + "Y la matrícula es", + matricula)

#Pero para evitar eso podemos utilizar el Formateo de cadenas.
#La primer manera es utilizar la función "format", utilizemos el ejemplo anterior
            #print("Mi auto es color {} y la matricula es {}".format(color_auto,matricula))
        #Lo que hace "format" es que presenta las variables como si fueran string, sin necesidad de castear nada

#Y ahora vamos con el segundo método "Cadenas Literales"
    #Utilizemos el ejemplo pasado:
            #print(f "Mi auto es color {color_auto} y la matricula es {matricula}") <---------Esto solo funciona con python3


#-----------------------------------------------------------------------------------
#Supongamos que queremos imprimir en una oración 2 variables INT
x = 10
y = 5

#Normalmente lo que haríamos sería:
print("Mis numeros son "+ str(x) + " y " + str(y))

#Pero para poder evitar eso, utilizaremos primero la función Format

print("Mis numeros son {} y {}" .format(x, y))

#Incluso podemos hacer operaciones utilizando esta función
print("La suma de mis numeros {} y {} es igual a = {}" .format(x, y, x+y))
#Esta es una muy buena manera de hacerlo, pero casi no se usa o se dejó de usar por que es poco
#Legible para el ojo humano, así que la mayoría de los programadores no utilizamos esta manera
#Por lo que se implementó la siguiente función.

#Veamos
color = "Rojo"
matricula = 1234

#Implementemos la función de cadenas literales
print(f"El Auto es color {color} y  la matrícula es {matricula}")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Ejercicios
#1.- Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
     #Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
        #Utiliza las Variables:
            #nombre_asociado = "Jesse Pinkman"
            #numero_asociado = 399058

#2.- Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
     #Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
        #Utiliza las Variables:
            #puntos_nuevos = 350
            #puntos_totales = 1225

#3.- Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
     #Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

    #En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
        #Utiliza las siguientes variables
            #puntos_anteriores = 875
            #puntos_nuevos = 350