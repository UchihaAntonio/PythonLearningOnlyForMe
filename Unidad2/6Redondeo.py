#En Python así como en las matemáticas, podemos hacer opeaciones con punto flotante
#Esto quiere decir que nosotros obtendremos resultados con decimales
#Python nos ofrece la posibilidad de reducir o de redondear esos resultados
#Veamos como se hace.
print(90/7)
#Pero ahora, si lo escribimos dentro de "ROUND"
print(round(90/7))

#Pero tambien lo podemos poner dentro de una variable como en el siguiente ejemplo
resultado = round(90/7)
print(resultado)

#Pero que pasa si yo quiero que solo me muestre 2 decimales
#Lo podemos hacer de la siguiente manera
valor = round(95.66666666666666666666666, 2)
valor2 = round(95.66666666666666666666666, 5)
print(valor)
print(valor2)