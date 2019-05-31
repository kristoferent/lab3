import numpy as np
from random import *

n = 5
m = 10
with open('train.dat', 'w') as f:
    for i in range(0, n * 10 + 1, 10):
        f.write(str(i / n) + '\n')
with open('train.ans', 'w') as f:
    for i in range(n + 1):
        f.write(str(random() * 10) + '\n')
with open('test.dat', 'w') as f:
    x = []
    for i in range(m):
        x.append(random() * 10)
    x.sort()
    for i in range(m):
        f.write(str(x[i]) + '\n')
