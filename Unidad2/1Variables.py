#--------------------------------Variables-------------------------------------------
#Una variable es como una cajita, puedes meter en ella distintos tipos de datos
#En python una variable es un espacio en memoria reservado para lo que sea 
#Que quiera meter en ese espacio.
#Y ese mismo contenido puede cambiar las veces que sea necesario, por eso la llamamos
#Variable, por que varía su contenido.

#Veamos un ejemplo: 

nombre = "Juan"

#Por lo tanto, si quiero imprimir la variable nombre lo haría de esta manera:

print(nombre)

#Se imprime tal cual, pero el contenido de una variable puede cambiar durante
#la ejecución del código, por ejemplo.

#nombre = "Antonio"

#Si yo ahora imprimo esto, el contenido de la variable ha variado.
#print(nombre)

#Y no solo podemos hacer esto con texto, tambien con int y float
#edad = 23
#print(edad)

#Además de que podemos hacer operaciones matemáticas dentro de las variables 
#Siempre y cuando tenga valores numéricos.

#Otra de las funciones más poderosas de python es que podemos asignar
#Directamente el contenido que nos ha dado un usuario a una de nuestras variables
#Por ejemplo:

Name = input("Dame tu Nombre Individuo! \n")
print("Tu nombre es : " + Name)

#Incluso dentro de las variables podemos hacer concatenaciones, mira este ejemplo:

Palabra1 = "Hola"
Palabra2 = "Mundo"

Frase = Palabra1 + Palabra2

print(Frase)

#--------------------------------------------------------------------------------------------


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@EJERCICIOS@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#1.- Declara dos variables, llamadas nombre y edad.
    #Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

#2.- Crea tres variables:
    #nombre
    #apellido
    #nombrecompleto

    #A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". 
    #Finalmente, construye la variable nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio). 

#3.-Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
        #"Estás tomando un curso de curso"

    #Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable. 
    #Recuerda agregar un espacio antes de concatenar la variable al resto del texto.