if __name__ == "__main__":
    constant_number = 7
    integer = int(input("Ingrese n:\n"))
    if integer == constant_number:
        print("Los números son iguales.")
    elif integer > constant_number:
        print("El número ingresado es mayor.")
    else:
        print("El número ingresado es menor.")