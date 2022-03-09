import numpy as np

# 1.
a = np.arange(21)
print(a[3:15:3])

# 2.
b = np.array([[1,5,4,3,2],
              [2,1,5,4,3],
              [3,2,1,5,4],
              [4,3,2,1,5],
              [5,4,3,2,1]])
print(b[0,1])
print(b[1,2])
print(b[2,3])
print(b[3,4])
print(b[4,0])

# 3.
x = np.random.random((5,5,5))

print(x)
print("\n",x[[3,2,4],[4,0,3],[3,1,2]])