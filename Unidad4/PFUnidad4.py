from random import randint, uniform, choice, random, shuffle    
NumeroRandom = randint(0, 101)

print("--------------------------------------------")
print("Juego de Azar!") 
print("-------------------------------------------- ")
nombre_usuario = input("Cual es tu Nommbre? \n\n")
print(f"\n\nBueno {nombre_usuario} He pensado un número entre el 1 y el 100 \n\n")

print("Tu trabajo será adivinar que número es, pero no te preocupes, tienes 8 oportunidades para adivinarlo.")

print(f"Bien, comencemos con tu primer intento {nombre_usuario} \n")

respuesta_usuario = int(input("Dame tu primer numero: "))

oportunidades = 8

while oportunidades > 1:
    if respuesta_usuario != NumeroRandom and respuesta_usuario > 0 and respuesta_usuario < 100:
        print("Parece que no haz atinado el numero, pero no te preocupes, aqui hay una pista \n")

        if respuesta_usuario < NumeroRandom:
            print("Tu Numero es menor al que he pensado\n")
            oportunidades = oportunidades - 1
            print(f"Te quedan {oportunidades} Intentos\n")
            respuesta_usuario = int(input("Dame tu numero: "))


        if respuesta_usuario > NumeroRandom:
            print("Tu Numero es Mayor al que he pensado\n")
            oportunidades = oportunidades - 1
            print(f"Te quedan {oportunidades} Intentos\n")
            respuesta_usuario = int(input("Dame tu numero: "))

    elif respuesta_usuario == NumeroRandom:
        print("Increible! Haz acertado\n")
        print(f"Y eso que te quedaban {oportunidades} intentos")
        break

    else:
        print("Lo siento, no es un numero Valido, Dame un numero Valido")
        respuesta_usuario = int(input("Dame un numero: "))

if oportunidades == 1:
    print("Lo siento, te haz quedado sin oportunidades, Vuelve a intentarlo mas tarde")