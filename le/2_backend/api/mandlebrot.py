import numpy as np
import matplotlib.pyplot as plt


def sample(c, max_iters=100):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iters:
        z = z**2 + c
        n += 1
    if n == max_iters:
        return 0
    else:
        return n


def sample_area(xmin, xmax, ymin, ymax, width=1000, height=1000, max_iters=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.empty((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = sample(x[j] + y[i] * 1j, max_iters)
    return mandelbrot_set


def plot(xmin, xmax, ymin, ymax, width=1000, height=1000, max_iters=100):
    mandelbrot_set = sample_area(xmin, xmax, ymin, ymax, width, height, max_iters)
    plt.imshow(mandelbrot_set.T, cmap="magma", extent=(xmin, xmax, ymin, ymax))
    plt.axis("off")
    plt.show()
