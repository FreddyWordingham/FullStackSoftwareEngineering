import numpy as np


def sample(c, max_iters):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iters:
        z = z**2 + c
        n += 1
    if n == max_iters:
        return 0
    else:
        return n


def sample_area(real_start, real_end, imag_start, image_end, max_iters, width, height):
    x = np.linspace(real_start, real_end, width)
    y = np.linspace(imag_start, image_end, height)
    mandelbrot_set = np.empty((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = sample(x[j] + y[i] * 1j, max_iters)
    return mandelbrot_set
