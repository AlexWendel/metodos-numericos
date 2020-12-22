import math
<<<<<<< HEAD
from sympy import *

x,y = symbols('x y')
init_printing(use_unicode=True)

def u(x,y):
    return (x**2) + x*y - 10

def v(x,y):
    return y + 3*x*(y**2) - 57

print("Digite o par x y correto")
a = float(input("x: "))
b = float(input("y: "))
print()
print("U0 = ", u(a,b))
print("v0 = ",v(a,b))



def du_x(x,y):
    return diff(u(x,y), x)

def du_y(x,y):
    return diff(u(x,y), y)

def dv_x(x,y):
    return diff(v(x,y), x)

def dv_y(x,y):
    return diff(v(x,y), y) 

print("du/dx = ", du_x(x,y))
print("du/dy = ", du_y(x,y))
print("dv/dx = ", dv_x(x,y))
print("dv/dy = ", dv_y(x,y))

divisor = ((du_x(x,y) * dv_y(x,y)) - (du_y(x,y) * dv_x(x,y)))
=======
import sympy
>>>>>>> 2288eacf61f421c54309c583f9d70cd5bacecdd9

# def calc_x(x, u, v, dv_y, dv_x, du_y, du_x):
#     dividendo = ((u * dv_y) - (v * du_y))
#     divisor = ((du_x * dv_y) - (du_y * dv_x))
#     return x - (dividendo/divisor)

# def calc_y(y, u, v, dv_y, dv_x, du_y, du_x):
#     dividendo = ((v * du_x) - (u * dv_x))
#     divisor = ((du_x * dv_y) - (du_y * dv_x))
#     return y - (dividendo/divisor)

# def u(x,y):
#     return (x**2) + x*y - 10

# def v(x,y):
#     return y + 3*x*(y**2) - 57

# x = float(input("x: "))
# y = float(input("y: "))