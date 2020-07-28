from sympy import *

x = symbols('x')
y = Function('y')(x)

d2 = diff(y,x,2)   #second derivative of y 
d1 = diff(y,x)      # first derivative of y
soln = dsolve(d2 + 2*d1 + y - sin(x))
print(soln.rhs)
