import numpy as np
from scipy.integrate import nquad
from rosenbrock import * 

a, b = 1., 100.
x0, x1 = -2., 2.
y0, y1 = 1.4, 1.6
fxy = 1/(x1-x0)*1/(y1-y0)

def g(x, y, a=a, b=b):
	return (a - x)**2. + b*(y - x**2.)**2.

def fZ(z,a=a,b=b):
    return _f(x1,a,b)(z) - _f(x0,a,b)(z) 

def _f(x,a=a,b=b):
    return lambda z: fxy*np.sqrt(b)/(b*1j) * np.log(x -a +np.sqrt((x-a)**2)+a**2-z-a)

print(
    nquad(lambda z: z*fZ(z),[[-2., 2.]])
    )
