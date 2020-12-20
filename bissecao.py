import math

a, b = (2, 3)  # Range
tol_target = 0.002  # Tolerância

n = 0
tol = 100000000

def calc_func(x, p=False):
    if p:
        print(x * math.log10(x)-1)  # Equação
    return x * math.log10(x)-1  # Equação


def calc_medium(a, b):
    print("Ponto médio (Xns):")
    print(f"Xns= ({a}+{b})/2")
    print(f"Xns= {(a+b)/2}\n")
    return (a + b) / 2


def calc_tol(a, b):
    print("Tolerância:")
    print(f"Tol= ({b}-{a})/2")
    print(f"Tol= {(b-a)/2}\n")
    return abs((b - a) / 2)


def calc_new_range(a, b, xn):
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