#Sabemos que el tipo de Dato String es una cadena de caracteres.
#Entonces si nosotros queremos trabajar con este tipo de datos, nosotros debemos saber que cada caracter 
#Representa un número dependiendo la posición que ocupa dentro de la cadena.

#A eso se le llama el Indexeado, que cada caracter ocupa una posición dentro de la cadena.

#Por Ejemplo si tenemos la Siguiente Cadena: 

string = "Hola"

#Esto nos quedaría algo así, Donde: 
#"H" pertenece a la Posición 0
#"o" pertenece a la Posición 1
#"l" pertenece a la Posición 2
#"a" pertenece a la Posición 3

#Ojo, En programación siempre contamos comenzando en el 0!!  <----------

#Y tambien hay una manera de trabajar con el índice inverso que nos quedaría algo así:
#"H" pertenece a la Posición 0
#"o" pertenece a la Posición 3
#"l" pertenece a la Posición 2
#"a" pertenece a la Posición 1

#Entonces, dependiendo de lo que necesitemos python nos puede ayudar a extraer lo que 
#Necesitemos en todo momento para trabajar con el, por ejemplo:

#Supongamos que tenemos lo siguiente:

saludo = "HOLA" #Esta es una variable que contiene una cadena

#Si quiero saber en que posición se encuentra la "L" haría algo como esto:

print(saludo.index("L")) #Esto nos devolverá en que posición se encuenta la letra "L"

#En cambio si quiero saber que hay en la posición 1 haría algo como esto:

print(saludo[1]) #Esto nos devolverá lo que sea que haya en esa posición

#Este método nos ayuda a Buscar dentro de un String lo que necesitemos
#Por ejemplo, si necesitamos buscar una palabra completa se podría: 

cadena = "Hola, Bienvenido a Python"
resultado = cadena.index("Python")
print(resultado)

#Esto nos indica a partir de qué posición comienza la palabra "Python"
#Cuenta y verás que es correcto

#OJO: Este método distingue entre las Mayúsculas y minúsculas
#Para que tengas cuidado con tus búsquedas

#Además de que podemos hacer búsquedas con índice inverso de 
#la siguiente manera
variable = "Yo ya quería aprender Python"
posicion = variable.rindex("í")
print(posicion)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#EJERCICIOS
#1.- Encuentra y muestra en pantalla qué caracter ocupa la quinta 
        #posición dentro de la siguiente palabra: "ordenador"

#2.- Encuentra y muestra en pantalla el índice de la primera aparición de la palabra 
        #"práctica" en la siguiente frase:
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

#3.- Encuentra y muestra en pantalla el índice de la última aparición de la palabra 
        #"práctica" en la siguiente frase:
frase1 = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."


