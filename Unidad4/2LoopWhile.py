"""Bien, en la clase pasada pudimos ver lo que es el ciclo FOR que es un ciclo que se cumple
o se repite una cantidad determinada de veces, ahora veremos el ciclo while, que basicamente es como 
un For con un IF, es un ciclo que se cumplirá mientras una condición se cumpla.

Es decír, que lo podemos interpretar como dice su nombre, Repeat While.

Repite Mientras

Y cuando la condición no se cumple, es cuando para de repetirse

Entonces podemos decir que tiene una salida Booleana ya que solo es verdadero o Falso"""

#Pero debes tener cuidado por que puedes generar un loop infinito que acabe con tu pc y ocasione 
#un pantallazo azul

"""Ahora veamos un ejemplo"""

Monedas = 10

while Monedas > 0 and Monedas < 15:
    Monedas = Monedas + 1
    print(f"Tienes {Monedas} monedas")


#Una vez entendido el ciclo For, y el IF
#Es muy sencillo entender el ciclo While

#Es una manera sencilla de poder controlar las veces que queramos que algo se repita determinadas veces.
#Pero tambien podemos perder el control de cuantas veces algo se repetira, pero solo hasta cierto caso
#Por que de todas maneras podemos hacer que se detenga de manera automatica con la condicion del while

#Mira este Ejemplo

Entrada = "s"

while Entrada == "s":
    Entrada = input("Quieres continuar con este Ciclo?    (s/n) ")

else:
    print("Gracias por participar")

"""Pero dentro del ciclo While tendremos algunas palabras que nos ayudaran con el flujo de ejecucion de nuestro programa

Por ejemplo la palabra PASS, que es simple, lo que hara es que simplemente no tomara el cuenta el ciclo while, pero esto es como 
si nos lo saltasemos a proposito, esto es util para cuando quieres seguir programando y aun no tienes con que llenar el ciclo While"""

#Y tenemos la palabra BREAK, que lo que hace es que podemos interrumpir por la fuerza un ciclo.
#Como por ejemplo para que no se cicle de manera infinita un while

#Mira este ejemplo

nombre = input("Dame un nombre    ")

for a in nombre:
    if a == 'a': #Basicamente lo que hara, es que imprimira lo que el usuario haya tecleado hasta 
        break   #Encontrarse con la letra que nosotros le hayamos indicado, en este caso la 'a'
    print(a)

#Pero podemos hacer que lo reanude, utilizando la palabra CONTINUE
for a in nombre:
    if a == 'a':
        continue  
    print(a)


#Sencillo no? 
#Muy bien, ahora te toca a ti

#Hora de Practicar 
"""---------------------------------------------------------------------------------------"""
"""Ejercicios"""

#1.-Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

#2.-Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) 
# con las siguientes condiciones adicionales:

"""Si el número es divisible por 5, mostrar dicho número en pantalla 
(¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla 
(no te olvides de seguir restando para que el programa no corra infinitamente)."""

#3.-Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos,
#  e interrumpe el flujo en el momento que encuentres un valor negativo:

"""lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]"""
#No debes cambiar el orden de la lista.