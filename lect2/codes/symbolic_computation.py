import sympy as sp
if __name__ == "__main__":
    x = sp.symbols('x')
    poly = 3 * x**4 + 4 * x**3 + 2 * x**2 -4
    dpoly = poly.diff(x)
    print(dpoly)
    print(poly.evalf(subs={x: 7}))
    ipoly = poly.integrate(x)
    print(ipoly)
    print(ipoly.evalf(subs={x: 7}))