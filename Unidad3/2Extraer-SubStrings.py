#El día de hoy aprenderemos a manejar strings de otra manera, 
#Es decir, a extraer porciones de texto que nosotros necesitemos, a esta operación se le llama:
#Slicing, o rebanado. 

#Para nosotros poder extraer caracteres de un string lo haríamos algo así

#Donde esta es nuestra Cadena de Texto:
mi_variable = "Esta es mi cadena de Texto"
print(mi_variable)
#Y para extraer una porción del texto lo haría de esta manera:
#Creo una variable donde almacenaré la información que extraiga de la variable
fragmento = mi_variable[11 : 18]
print(fragmento)

#¿Lo viste?, Se supone que tiene que imprimir la palabra "cadena"
#Pues si observas detenidamente cuando estoy extrayendo la palabra en la línea 13
#Le estamos dando un rango, que es un rando de índices, donde,
#Va a extraer todo lo que haya dentro de ese rango.

#Pero dentro del Rango [11 : 18], ponemos otro número, como por ejemplo
#[11 : 18 : 2], esto lo que hará es que extraerá el texto dependiendo del número
#Veámoslo en acción

texto_de_ejemplo = "0123456789" #Lo haremos con numeros para que sea visual
#Recuerda que al estar dentro de unas comillas estos números se comportarán 
#como un STRING
print(texto_de_ejemplo)

#Ahora extraigamos la ingormación de 2 en 2
extraccion = texto_de_ejemplo [0 : 10 : 2]
print(extraccion)

#Ahora, como dato curioso, si pones en el tercer número del rango un -1
#Este te arrojará la cadena leída al revés

extraccion_reves = texto_de_ejemplo[ :  : -1] #Si no pones nada dentro del
#primer rango, python lo interpreta como si fuera toda la cadena
print(extraccion_reves)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#EJERCICIOS
#1.- Extrae la primera palabra ("Extraer") de la siguiente frase utilizando slicing, 
# #y muéstrala en pantalla
frase = "Controlar la complejidad es la esencia de la programación"

#2.- Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, 
# e imprime el resultado.
frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

#3.- Invierte la posición de todos los caracteres de la siguiente frase y 
# muestra el resultado en pantalla.
frase3 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"