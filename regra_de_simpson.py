import math
from utils import *

eq =  input("Digite a funcão: ") # "1/(1+x**2)" # 0.2 + 25*x - 200 * (x**2) + 675 * (x**3) -900* (x**4) + 400*(x**5)
start = float(eval(input("Limite de integração a:"))) 
end = float(eval(input("Limite de integração b:"))) #(math.pi/2)
n = int(input("Número de subintervalos desejado:")) 

def calc_func(x):
    return eval(eq)

# Utiliza polinômios de 2 graus
# Só vale para um número de intervalo par
def calc_umterco(h, a, ab, b, show=True):
    a = calc_func(a)
    ab = calc_func(ab)
    b = calc_func(b)    
    if show:
        print(f"{h}/3 * ({a} + 4 * {ab} + {b})")
    return (h / 3) * (a + (4 * ab) + b)

# Utiliza polinomios de 3 grau
# Só vale para um número de intervalos divisíveis por 3
def calc_tresoitavos(h, a, x2, x3, b, show=True):
    a = calc_func(a)
    b = calc_func(b)
    if show:
        print(f"(3*{h})/8) * ({a} + 3*{calc_func(x2)} + 3*{calc_func(x3)} + {b}")
    return ((3*h)/8) * (a + 3*calc_func(x2) + 3*calc_func(x3) + b)

def calc_h(start, end, n):
    return (end - start) / n

def calc_ab(a, b):
    return (a + b) / 2    

h = calc_h(start, end, n)
subint = [start]

a = start
for i in range(n-1):
    a += h
    subint.append(a)
subint.append(end)


if (n % 2 == 0):
    print("Realizando operação por Simpson 1/3")
    # 1/3
    result = 0
    m = 3
    for i in range(int(len(subint)/2)):
        a, ab, b = subint[i*2:i+m]
        result += calc_umterco(h, a, ab, b)
        m += 3
    print(result)

elif (n % 3 == 0):
    print("Realizando operação por Simpson 3/8")
    # 3/8
    result = 0
    m = 4
    for i in range(int(len(subint)/3)):
        a, x2, x3, b = subint[i*3:i+m]
        result += calc_tresoitavos(h, a , x2, x3, b)
        m += 4
    print(result)

else:
    print("Realizando operação por Simpson 1/3 e 3/8")
    # 3/8 + 1/3
    it_2 = (n % 2)
    it_3 = (n % 3)

    # 1/3
    sub = subint[:(2*it_2)+1]
    result_0 = 0
    m = 3
    for i in range(int(len(sub)/2)):
        a, ab, b = sub[i*2:i+m]
        result_0 += calc_umterco(h, a, ab, b)
        m += 3

    # 3/8
    sub = subint[(2*it_2):(3*it_3)+1]
    result_1 = 0
    m = 4
    for i in range(int(len(sub)/3)):
        a, x2, x3, b = sub[i*3:i+m]
        result_1 += calc_tresoitavos(h, a , x2, x3, b)
        m += 4

    # print(f"{result_0} + {result_1}")
    print(f"Resultado: {result_0 + result_1}")