import numpy as np

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra la raíz de la ecuación f(x) = 0 usando el método de bisección.

    Parámetros:
    f: función f(x) cuya raíz se busca.
    a, b: intervalo inicial [a, b] con f(a) * f(b) < 0.
    tol: tolerancia para el criterio de convergencia.
    max_iter: número máximo de iteraciones.

    Retorna:
    c: valor aproximado de la raíz.
    iteraciones: número de iteraciones realizadas.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección requiere que f(a) y f(b) tengan signos opuestos.")

    iteraciones = 0
    while (b - a) / 2 > tol and iteraciones < max_iter:
        c = (a + b) / 2  # Punto medio
        if f(c) == 0:
            return c, iteraciones  # Encontramos la raíz exacta

        if f(a) * f(c) < 0:  
            b = c  # La raíz está en [a, c]
        else:
            a = c  # La raíz está en [c, b]

        iteraciones += 1

    return (a + b) / 2, iteraciones  # Devolvemos la mejor aproximación

# Definimos la función
f = lambda x: x**3 - x - 1  # Ejemplo: x³ - x - 1 = 0

# Definimos el intervalo [a, b]
a, b = 1, 2

# Ejecutamos el método
raiz, iteraciones = biseccion(f, a, b)

print(f"Raíz encontrada: {raiz:.6f} en {iteraciones} iteraciones")
