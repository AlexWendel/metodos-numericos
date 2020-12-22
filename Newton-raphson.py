import math
from sympy import *

x,y = symbols('x y')
init_printing(use_unicode=True)

#definindo função u e v
# eq1 = input("digite u(x,y):")
# def u(x,y):
    
#     return eq1

# eq2 = input("digite v(x,y):")
# def v(x,y):
    
#     return eq2
def u(x,y):    
    return (x**2) + x*y - 10

def v(x,y):
    return y + 3*x*(y**2) - 57
  
print("par de raízes esperada ")
c = 2
d = 3
print(" x : ", c)
print(" y : ", d)  
print()

print("Aproximação inicial")
a = 1.5
b = 3.5
print(" x : ", a)
print(" y : ", b)
# a = float(input("x: "))
# b = float(input("y: "))
print()

print("U0 = ", u(a,b))
print("v0 = ",v(a,b))



du_x =  diff(u(x,y), x)
du_y = diff(u(x,y), y)
dv_x = diff(v(x,y), x)
dv_y =  diff(v(x,y), y) 

print("du/dx = ", du_x.evalf(subs={x:a, y:b}))
print("du/dy = ", du_y.evalf(subs={x:a, y:b}))
print("dv/dx = ", dv_x.evalf(subs={x:a, y:b}))
print("dv/dy = ", dv_y.evalf(subs={x:a, y:b}))

divisor = ((du_x.evalf(subs={x:a, y:b}) * dv_y.evalf(subs={x:a, y:b})) - du_y.evalf(subs={x:a, y:b}) * dv_x.evalf(subs={x:a, y:b}))

def calc_x(x, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((u * dv_y) - (v * du_y))
    return x - (dividendo/divisor)

def calc_y(y, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((v * du_x) - (u * dv_x))
    return y - (dividendo/divisor)

print("começando interações")
print("i = 0\n")

resultx = calc_x(a,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}), du_x.evalf(subs={x:a, y:b}))
print("x1 = ", resultx)

resulty = calc_y(b,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}),du_x.evalf(subs={x:a, y:b}))
print(" y1 = ",resulty)

errox = abs(((resultx - c) / resultx)*100)
print("erro em x :", errox)
erroy = abs(((resulty - c) / resulty)*100)
print("erro em y :", erroy)