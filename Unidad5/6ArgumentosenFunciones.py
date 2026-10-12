"""
===========================================================
        ARGUMENTOS EN LAS FUNCIONES DE PYTHON
===========================================================

1) PARÁMETRO vs ARGUMENTO (la diferencia más importante)
-----------------------------------------------------------
- PARÁMETRO: es la "variable" que escribes al DEFINIR la función.
- ARGUMENTO: es el "valor real" que envías al LLAMAR la función.

    def saludar(nombre):   # <- 'nombre' es el PARÁMETRO
        print(nombre)

    saludar("Ana")         # <- "Ana" es el ARGUMENTO

Piénsalo así: el parámetro es la caja vacía, el argumento es lo que
metes dentro de la caja cuando usas la función.


2) ¿CÓMO FUNCIONA POR DENTRO?
-----------------------------------------------------------
Cuando llamas a la función:
  a) Python evalúa los argumentos (calcula sus valores).
  b) Crea un espacio de memoria nuevo (scope local) para esa llamada.
  c) "Ata" (asigna) cada argumento a su parámetro correspondiente.
  d) Ejecuta el cuerpo de la función.
  e) Devuelve el valor del 'return' (si no hay return, devuelve None)
     y destruye el espacio local.

Los parámetros SOLO existen dentro de la función (ámbito local).


3) TIPOS DE ARGUMENTOS
-----------------------------------------------------------
a) POSICIONALES: se asignan según el ORDEN.
       def dividir(a, b): ...
       dividir(10, 2)     -> a=10, b=2   (¡el orden importa!)

b) POR NOMBRE / KEYWORD: se asignan por el NOMBRE del parámetro.
       dividir(b=2, a=10) -> el orden ya no importa

c) POR DEFECTO (opcionales): tienen un valor si no los envías.
       def saludar(nombre, saludo="Hola"): ...
       Regla: los parámetros con valor por defecto van SIEMPRE al final.

d) *args  -> recibe MUCHOS argumentos posicionales como una TUPLA.
e) **kwargs -> recibe MUCHOS argumentos con nombre como un DICCIONARIO.

Orden obligatorio al definir:
       def f(posicionales, con_default=..., *args, **kwargs)


4) PASO POR "ASIGNACIÓN DE OBJETO" (ojo con esto)
-----------------------------------------------------------
Python NO copia los valores, pasa una REFERENCIA al objeto:
- Si el objeto es INMUTABLE (int, float, str, tuple), reasignarlo dentro
  de la función NO afecta al de afuera.
- Si el objeto es MUTABLE (list, dict, set), modificarlo dentro
  (append, [0]=..., etc.) SÍ afecta al de afuera.

⚠ Nunca uses una lista/diccionario como valor por defecto:
       def mal(lista=[]):   # se comparte entre TODAS las llamadas
       def bien(lista=None): # forma correcta
           if lista is None:
               lista = []


5) IDEA GENERAL (no solo Python)
-----------------------------------------------------------
Los argumentos son el CANAL DE ENTRADA de datos a una función:
entran argumentos -> se procesan -> sale un 'return'.
Gracias a ellos una función es GENÉRICA y REUTILIZABLE, en vez de
depender de variables globales fijas.
"""

# ==========================================================
# EJEMPLO 1: Posicionales, por nombre y valor por defecto
# ==========================================================

# 'nombre' es obligatorio; 'saludo' e 'signo' tienen valor por defecto
def saludar(nombre, saludo="Hola", signo="!"):
    # dentro de la función, los parámetros se usan como variables normales
    return f"{saludo}, {nombre}{signo}"


print("--- EJEMPLO 1 ---")
print(saludar("Ana"))                      # usa los valores por defecto
print(saludar("Luis", "Buenos días"))      # posicional: 2do valor -> saludo
print(saludar(saludo="Qué onda", nombre="Sofía"))  # por nombre: el orden da igual
print(saludar("Marco", signo="?"))         # mezcla: posicional + keyword


# ==========================================================
# EJEMPLO 2: *args y **kwargs (cantidad variable de argumentos)
# ==========================================================

# *notas    -> junta todos los argumentos posicionales en una TUPLA
# **datos   -> junta todos los argumentos con nombre en un DICCIONARIO
def reporte(alumno, *notas, aprobatoria=6, **datos):
    print(f"\nAlumno: {alumno}")
    print(f"Notas recibidas (tupla): {notas}")

    # si no se enviaron notas, evitamos dividir entre cero
    promedio = sum(notas) / len(notas) if notas else 0
    print(f"Promedio: {promedio:.2f}")
    print("Estado:", "APROBADO" if promedio >= aprobatoria else "REPROBADO")

    # recorremos los datos extra que llegaron como diccionario
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")


print("\n--- EJEMPLO 2 ---")
reporte("Ana", 8, 9, 10)                       # 3 notas, aprobatoria por defecto
reporte("Luis", 5, 6, 4, aprobatoria=7,        # cambiamos la calificación mínima
        grupo="B2", turno="Matutino")          # estos van a **datos


# ==========================================================
# EJEMPLO 3: Mutable vs Inmutable (cómo viaja el argumento)
# ==========================================================

def intentar_cambiar_numero(numero):
    # 'numero' es un int (INMUTABLE): esto crea un objeto NUEVO,
    # solo cambia la variable local, no la de afuera.
    numero = numero + 100
    print("  dentro de la función  ->", numero)


def agregar_producto(carrito, producto):
    # 'carrito' es una lista (MUTABLE): append MODIFICA el mismo objeto,
    # por lo que el cambio SÍ se ve fuera de la función.
    carrito.append(producto)
    print("  dentro de la función  ->", carrito)


# Forma correcta de usar un valor por defecto mutable
def crear_lista(item, lista=None):
    if lista is None:      # así cada llamada arranca con su propia lista
        lista = []
    lista.append(item)
    return lista


print("\n--- EJEMPLO 3 ---")
mi_numero = 10
print("antes (inmutable)      ->", mi_numero)
intentar_cambiar_numero(mi_numero)
print("después (inmutable)    ->", mi_numero, "  # NO cambió")

mi_carrito = ["pan"]
print("\nantes (mutable)        ->", mi_carrito)
agregar_producto(mi_carrito, "leche")
print("después (mutable)      ->", mi_carrito, "  # SÍ cambió")

print("\nvalor por defecto seguro:")
print(crear_lista("a"))   # ['a']
print(crear_lista("b"))   # ['b']  y NO ['a', 'b']
