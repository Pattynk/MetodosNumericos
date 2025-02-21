import numpy as np

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    """
    Encuentra la raíz de la ecuación x = g(x) usando el método del punto fijo.

    Parámetros:
    g: función g(x) que define la ecuación x = g(x).
    x0: valor inicial.
    tol: tolerancia.
    max_iter: número máximo de iteraciones.

    Retorna:
    xn: valor aproximado de la raíz.
    iteraciones: número de iteraciones realizadas.
    """
    xn = x0
    iteraciones = 0

    while iteraciones < max_iter:
        xnuevo = g(xn)  # Aplicamos g(x)

        if abs(xnuevo - xn) < tol:
            return xnuevo, iteraciones + 1  # Convergió

        xn = xnuevo
        iteraciones += 1

    raise ValueError("El método no convergió después de {} iteraciones".format(max_iter))

# Definimos la función g(x)
g = lambda x: (x + 1)**(1/3)

# Valor inicial
x0 = 1.5

# Ejecutamos el método
raiz, iteraciones = punto_fijo(g, x0)

print(f"Raíz encontrada con punto fijo: {raiz:.6f} en {iteraciones} iteraciones")
