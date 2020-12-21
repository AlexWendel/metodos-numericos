import math
import sympy

def calc_x(x, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((u * dv_y) - (v * du_y))
    divisor = ((du_x * dv_y) - (du_y * dv_x))
    return x - (dividendo/divisor)

def calc_y(y, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((v * du_x) - (u * dv_x))
    divisor = ((du_x * dv_y) - (du_y * dv_x))
    return y - (dividendo/divisor)

def u(x,y):
    return (x**2) + x*y - 10

def v(x,y):
    return y + 3*x*(y**2) - 57

x = float(input("x: "))
y = float(input("y: "))