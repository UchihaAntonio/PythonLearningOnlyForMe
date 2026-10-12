"""
===============================================================================
                    **kwargs EN PYTHON (Argumentos con nombre indefinidos)
===============================================================================

1) ¿QUÉ SIGNIFICA?
   kwargs = "keyword arguments" (argumentos de palabra clave / con nombre).
   El nombre "kwargs" es solo una CONVENCIÓN, lo que realmente importa es el
   doble asterisco **. Podrías escribir **datos y funcionaría igual, pero por
   costumbre de la comunidad Python se usa **kwargs.

2) ¿PARA QUÉ SIRVE?
   Permite que una función reciba una CANTIDAD INDEFINIDA de argumentos que se
   pasan con la forma  nombre=valor.  Python los empaqueta automáticamente
   dentro de un DICCIONARIO.

       def f(**kwargs):
           print(kwargs)

       f(nombre="Ana", edad=30)   ->   {'nombre': 'Ana', 'edad': 30}

   Las CLAVES del diccionario son siempre strings (el nombre del argumento)
   y los VALORES son lo que hayas pasado (cualquier tipo de dato).

3) DIFERENCIA CON *args
   ---------------------------------------------------------------------------
   | *args                              | **kwargs                           |
   ---------------------------------------------------------------------------
   | Un solo asterisco                  | Doble asterisco                    |
   | Argumentos POSICIONALES            | Argumentos con NOMBRE (clave=valor)|
   | Se empaquetan en una TUPLA         | Se empaquetan en un DICCIONARIO    |
   | f(1, 2, 3)                         | f(a=1, b=2)                        |
   ---------------------------------------------------------------------------

4) ORDEN OBLIGATORIO DE LOS PARÁMETROS
   Python exige este orden al DEFINIR una función:

       def funcion(posicionales, *args, con_valor_por_defecto=x, **kwargs):

   Ejemplo real:
       def perfil(nombre, *hobbies, activo=True, **extras):
           ...
   Si pones **kwargs antes de otro parámetro -> SyntaxError.

5) EL OPERADOR ** TAMBIÉN "DESEMPAQUETA"
   El doble asterisco funciona en dos direcciones:
     - En la DEFINICIÓN de la función: EMPAQUETA (recoge) argumentos en un dict.
     - En la LLAMADA a la función: DESEMPAQUETA un dict en argumentos con nombre.

       datos = {"nombre": "Ana", "edad": 30}
       saludar(**datos)        # equivale a saludar(nombre="Ana", edad=30)

6) CÓMO SE TRABAJA CON kwargs DENTRO DE LA FUNCIÓN
   Como es un diccionario normal, puedes usar todos sus métodos:
       kwargs.items()          -> pares (clave, valor) para recorrer
       kwargs.keys()           -> solo las claves
       kwargs.values()         -> solo los valores
       kwargs.get("clave", 0)  -> valor seguro con default (no lanza error)
       "clave" in kwargs       -> comprobar si se envió ese argumento

7) ¿CUÁNDO USARLO EN LA VIDA REAL?
   - Configuraciones opcionales (ej: opciones de un gráfico, de una conexión).
   - Funciones "envoltorio" (decoradores) que deben pasar cualquier argumento
     que reciban a otra función sin conocerlos de antemano.
   - APIs flexibles donde el usuario puede mandar campos extra.

   OJO: abusar de **kwargs hace el código menos legible, porque quien lee la
   función no sabe qué argumentos acepta. Úsalo cuando de verdad aporte.
===============================================================================
"""


# =============================================================================
# EJEMPLO 1: Ficha de usuario -> recorrer el diccionario que crea **kwargs
# =============================================================================
# Objetivo: ver cómo Python empaqueta los argumentos con nombre en un dict
# y cómo recorrerlo con .items()

def ficha_usuario(nombre, **datos_extra):
    # 'nombre' es un parámetro normal (obligatorio y posicional).
    # 'datos_extra' recoge TODO lo demás que llegue como clave=valor.

    print(f"--- Ficha de {nombre} ---")

    # Comprobamos si realmente llegó información adicional.
    # Un diccionario vacío {} se evalúa como False.
    if not datos_extra:
        print("No se registraron datos adicionales.")
        return

    # .items() nos da pares (clave, valor) en cada vuelta del for.
    for clave, valor in datos_extra.items():
        # .replace("_", " ") para que 'correo_electronico' se lea bonito.
        # .capitalize() pone la primera letra en mayúscula.
        etiqueta = clave.replace("_", " ").capitalize()
        print(f"{etiqueta}: {valor}")


