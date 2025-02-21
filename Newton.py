import numpy as np

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Encuentra la raíz de la ecuación f(x) = 0 usando el método de Newton-Raphson.

    Parámetros:
    f: función f(x) cuya raíz se busca.
    df: derivada f'(x).
    x0: valor inicial.
    tol: tolerancia para el criterio de convergencia.
    max_iter: número máximo de iteraciones.

    Retorna:
    xn: valor aproximado de la raíz.
    iteraciones: número de iteraciones realizadas.
    """
    xn = x0
    for i in range(max_iter):
        fxn = f(xn)
        dfxn = df(xn)
        
        if abs(fxn) < tol:
            return xn, i+1  # Convergió
        
        if dfxn == 0:
            raise ValueError("La derivada se anuló, el método falla.")

        xn = xn - fxn / dfxn  # Fórmula de Newton-Raphson

    raise ValueError("El método no convergió después de {} iteraciones".format(max_iter))

# Definimos la función y su derivada
f = lambda x: x**3 - x - 1  # Ejemplo: x³ - x - 1 = 0
df = lambda x: 3*x**2 - 1    # Derivada: 3x² - 1

# Parámetro inicial
x0 = 1.5

# Aplicamos Newton-Raphson
raiz, iteraciones = newton_raphson(f, df, x0)

print(f"Raíz encontrada: {raiz:.6f} en {iteraciones} iteraciones")
