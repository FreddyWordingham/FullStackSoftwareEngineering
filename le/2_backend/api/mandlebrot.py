import numpy as np

from . import colour


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


def sample_area(x_min, x_max, y_min, y_max, width=1000, height=1000, max_iters=100):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_set = np.empty((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = sample(x[j] + y[i] * 1j, max_iters)
    return mandelbrot_set


def plot(
    x_min,
    x_max,
    y_min,
    y_max,
    start_hex,
    end_hex,
    width=1000,
    height=1000,
    max_iters=100,
):
    mandelbrot_set = sample_area(x_min, x_max, y_min, y_max, width, height, max_iters)
    return np.vectorize(
        lambda x: colour.interpolate_linear(start_hex, end_hex, x / max_iters)
    )(mandelbrot_set)