print("=" * 60)
ficha_usuario("Antonio", edad=25, ciudad="CDMX", correo_electronico="a@mail.com")
print()
ficha_usuario("Lucía")  # Sin extras: kwargs llega como diccionario vacío {}


# =============================================================================
# EJEMPLO 2: Calculadora de pedido -> opciones configurables con .get()
# =============================================================================
# Objetivo: usar **kwargs como "opciones opcionales" y leerlas de forma segura
# con .get(clave, valor_por_defecto), que NO lanza error si la clave no existe.

def calcular_total(precio_base, **opciones):
    # .get() devuelve el valor por defecto si el usuario no envió esa opción.
    descuento = opciones.get("descuento", 0)      # en porcentaje, 0 si no viene
    impuesto  = opciones.get("impuesto", 16)      # IVA por defecto en México
    envio     = opciones.get("envio", 0)          # costo de envío
    moneda    = opciones.get("moneda", "MXN")

    # Cálculo paso a paso para que se entienda la lógica.
    total = precio_base
    total = total - (total * descuento / 100)     # aplicamos el descuento
    total = total + (total * impuesto / 100)      # sumamos el impuesto
    total = total + envio                         # sumamos el envío

    # Avisamos si llegaron opciones que la función no reconoce.
    # Así el usuario detecta errores de escritura como "descuneto=10".
    validas = {"descuento", "impuesto", "envio", "moneda"}
    desconocidas = set(opciones) - validas        # diferencia de conjuntos
    if desconocidas:
        print(f"Aviso: opciones ignoradas -> {desconocidas}")

    return f"Total: {round(total, 2)} {moneda}"


print("=" * 60)
print(calcular_total(1000))                                   # todo por defecto
print(calcular_total(1000, descuento=10, envio=99))           # con opciones
print(calcular_total(1000, impuesto=0, moneda="USD"))         # sin impuesto
print(calcular_total(1000, descuneto=10))                     # opción mal escrita


# =============================================================================
# EJEMPLO 3: *args + **kwargs juntos y DESEMPAQUETADO de un diccionario
# =============================================================================
# Objetivo: mostrar el orden correcto de los parámetros y cómo el ** también
# sirve al LLAMAR una función para convertir un dict en argumentos con nombre.

def registrar_evento(nombre_evento, *asistentes, lugar="Por definir", **detalles):
    # nombre_evento -> parámetro posicional obligatorio
    # *asistentes   -> tupla con los posicionales extra
    # lugar         -> parámetro con valor por defecto (keyword-only aquí,
    #                  porque está después de *asistentes)
    # **detalles    -> diccionario con cualquier otro clave=valor

    print(f"Evento: {nombre_evento}")
    print(f"Lugar: {lugar}")
    print(f"Asistentes ({len(asistentes)}): {', '.join(asistentes)}")

    # Verificamos si una clave concreta fue enviada usando 'in'.
    if "hora" in detalles:
        print(f"Hora: {detalles['hora']}")

    # Mostramos el resto de detalles (todos los que no sean 'hora').
    otros = {k: v for k, v in detalles.items() if k != "hora"}
    if otros:
        print(f"Otros detalles: {otros}")
    print("-" * 40)


print("=" * 60)

# Llamada normal: mezclamos posicionales y con nombre.
registrar_evento("Taller de Python", "Ana", "Luis", "Mario",
                 lugar="Sala 3", hora="10:00", duracion="2h", online=False)

# DESEMPAQUETADO: partimos de estructuras ya existentes.
lista_asistentes = ["Sofía", "Carlos"]
config = {"lugar": "Auditorio", "hora": "18:30", "costo": 0}

# El * desempaqueta la lista en argumentos posicionales.
# El ** desempaqueta el diccionario en argumentos clave=valor.
# Es equivalente a escribir:
#   registrar_evento("Charla IA", "Sofía", "Carlos",
#                    lugar="Auditorio", hora="18:30", costo=0)
registrar_evento("Charla IA", *lista_asistentes, **config)
