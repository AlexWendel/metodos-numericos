# Método da bisseção
import math
from utils import *

tol = 100000000 # Tolerância inicial fictícia
eq = input("Digite a equação:") # x*math.log10(x)-1
a = float(input("Digite o ponto A:")) # Ponto A do intervalo
b = float(input("Digite o ponto B:")) # Ponto B do intervalo
tol_target = float(input("Digite a tolerância:"))  # Tolerância esperada
n = 0 # Quantidade iterações realizadas

def calc_func(x, p=False):
    result = eval(eq)
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
    print(f"\nIteração {n}:")

    xn = calc_medium(a, b)
    tol = calc_tol(a, b)
    fxn = calc_func(xn)
    table_row = f"N:{n} A:{a} B:{b} Xn: {xn} f(xn):{fxn} Tol:{tol}\n"

    print(table_row[:-2])
    print(f"Xn = {xn}")
    print(f"f(x)={eq.replace('x', str(xn))} = {fxn}")  # Equação

    tabela += table_row    
    tabela += "------------------------------------------------------------\n"

    if tol <= tol_target:
        print("TOLERÂNCIA ATINGIDA!")
        break
    
    a, b = calc_new_range(a, b, xn)
    n += 1

print("\n"+tabela)