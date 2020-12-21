import math
from utils import *

error = None # Erro inicial fictício
eq = input("Digite a equaçao: ")#input("Digite a equação:") # math.sin(x) - pow(x, 2)
x0 = float(eval(input("Digite o X0:"))) # 2.3
x1 = float(eval(input("Digite o X1:"))) # 2.7
error_target = float(input("Digite o erro:")) # 10³
n = 0 # Número de iterações realizadas

def calc_next(xi, fxi, x0, fx0):
  return xi - ((fxi * (x0 - xi)) / (fx0 - fxi))

def calc_func(x):
  return eval(eq)

def calc_err(xi, x0):
  return abs((x0-xi)/xi)

tabela = "---------------------------- Tabela -----------------------------\n"
while not error or (error > error_target):

  fx0 = calc_func(x0)  
  fx1 = calc_func(x1)
  next_x = calc_next(x1, fx1, x0, fx0)

  table_row = f"| N: {n} | X{n}: {x0} | f(x{n}): {fx0} | ε: {(error if error else 'N/A')}\n"
  # print(f"\nx0: {x0}  x1: {x1}")
  # print(table_row)
  tabela += table_row
  tabela += "------------------------------------------------------------------\n"  

  n += 1

  if n != 0:
    # print(f"Erro: ({x1}-{x0})/{x0}") 
    error = calc_err(x0, x1)

  x0 = x1
  x1 = next_x

print('\n', tabela)