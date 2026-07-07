"""El dia de hoy conoceremos los distintos metodos que python nos ofrece para
trabajar con los datos de tipo string, por ejemplo, comenzaremos con el 
metodo upper, ve el siguiente ejemplo."""

texto = "Bienvenida de Nuevo a Python"
print (texto) #Lo unico que pasa es que estamos imprimiento el texto
#En cambio si aplicamos el metodo upper, nuestro texto se convertira en solo caracteres en mayusculas.

Mayus = texto.upper()
print(Mayus) 
#Te diste cuenta?

"""Pero este metodo tambien funciona con indices, de modo que si queremos 
transformar solo un caracter y conocemos su indice dentro del string, podemos hacer que este sea el 
unico que se ponga en mayusculas"""
ejemplo1 = "Bienvenida de Nuevo a Python"
Mayus1 = ejemplo1[3].upper()
print(Mayus1) #Lo notaste?

"""Pero si hay un metodo para hacer todo en Mayus, debe haber uno para hacerlo en minusculas
y efectivamente, lo hay, este metodo es Lower y funciona de la misma manera"""

"""Pero ademas de eso tenemos otro metodo que se llama split, que separa nuestro string en elementos
y los guarda en un tipo de dato Lista, que se guarda entre corchetes, mira el ejemplo"""

SPLIT = texto.split()
print(SPLIT) #Ahora SPLIT es un tipo de Dato Lista, ya mas adelante trabajaremos con este tipo de dato
#Asi que no te preocupes por no entender de momento

"""Pero a este Metodo podemos pasarle un paramentro para que nos ayuda a separar mejor, por defecto
splitt separa los elementos utilizando el espacio, pero si nosotros dentro del parentesis del splitt
podemos decirle que caracter queremos que use como separador, como por ejemplo la "n" """
#Intenta hacer el metodo de splitt usando como separador la "n"

"""Pero si el metodo splitt divide, claro que hay uno para unir, se llama join, este metodo es muy 
importante por que no solo se usa en python, sino que tambien se usa en otros lenguajes de programacion
por ejemplo en sql que es un lenguaje dedicado a las bases de datos"""
#Mira el ejemplo

a = "Aprender"
b = "Python"
c = "es"
d = "Genial!!"
e = " " #Aqui solo hay un espacio, pero si splitt separa usando los espacios
#Ahora usaremos un espacio para unir con join

#Ahora queremos que esto nos lo junte todo en un elemento, podemos hacer que lo concatene, si claro
#Pero tambien podemos hacer el metodo join que es un poco mas rapido
#Y se ocupa menos codigo

frase = e.join([a,b,c,d])
print(frase) #interesante no?

"""En los metodos de string podemos encontrar cosas como FIND, que es un metodo parecido a INDEX
pero que este no da error cuando no encuentra algo, sino que regresa un -1, mira el ejemplo"""

FIND = "ABABABABABABABABABA"
#Y si le digo que busque una z, jamas la encontraria
encontrarz = FIND.find("z")
print(encontrarz) 
#El metodo index devolvia un error, FIND simplemente no da un -1

"""Y por ultimo tenemos el metodo replace que lo que hace es que busca un pedazo de nuestro 
string y lo reemplaza por otro, en este caso haremos una prueba con la variable FIND, no te confundas!"""

reemplazar = FIND.replace("B", "Z") #Aqui solo estamos haciendo que busque las B y las reemplaze por Z
print(reemplazar)
#Facil no?

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Ejercicios:

#1.- Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar." 

#2.- Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]

"""3.-Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas."""

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."



