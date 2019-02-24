def square(n):
    return n * n
def add(linklist):
    sum = 0
    for s in linklist:
        sum += square(s)
    return sum
if __name__ == "__main__":
    print(add([1, 2, 3, 4]))