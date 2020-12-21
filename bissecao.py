# Método da bisseção

import math

tol = 100000000 # Tolerância inicial fictício
a, b = (2, 3)  # Intervalo
tol_target = 0.001  # Tolerância esperada
n = 0 # Quantidade iterações realizadas

def calc_func(x, p=False):
    result = x * math.log10(x)-1
    if p:
        print(result) 
    return result

def calc_medium(a, b, show=False):
    result = (a + b) / 2
    if show:
        print("Ponto médio (Xns):")
        print(f"Xns= ({a}+{b})/2")
        print(f"Xns= {result}\n")
    return result

def calc_tol(a, b, show=False):
    result = abs((b - a) / 2)
    if show:
        print("Tolerância:")
        print(f"Tol= ({b}-{a})/2")
        print(f"Tol= {result}\n")
    return result

def calc_new_range(a, b, xn, show=False):
    if show:
        print(f"f(a): {calc_func(a)}")
        print(f"f(a) * f(Xn) = {calc_func(a) * calc_func(xn)}\n")

    if calc_func(a) * calc_func(xn) < 0:
        return (a, xn)
    else:
        return (xn, b)

tabela = "------------------------- Tabela -------------------------\n"
while True:
    print(f"Interação: {n}")
    xn = calc_medium(a, b)
    tol = calc_tol(a, b)

    print(f'f({xn})= {xn} * log({xn})-1')  # Equação

    print('fxn=', end='')
    fxn = calc_func(xn, True)
    print(f"N: {n} A:{a} B:{b} Xn: {xn} f(xn): {fxn} Tol: {tol}")
    tabela += f"N: {n} A:{a} B:{b} Xn: {xn} f(xn): {fxn} Tol: {tol}\n"
    tabela += "------------------------------------------------------------\n"

    if tol <= tol_target:
        break

    a, b = calc_new_range(a, b, xn)
    n += 1

print("\n"+tabela)