
import numpy as np
import matplotlib.pyplot as plt

def one():

    x_rhombus_outer = [0, 4, 0, -4, 0]
    y_rhombus_outer = [4, 0, -4, 0, 4]

    x_square_outer = [-2, 2, 2, -2, -2]
    y_square_outer = [2, 2, -2, -2, 2]

    x_rhombus_inner = [0, 2, 0, -2, 0]
    y_rhombus_inner = [2, 0, -2, 0, 2]

    x_square_inner = [-1, 1, 1, -1, -1]
    y_square_inner = [1, 1, -1, -1, 1]

    fig, ax = plt.subplots()

    ax.plot(x_rhombus_outer, y_rhombus_outer)
    ax.plot(x_square_outer, y_square_outer)
    ax.plot(x_rhombus_inner, y_rhombus_inner)
    ax.plot(x_square_inner, y_square_inner)
    plt.show()

def two():
    x = np.arange(-10, 10, 0.5)

    y1 = 5 * x + 1
    y2 = 3 * x**2 + 2
    y3 = -3 * x**2 + 4
    y4 = -2 * x**3 + 1

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot(x, y4)
    plt.show()


def three():
    x = np.linspace(0, 4 * 3.1415, 100)
    sin_x = np.sin(x)
    cos_x = np.cos(x)

    plt.plot(x, sin_x)
    plt.plot(x, cos_x)
    plt.show()

one()
two()
three()