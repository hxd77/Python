import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
def f(z):
    return np.vdot(z,z)

print(f(a))