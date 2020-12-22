import math
from sympy import *

x,y = symbols('x y')
init_printing(use_unicode=True)

#definindo função u e v
# eqU = input("digite u(x,y):")
# def u(x,y): 
#     return eqU

# eqV = input("digite v(x,y):")
# def v(x,y):
#     return eqV
def u(x,y):    
    return (x**2) + x*y - 10

def v(x,y):
    return y + 3*x*(y**2) - 57
  
print("par correto de raízes ")
c = 2
d = 3
print(" x : ", c)
print(" y : ", d)  
print()

print("Aproximação inicial")
a = 1.5#1.9987
b = 3.5#3.0029
# a = float(input("x: "))
# b = float(input("y: "))
print(" x : ", a)
print(" y : ", b)
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

print("\ncomeçando iterações para i = 0\n")

resultx = calc_x(a,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}), du_x.evalf(subs={x:a, y:b}))
print("x1 encontrado = ", resultx)

resulty = calc_y(b,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}),du_x.evalf(subs={x:a, y:b}))
print("y1 encontrado = ",resulty)

errox = abs(((resultx - c) / resultx)*100)
print("\nerro em x :", errox)
erroy = abs(((resulty - d) / resulty)*100)
print("erro em y :", erroy)

# if errox > 1.1 && erroy > 1.1:
#     resultx1 = resultx
#     resulty1 = resulty
#     a = resultx1
#     b = resulty1



i = 1
while ( erroy > 1.1):

    print("\nO par correto ainda não foi alcançado\n")
    print("começando iterações para i = ",i)
   

    print("\nx : ", resultx)
    print("y : ", resulty)
    resultx1 = resultx
    resulty1 = resulty
    a = resultx1
    b = resulty1
    

    resultx = calc_x(a,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}), du_x.evalf(subs={x:a, y:b}))
    print("x1 encontrado = ", resultx)

    resulty = calc_y(b,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}),du_x.evalf(subs={x:a, y:b}))
    print("y1 encontrado = ",resulty)

    errox = abs(((resultx - c) / resultx)*100)
    print("erro em x :", errox)
    erroy = abs(((resulty - d) / resulty)*100)
    print("erro em y :", erroy)
    i = i+1
print("\no par correto foi alcançado como x = ", resultx, " e y = ", resulty)