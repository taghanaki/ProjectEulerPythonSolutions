import numpy as np
n = 20
a = np.zeros((n, n))

for i in range(n):
    a[i, 0] = i+2
    a[0, i] = i+2

for i in range(1, n):
    for j in range(1, n):
        a[i, j] = a[i, j-1]+a[i-1, j]

print(int(a[n-1, n-1]))
