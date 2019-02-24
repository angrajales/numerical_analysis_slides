import numpy as np # Computación Numérica
import sympy as sp # Computación Simbólica
import math        # Operaciones matemáticas.
import matplotlib  # Graficos
import sys         # Sistema
if __name__ == "__main__":
    x = sp.symbols('x')
    fx = x ** 2 + sp.sin(x)
    print(fx.diff(x))
    print(np.random.normal((4, 4)))