import math

def calc_relative_error(real, result):
    return abs(((real - result) / real) * 100)

def func(x):
    return pow(x, 3) + (4 * x) - 15

def regresive(x1, x2, h):
    fx1 = func(x1)
    fx2 = func(x2)
    #  f(xi) - f(xi-1)
    return (fx1 - fx2) / h

def progressive(x1, x2, h):
    fx1 = func(x1)
    fx2 = func(x2)
    #  f(xi+1) - f(xi)
    return (fx2 - fx1) / h

def central(x2, x0, h):
    fx0 = func(x0)
    fx2 = func(x2)
    #  f(xi+1) - f(xi-1)
    print(f"({fx2} - {fx0}) / (2 * {h})")
    return (fx2 - fx0) / (2 * h)

def gen_locations(x, step):
    return [x - step, x, x + step] # TODO: Dar um jeito nisso aqui

rr = 4 # Resultado real
casas = 2
x = 0
step = .25
points = gen_locations(x, step)
y = [func(point) for point in points]

print("X        f(x)")
print("============")
for x in range(len(points)):
    print(f"{points[x]}        {y[x]}")    

print("============")
print("Progressiva:")
result = progressive(points[1], points[2], step)
print(f"{result}")
print(f"Erro: {round(calc_relative_error(rr, result), casas)}%")
print("============") 

print("Regressiva:")
result = regresive(points[1], points[0], step)
print(f"{result}")
print(f"Erro: {round(calc_relative_error(rr, result), casas)}%")
print("============") 

print("Central:")
result = central(points[2], points[0], step)
print(f"{result}")
print(f"Erro: {round(calc_relative_error(rr, result),casas)}%")
print("============") 