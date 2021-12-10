import numpy as np
import time
import threading

n = 1000000
a = np.random.randn(n)
b = np.random.randn(n)
c = np.empty(n, dtype='float64')

for i in range(n):
    c[i] = a[i] + b[i]
