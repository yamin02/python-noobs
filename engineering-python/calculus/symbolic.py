from sympy import *
x,y,z = symbols('x,y,z')

def f(x,y):
    return (3*y**6 + 5**(y**xy) + exp(3))

print(integrate(f(x,y),(y,2,4)))
print(diff(f(x,y), y))

p = series(sin(x)+ cos(x) , x )
print(p)