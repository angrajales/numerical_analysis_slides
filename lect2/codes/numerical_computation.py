import numpy as np
if __name__ == "__main__":
    a = [2, 3, 5.6, 1, 7.8, 9, 100]
    np_a = np.array(a)
    print((np.sum(np_a), np.max(np_a), np.min(np_a)))
    print(np_a ** 2)
    print(np.dot(np_a, np_a ** (1/2)))
    print(np_a[1:5])