#---------------------Enteros y Flotantes----------------------
mi_numero = 1
print(mi_numero)
#Existe una función que se llama Type ---> Esta nos devuelve el tipo de dato de la variable
#Así como se muestra a continuación
print(type(mi_numero))

#-------------------------------------------------------------
#Una Variable puede que no solo esté constituida por un valor
#Tambien puede ser constituida por una operación como mi_numero = 1 + 3
#Continuemos con el ejemplo
mi_numero2 = 1 + 3
print(mi_numero2 + mi_numero2)
print(type(mi_numero2))

#-------------------------------------------------------------
#Pero tambien podemos hacer que una variable sea de tipo FLOAT, 
#Simplemente escribimos lo siguiente
mi_numero3 = 5.8
#Y tambien podemos hacer operaciones entre variables
#Pero cuando detecta que es una variable float, por que es la que tiene la prioridad
#Se queda como una variable de tipo Float
print(mi_numero3)
print(type(mi_numero3))

#-------------------------------------------------------------
#Inclusive podemos seguir haciendo operaciones aunque el tipo de dato sea FLOAT
print(mi_numero3 + mi_numero3)
print(type(mi_numero3))

#-------------------------------------------------------------
#Pero que pasaría si la variable contase con dos tipos de dato
#INTEGER y FLOAT
mi_numero4 = 5 + 5.8
print(mi_numero4)
print(type(mi_numero4))
#El resultado es Float, por que no importa el tipo de dato
#Sinó el tipo de dato que resulta de la operación

#-------------------------------------------------------------
#Vayamos a un problema más complejo
edad = input("Dime tu edad: ")
#Es decir que asignamos un valor a la variable edad, dependiendo 
#De lo que el usuario haya ingresado, veamos el resultado
print("Tu edad es: ", edad)

#Entonces, esto podría indicarnos que podemos hacer operaciones
#De variables como en los ejemplos pasados, intentemos una suma

#nueva_edad = edad + 1
#print("Vas a Cumplir: " + nueva_edad) #<--------------- Esto nos arroja un error

#Por que no podempos concatenar un Tipo de dato INTEGER con un STRING
#Esto nos indica que cuando el usuario tecleo el valor de la variable edad
#La variable adoptó la forma de un STRING, imprimamos el tipo de Variable
print(type(edad))

#-------------------------------------------------------------
#Entonces ¿Qué es lo que pasaría si agregamos un signo de "+"?
edad = edad + edad
print(edad)
# Lo que hace no es una suma, es una concatenación de dos STRINGS
#Es decir, que junta el "23" y el "23"

#======================================================================
#EJERCICIOS

#1.-Declara una Variable que se llame: "num_entero", que sea de tipo entero
    #Imprime su tipo

#2.- ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.
    #Para ello, crea dos variables:
    #num1 = 7.5
    #num2 = 2.5
    #A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.