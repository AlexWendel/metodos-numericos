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
    # 1/3
    print("Realizando operação por Simpson 1/3")
    result = 0
    m = 3
    for i in range(int(len(subint)/2)):
        a, ab, b = subint[i*2:i+m]
        result += calc_umterco(h, a, ab, b)
        m += 3
    print(result)

if (n % 3 == 0):
    # 3/8
    print("Realizando operação por Simpson 1/3")
    result = 0
    m = 4
    for i in range(int(len(subint)/3)):
        a, x2, x3, b = subint[i*3:i+m]
        print(a)
        result += calc_tresoitavos(h, a , x2, x3, b)
        m += 4
    print(result)

# print(calc_func(0))
# #preenchendo o vetor com os subintervalos
# for i in range(len(subint)):
#     subint[i] = h*i    

# resto1 = (n) % 2
# resto2 = (n) % 3
# result = 0

# print(" intervalos utilizados ")
# for i in range(0,n):
    
#     print("  ",subint[i],"->",subint[i+1])

# print()

# #verificando se o numero de subintervalos é par
# if resto1 == 0 :
#     print("o numero de subintervalos é par, será resolvida com simpson 1/3")
    
#     if n == 2:
#         result = calc_umterco(h ,subint[0],subint[1],subint[2])
#         print("O intervalo total é: ",result)
#         print()
#     elif n == 4:
#         result = calc_umterco(h ,subint[0],subint[1],subint[2]) + calc_umterco(h ,subint[2],subint[3],subint[4])
#         print("O intervalo total é: ",result)
#         print()
#     elif n == 6:
#         result = calc_umterco(h ,subint[0],subint[1],subint[2]) + calc_umterco(h ,subint[2],subint[3],subint[4]) + calc_umterco(h ,subint[4],subint[5],subint[6]) 
#         print("O intervalo total é: ",result)
#         print()

# #verificando se o numero de subintervalos é divisivel por 3
# elif resto2 == 0:
#     print("o numero de subintervalos é divisivel por 3, será resolvida com simpson 3/8")
    
#     if n == 3:
#         result = calc_tresoitavos(h, subint[0], subint[1],subint[2],subint[3])
#         print("o intervalo final é: ", result)
#         print()
#     elif n == 9:
#         result = calc_tresoitavos(h, subint[0], subint[1],subint[2],subint[3]) + calc_tresoitavos(h, subint[3], subint[4],subint[5],subint[6]) + calc_tresoitavos(h, subint[6], subint[7],subint[8],subint[9])
#         print("o intervalo final é: ", result)
#         print()    

# else :
#     print("o numero de subintervalos não é par e nem divisivel por 3,será resolvida com simpson composta")
#     simpUmTres = calc_umterco(h ,h * 0,h * 1,h * 2)
#     print()
#     print("simpson 1/3 : ",simpUmTres)
#     print()
#     simpTresOito =  calc_tresoitavos(h, subint[2], subint[3],subint[4],subint[5])
#     print("simpson 3/8: ", simpTresOito)
#     print()
#     result =  simpUmTres + simpTresOito
#     print("O intervalo total é: ",result)
#     print()

