import math
from utils import *
from sympy import *

x,y = symbols('x y')
init_printing(use_unicode=True)

#definindo função u e v
eqU = input("digite u(x,y):")

eqV = input("digite v(x,y):")

#função pra calcular 
def u(x,y):    
    # (x**2) + x*y - 10
    return eval(eqU)

def v(x,y):
    # y + 3*x*(y**2) - 57
    return eval(eqV)
  

#recebendo valores utilizados no método
print("Digite par correto de raízes ")
c = float(input("x : "))
d = float(input("y : "))  
print(" x : ", c)
print(" y : ", d)  
print()

print("Digite a aproximação inicial")
a = float(input("x : "))
b = float(input("y : ")) 
print(" x : ", a)
print(" y : ", b)
print()

print("U0 = ", u(a,b))
print("v0 = ",v(a,b))


#diff = derivação das equações antes da ,(virgula) a função e depois da ',' a variavel relacionada a derivação
du_x =  diff(u(x,y), x)
du_y = diff(u(x,y), y)
dv_x = diff(v(x,y), x)
dv_y =  diff(v(x,y), y) 

#  .evalf(subs={x:a, y:b})) aplica os valores 'a' em x e 'b' em y na função chamada
print("du/dx = ", du_x.evalf(subs={x:a, y:b}))
print("du/dy = ", du_y.evalf(subs={x:a, y:b}))
print("dv/dx = ", dv_x.evalf(subs={x:a, y:b}))
print("dv/dy = ", dv_y.evalf(subs={x:a, y:b}))

# o divisor é igual p 'x' e 'y'
divisor = ((du_x.evalf(subs={x:a, y:b}) * dv_y.evalf(subs={x:a, y:b})) - du_y.evalf(subs={x:a, y:b}) * dv_x.evalf(subs={x:a, y:b}))

# calculando x
def calc_x(x, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((u * dv_y) - (v * du_y))
    return x - (dividendo/divisor)

# calculando y
def calc_y(y, u, v, dv_y, dv_x, du_y, du_x):
    dividendo = ((v * du_x) - (u * dv_x))
    return y - (dividendo/divisor)

#começando iterações com i = 0
print("\ncomeçando iterações para i = 0\n")

resultx = calc_x(a,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}), du_x.evalf(subs={x:a, y:b}))
print("x1 encontrado = ", resultx)

resulty = calc_y(b,u(a,b),v(a,b),dv_y.evalf(subs={x:a, y:b}),dv_x.evalf(subs={x:a, y:b}),du_y.evalf(subs={x:a, y:b}),du_x.evalf(subs={x:a, y:b}))
print("y1 encontrado = ",resulty)

#calculo do erro
def erro(real,aprox):
    return abs(((real - aprox) / real)*100)

errox = erro(c,resultx)
print("\nerro em x :", errox)
erroy = erro(d,resulty)
print("erro em y :", erroy)

#iterações seguinte de i = 1 até que o erro em relação ao par correto for menor ou igual a 0.5%
i = 1
while ( erroy > 0.5 or errox > 0.5):

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

    errox = erro(c,resultx)
    print("erro em x :", errox)
    erroy = erro(d,resulty)
    print("erro em y :", erroy)
    i = i+1
print("\no par correto foi alcançado como x = ", resultx, " e y = ", resulty)