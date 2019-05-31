import numpy as np
import time
import math
import matplotlib.pyplot as plt
import scipy.linalg as sla

def func_i(x, y, z, i):
    return (y[i + 1] - y[i]) / (x[i + 1] - x[i]) * (z - x[i]) + y[i]

def func(x, y, z):
    i = 0
    while(z >= x[i]):
        i += 1;
    return func_i(x, y, z, i - 1)

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
