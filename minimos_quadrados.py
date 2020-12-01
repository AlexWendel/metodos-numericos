from utils import get_partial_eq

# HARDCODED EQUATION
line_equation = "a + bx"

# Para uma linha
a1 = "((n * sumxy) - (sum_x * sum_y)) / ((n * sum_sqrtx) - pow(sum_x, 2))"
a0 = "((sum_sqrtx * sum_y) - (sumxy * sum_x)) / ((n * sum_sqrtx) - pow(sum_x, 2))"

# TODO: IMPLEMENTAR TUDO
# Aqui temos um fodendo problema, este método varia de acordo com a equação necessária, sendo uma reta a mais simples.
table_matrix = {
    1: 0.5,
    2: 2.5,
    3: 2.0,
    4: 4.0,
    5: 3.5,
    6: 6.0,
    7: 5.5
}

# Variaveis necessárias
n = len(table_matrix) # Quantidade de itens
sum_x = sum(table_matrix.keys()) # Soma de X da tabela
sum_y = sum(table_matrix.values()) # Soma de Y da tabela
sumxy = sum([x*y for x,y in table_matrix.items()]) # Soma da multiplicacao dos x por y
sum_sqrtx = sum([pow(x,2) for x in table_matrix.keys()]) # Soma dos x's ao quadrado
rounding = 6 # Casas decimais depois da vírgula

values = {
    'n': n,
    'sum_x': sum_x,
    'sum_y': sum_y,
    'sumxy': sumxy,
    'sum_sqrtx': sum_sqrtx
}

def calc_line():
    a0_equation = get_partial_eq(a0, values)
    a1_equation = get_partial_eq(a1, values)

    print(f"a0: {a0_equation}")
    print(f"a1: {a1_equation}")

    a1_result = round(eval(a0_equation), rounding)
    a0_result = round(eval(a1_equation), rounding)

    # Reconstruir a equacao da reta
    line_result = get_partial_eq(line_equation, {'a': a0_result, 'b': a1_result})
    print(f"f(x): {line_result}")

print(calc_line)