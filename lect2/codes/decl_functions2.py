import math
def taylorSin(at, maxtoler, maxiter):
    result , real_value = 0.0, math.sin(at)
    for i in range(0, maxiter):
        den = math.factorial(2 * i + 1)
        num, mult = (-1) ** i, at ** (2 * i + 1)
        result += (num / den) * mult
        if abs(real_value - result) < maxtoler:
            break
    return result
if __name__ == "__main__":
    print(taylorSin(7/8, 10**-8, 100))