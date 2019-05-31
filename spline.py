import numpy as np
import time
import math
import matplotlib.pyplot as plt
import scipy.linalg as sla

def sweep(n, a, b, c, f):
    alpha = np.zeros(n + 1)
    beta = np.zeros(n + 1)
    x = np.zeros(n)
    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i]/d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x

def generateSpline(x, y, z, pos):
    n = len(x) - 1
    h = (x[n] - x[0]) / n
    A = np.array([0] + [1] * (n - 1) + [0])
    B = np.array([1] + [4] * (n - 1) + [1])
    C = np.array([0] + [1] * (n - 1) + [0])
    D = np.zeros(n + 1)
    f = np.zeros(n + 1)
    for i in range(1, n):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h**2
    s = sweep(n + 1, A, B, C, f)

    for i in range(0, n):
        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        D[i] = y[i]

    return A[pos] * ((z - x[i]) ** 3) + B[pos] * ((z - x[i]) ** 2) + C[pos] * (z - x[i]) + D[pos]

def func(x, y, z):
    i = 0
    while(z >= x[i]):
        i += 1;
    return generateSpline(x, y, z, i - 1)

def open_from_file(name):
    with open(name) as f:
        x = []
        for line in f:
            x.append(float(line.strip('\n')))
        return x

x = open_from_file('train.dat')
y = open_from_file('train.ans')
z = open_from_file('test.dat')
with open('test_s.ans', 'w') as f:
    for i in range(len(z)):
        f.write(str(func(x, y, z[i])) + '\n')
