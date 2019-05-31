import numpy as np
import time
import math
import matplotlib.pyplot as plt
import scipy.linalg as sla

def phi(x, y, i, z):
    p = 1
    for j in range(len(x)):
        if (i != j):
            p = p * ((z - x[j]) / (x[i] - x[j]))
    return p

def func(x, y, z):
    s = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if (j != i):
                p *= (z - x[j]) / (x[i] - x[j])
        s += y[i] * p
    return s

def open_from_file(name):
    with open(name) as f:
        x = []
        for line in f:
            x.append(float(line.strip('\n')))
        return x

x = open_from_file('train.dat')
y = open_from_file('train.ans')
z = open_from_file('test.dat')
with open('test_l.ans', 'w') as f:
    for i in range(len(z)):
        f.write(str(func(x, y, z[i])) + '\n')
