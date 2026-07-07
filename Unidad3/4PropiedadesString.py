#El día de Hoy veremos algunas propiedades de los strings, se podría decir
#Así que se podría decir que esta clase será mas teoría, pero aún así, practicaremos un poco.

"""Así que conzcamos una de sus propiedades más importantes"""
"""Los strings, son INMUTABLES, esto quiere decir que una vez que un string haya sido 
construido, no podrás hacer nada para cambiar su orden interno así como su contenido"""

"""Otra de las propiedades de un string es que pueden CONCATENARSE haciendo uso del signo
----> + <----"""

"""Pero tambien podemos multiplicar los strings esta es una operación distina
a la concatenación"""

"""Los Strings pueden ser multilineales, es decir que pueden albergar en su interior
saltos de línea, haciendo uso de las triples comillas."""

"""Y tambien puedes saber si un string contiene un substring, así como saber la 
longitud de un string"""

#Veamos un ejemplo de estas propiedades, comencemos con la INMUTABILIDAD
#Supongamos que tenemos un string
nombre = "Carina"

#Pero nos dimos cuenta que nos equivocamos y queremos que Carina se escriba con K
#Así que lo cambiamos.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nombre[0] = "K"
print(nombre)  #----------> Observa bien el error, dice que python no soporta esta acción
#Cuando termines borra estas líneas de código para que puedas seguir con la 
#Ejecución del programa
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Entonces lo que hago es sobrecargar mi función nombre
nombre = "Karina"

#Y ahora sí he podido cambiar el contenido de un string, pero...
#Realmente no, lo que pasa es que hemos cambiado el valor de una variable, le hemos
#creado dentro de ella un nuevo string, así que nunca lo modificamos, lo sobrecargamos

"""Para la concatenación ya lo hemos visto, por si no lo recuerdas te recomiendo que 
revises los apuntes de las clases anteriores"""

#Pero que pasa sí en vez de usar un "+", usamos un "*"
#Revisemoslo.
Apodo = "Kari"

print(Apodo * 10) #------> Es sencillo intuir su funcionamiento ¿No crees?

"""Ahora veamos lo que pasa si queremos que un string tenga dentro de sí 
un salto de línea, así que para eso escribiremos un poema"""

poema = """En líneas de código creamos, 
mundos enteros que imaginamos.
Bajo el brillo de un monitor,
nace la lógica y el error.

Con bucles y variables jugamos,
mientras funciones invocamos.
En cada bug, un reto escondido,
la solución siempre está al oído.

Teclas que danzan en armonía,
entre ceros y unos, la poesía.
Programar es arte en clave binaria,
un lenguaje que nunca cesa su magia."""
print(poema)

#Y así es como logramos que un string tenga saltos de línea, con unas simples comillas

#Y aprovechando que tenemos un poema, python tambien nos puede decir si tenemos un 
#sub string dentro de nuestro main string, mira el ejemplo.
print("error" in poema) #------> Este es un valor de tipo Booleano
                        #Así que solo nos dirá sí es verdadero o falso

#Y por último tenemos la posibilidad de calcular la longitud de nuestro String
#Calculemos la longitud de nuestro poema

print (len (poema)) #-----> Y con esto nos mostrará la longitud de nuestro poema.

"""---------------------------------------------------------------------------------------"""
"""Ejercicios"""

#1.-Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. 
# Por suerte, conoces que los strings son multiplicables y puedes realizar esta
# Actividad de forma simple y elegante.

#2.-Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
"""Tierra mojada,

mis recuerdos de viaje

entre las lluvias"""

#3.-Muestra en pantalla el largo (en números de caracteres) de la palabra "electroencefalografista"