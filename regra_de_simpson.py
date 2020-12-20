
def func(x):
    return (0.2 + 25*x -(200*x)**2 -(675*x)**3 -(900*x)**4 + (400*x)**5)

# Utiliza polinômios de 2 graus
# Só vale para números pares no intervalo
def calc_umterco(h, a, ab, b):
    a = func(a)
    ab = func(ab)
    b = func(b)
    return (h/3) * (a + 4 * ab + b)

# Utiliza polinomios de 3 grau
# Só vale para números de intervalos divisíveis por 3
def calc_tresoitavos(h, a, x2, x3, b):      
    a = func(a)
    b = func(b)
    return (3*h/8) * (a + 3*func(x2) + 3*func(x3) + b)

#dados = []


a = float(input("Defina o começo do intervalo inicial: "))
b = float(input("Defina o fim do intervalo inicial: "))
print("intervalo inicial definido como [",a,";",b,"]")
n = float(input("defina o numero de seguimentos n: "))

h = (b - a)/n

subint = [0]*5
print(subint)

for i in range(1,len(subint)):
    subint[i] = h*i    


print(subint)

# subintervalos = {
#     0 : h,
#     h : h*2,
#     h*2 : h*3,
#     h*3 : h*4,
#     h*4 : h*5
# }




