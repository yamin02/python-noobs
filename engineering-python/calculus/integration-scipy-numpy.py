import numpy as np
from sympy import *
from scipy import * 
from scipy.integrate import tplquad


def f(x,y,z):
	return (5*x - 3*y)

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

ans = integrate(f(x,y,z),(x,0,1),(y,0,1-x),(z,0,1-x-y))
print(ans)
# (-5*x/2 - 3*(1 - x)**2/2 + 5/2)*(-x - y + 1)
val, err = tplquad(f,0,1,lambda x:0,lambda x:1-x, lambda x,y:0,lambda x,y:1-x-y)

print(val)
# 0.08333333333333334