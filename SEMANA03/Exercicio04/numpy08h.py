import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])


dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]
print(dot)

dot = np.dot(a, b)
print(dot)

c = a * b
print(c)
d = np.sum(c)
print(d)

dot = a.dot(b)
print(dot)
dot = (a*b).sum()
print(dot)

dot = a @ b
print(dot)
