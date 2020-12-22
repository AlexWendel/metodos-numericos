import math
from utils import *

eq = input("Digite a equação:")
x = float(input("Digite o ponto: "))
step = float(eval(input("Digite o passo:")))
rr = float(eval(input("[OPCIONAL] Digite o resultado real:"))) #4 # Resultado real
rounding = 2 # Arrendondamento

def calc_relative_error(real, result):
    return abs(((real - result) / real) * 100)

def func(x):
    return eval(eq)

def regresive(x1, x2, h, show=False):
    fx1 = func(x1)
    fx2 = func(x2)
    #  f(xi) - f(xi-1)
    if show:
        print(f"({fx1} - {fx2}) / {h}")
    return (fx1 - fx2) / h

def progressive(x1, x2, h, show=False):
    fx1 = func(x1)
    fx2 = func(x2)
    #  f(xi+1) - f(xi)
    if show:
        print(f"({fx2} - {fx1}) / {h}")
    return (fx2 - fx1) / h

def central(x2, x0, h, show=False):
    fx0 = func(x0)
    fx2 = func(x2)
    #  f(xi+1) - f(xi-1)
    if show:
        print(f"({fx2} - {fx0}) / (2 * {h})")    
    return (fx2 - fx0) / (2 * h)

def gen_locations(x, step):
    return [x - step, x, x + step] # TODO: Dar um jeito nisso aqui


points = gen_locations(x, step)
y = [func(point) for point in points]

print("X        f(x)")
print("============")
for x in range(len(points)):
    print(f"{points[x]}        {y[x]}")    
print("============")


print("Progressiva:")
result = progressive(points[1], points[2], step)
print(f"Resultado: {result}")
if rr:
    print(f"Erro: {round(calc_relative_error(rr, result), rounding)}%")
print("============") 

print("Regressiva:")
result = regresive(points[1], points[0], step)
print(f"Resultado: {result}")
if rr:
    print(f"Erro: {round(calc_relative_error(rr, result), rounding)}%")
print("============") 

print("Central:")
result = central(points[2], points[0], step)
print(f"Resultado: {result}")
if rr:
    print(f"Erro: {round(calc_relative_error(rr, result), rounding)}%")
print("============") 