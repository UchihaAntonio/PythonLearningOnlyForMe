"""
================================================================================
FUNCIONES DINÁMICAS EN PYTHON
================================================================================

Las funciones dinámicas son un concepto fundamental en programación funcional
que permite crear y manipular funciones en tiempo de ejecución. Python ofrece
características que permiten trabajar con funciones como objetos de primera
clase (first-class objects), lo que habilita patrones avanzados como:

1. FUNCIONES COMO OBJETOS
   - Las funciones son objetos iterable en Python
   - Pueden ser asignadas a variables
   - Pueden ser pasadas como argumentos
   - Pueden ser retornadas desde otras funciones

2. CLOSURES (Clausuras)
   - Una función interna que captura variables del scope externo
   - Permite crear funciones especializadas manteniendo estado
   - Las variables capturadas persisten en memoria

3. DECORADORES
   - Funciones que reciben una función y retornan una función modificada
   - Permiten envolver el comportamiento de funciones sin modificarlas

4. FUNCIONES DE ORDEN SUPERIOR
   - map(), filter(), reduce()
   - Permiten aplicar transformaciones a iterables de forma funcional

5. LAMBDA
   - Funciones anónimas de una sola expresión
   - Útiles para callbacks y funciones pequeñas

================================================================================
"""

# EJEMPLO 1: CLOSURES - Crear funciones especializadas con estado capturado
# ============================================================================

print("EJEMPLO 1: CLOSURES Y FUNCIONES DINÁMICAS CON ESTADO\n")
print("-" * 70)

def crear_multiplicador(factor):
    """
    Función de orden superior que retorna una función.
    
    La función interna 'multiplicar' captura la variable 'factor' del scope
    externo, formando un closure. Esto permite crear funciones especializadas
    dinámicamente.
    
    Args:
        factor: El factor por el cual se multiplicará
    
    Returns:
        Una función que multiplica su argumento por 'factor'
    """
    def multiplicar(x):
        return x * factor
    return multiplicar


# Creamos dinámicamente dos funciones especializadas
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)
multiplicar_por_10 = crear_multiplicador(10)

print("Usando closures para crear funciones especializadas:")
print(f"duplicar(5) = {duplicar(5)}")
print(f"triplicar(5) = {triplicar(5)}")
print(f"multiplicar_por_10(5) = {multiplicar_por_10(5)}")
print()

# Inspeccionar el closure
print(f"Closure de 'duplicar': {duplicar.__closure__}")
print(f"Variables capturadas: {[cell.cell_contents for cell in duplicar.__closure__]}")
print()


# EJEMPLO 2: DECORADORES - Modificar comportamiento dinámicamente
# ============================================================================

print("EJEMPLO 2: DECORADORES - MODIFICAR FUNCIONES DINÁMICAMENTE\n")
print("-" * 70)

def decorador_cronometro(func):
    """
    Decorador que mide el tiempo de ejecución de una función.
    
    Este es un ejemplo de función dinámica que envuelve ('wraps') otra función,
    modificando su comportamiento sin alterar su definición original.
    
    Args:
        func: La función a decorar
    
    Returns:
        Una función envuelta que registra el tiempo de ejecución
    """
    import time
    from functools import wraps
    
    @wraps(func)  # Preserva metadatos de la función original
    def envolvente(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️  '{func.__name__}' tardó {(fin - inicio)*1000:.4f} ms")
        return resultado
    
    return envolvente


def decorador_validador_tipos(*tipos_esperados):
    """
    Decorador de orden superior que valida tipos de argumentos.
    
    Demuestra cómo crear decoradores parametrizados que retornan decoradores.
    
    Args:
        tipos_esperados: Tipos que se espera reciban los argumentos
    
    Returns:
        Un decorador que valida tipos
    """
    def decorador(func):
        from functools import wraps
        
        @wraps(func)
        def envolvente(*args, **kwargs):
            # Validar tipos de argumentos posicionales
            for i, (arg, tipo_esperado) in enumerate(zip(args, tipos_esperados)):
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(
                        f"Argumento {i} ({arg}) debe ser {tipo_esperado.__name__}, "
                        f"no {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        
        return envolvente
    return decorador


# Aplicar decoradores a funciones
@decorador_cronometro
@decorador_validador_tipos(int, int)
def suma_lenta(a, b):
    """Suma dos números con simulación de operación costosa."""
    import time
    time.sleep(0.1)
    return a + b


print("Aplicando decoradores dinámicamente:")
resultado = suma_lenta(5, 3)
print(f"Resultado: {resultado}\n")

# Intentar con tipo incorrecto (generará error capturado)
try:
    suma_lenta("5", 3)
except TypeError as e:
    print(f"❌ Error capturado: {e}\n")


# EJEMPLO 3: FUNCIONES DE ORDEN SUPERIOR CON MAP, FILTER Y REDUCE
# ============================================================================

print("EJEMPLO 3: FUNCIONES DE ORDEN SUPERIOR (MAP, FILTER, REDUCE)\n")
print("-" * 70)

from functools import reduce

# Datos de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 3.1 MAP - Aplicar función a cada elemento (transformación)
print("MAP - Transformación de elementos:")
print(f"Números originales: {numeros}")

# Usando lambda con map
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados: {cuadrados}")

# Definir función nombrada para mayor claridad
def es_par(x):
    """Predicate function para filtrar pares."""
    return x % 2 == 0

pares = list(filter(es_par, numeros))
print(f"\nFILTER - Filtración de elementos:")
print(f"Números pares: {pares}")

# 3.2 REDUCE - Acumulación/Agregación
print(f"\nREDUCE - Acumulación:")
suma_total = reduce(lambda acc, x: acc + x, numeros)
print(f"Suma total: {suma_total}")

producto_total = reduce(lambda acc, x: acc * x, numeros)
print(f"Producto total: {producto_total}")

# Composición: Mapear, filtrar y reducir
resultado_composicion = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x ** 2, filter(es_par, numeros))
)
print(f"\nComposición (suma de cuadrados de pares): {resultado_composicion}")
print()


# BONUS: EJEMPLO AVANZADO - DECORADOR CON MEMOIZACIÓN
# ============================================================================

print("BONUS: MEMOIZACIÓN - Optimización dinámica de funciones\n")
print("-" * 70)

def memoizacion(func):
    """
    Decorador que cachea resultados de funciones (memorización).
    
    Utiliza un closure para mantener un diccionario de resultados en caché,
    evitando recalcular valores ya computados.
    
    Args:
        func: Función cuyos resultados se cachearán
    
    Returns:
        Función envuelta con caché
    """
    cache = {}  # Variable capturada en el closure
    
    def envolvente(*args):
        # Usar args como clave del caché (solo funciona con args hashables)
        if args not in cache:
            cache[args] = func(*args)
            print(f"📝 Calculando {func.__name__}{args}...")
        else:
            print(f"💾 Usando caché para {func.__name__}{args}...")
        return cache[args]
    
    # Permitir acceso al caché desde fuera
    envolvente.cache = cache
    envolvente.__name__ = func.__name__
    
    return envolvente


@memoizacion
def fibonacci(n):
    """Serie de Fibonacci - función computacionalmente cara."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Memoización en acción:")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(5) = {fibonacci(5)}")  # Desde caché
print(f"Contenido del caché: {fibonacci.cache}")
print()

print("=" * 70)
print("FIN DE LA EXPLICACIÓN DE FUNCIONES DINÁMICAS EN PYTHON")
print("=" * 70)