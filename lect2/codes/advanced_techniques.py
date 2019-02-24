import numpy as np
if __name__ == "__main__":
    (a, b) = input().split(" ")
    result = a if a < b else b
    print(result)
    arr = np.arange(100)
    print(arr[2:len(arr):2])
    net = [i for i in range(1, 100) if i % 2 != 0]
    print(net)