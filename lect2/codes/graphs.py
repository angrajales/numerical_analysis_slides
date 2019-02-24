import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":
    x = np.linspace(-2, 2, num=100)
    y = x ** 2
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()