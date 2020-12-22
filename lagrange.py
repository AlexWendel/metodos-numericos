#!/usr/bin/env python3
import sys
from utils import *

# EQUAÇÕES HARDCODED
fn_eq = "li * y_i"
li_eq = "(x - x_j) / (x_i - x_j)"

points = int(input("Quantidade de pontos: "))
degree = int(input("Digite o grau do polinômio: "))
x = float(input("Digite o valor do ponto: "))

table_matrix = [[0,0] for i in range(points)]
for i in range(points):
    table_matrix[i][0] = float(input("x" + str(i) +" = "))
    table_matrix[i][1] = float(input("y" + str(i) +" = "))

def calc_li(xi, xj, x="x"):
    return get_partial_eq(li_eq, {'x_j': xj, 'x_i': xi, 'x': x})

# table_matrix = [
#     [1,0],
#     [4, 1.386294],
#     [6, 1.791760]
# ] # Tabela de valores
# degree = 2 # Grau da equação
table_rows = table_matrix[:degree+1] # Hardcoded, não mexa
rows_length = len(table_rows) # Quantidade de rows a serem analisadas (NÃO MEXA)
rounding = 6 # Quantidade de casas depois da vírgula

iterations = []
for i in range(rows_length):    
    x_i = table_rows[i][0]
    y_i = table_rows[i][1]# aka f(x)

    values_to_use = [v for v in table_rows if v != table_rows[i]]
    iteration_li = []
    for value in values_to_use:
        x_j, y_j = value        
        iteration_li.append(calc_li(x_i, x_j))
    
    final_iteration_li = " * ".join(iteration_li)
    final_iteration_li += f" * {y_i}"
    iterations.append(final_iteration_li)

glued_equation = " + ".join(iterations)
partial_equation = get_partial_eq(glued_equation, {'x': x})
print(f"f({x}) = {partial_equation}")
result = eval(partial_equation)
print(f"Resultado: {round(result, rounding)}")