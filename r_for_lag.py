import numpy as np
from random import *

n = 5
m = 10
with open('train.dat', 'w') as f:
    x = []
    x.append(0)
    for i in range(n - 2):
        x.append(random() * 10)
    x.append(10)
    x.sort()
    for i in range(n):
        f.write(str(x[i]) + '\n')
with open('train.ans', 'w') as f:
    for i in range(n):
        f.write(str(random() * 10) + '\n')
with open('test.dat', 'w') as f:
    x = []
    for i in range(m):
        x.append(random() * 10)
    x.sort()
    for i in range(m):
        f.write(str(x[i]) + '\n')
