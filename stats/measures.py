import numpy as np


def zr(x):
    return (x[0] + x[-1]) / 2


def ztr(x):
    a = 0.05
    n = len(x)
    r = round(a * n)
    return np.sum(x[r:n - r - 1]) / (n - 2 * r)


def zq(x):
    n = len(x)
    if n // 4 == 0:
        lq = x[-1]
    else:
        lq = x[round(n / 4)]
    if (3 * n) // 4 == 0:
        uq = x[3 * n / 4]
    else:
        uq = x[round(3 * n / 4)]

    return (lq + uq) / 2
