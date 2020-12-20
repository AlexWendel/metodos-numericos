
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

a = input("Defina o começo do intervalo inicial: ")
b = input("Defina o fim do intervalo inicial: ")
print("intervalo inicial definido como [",a,";",b,"]")
n = input("defina o numero de seguimentos n: ")

h = (b - a)/n

subintervalos = []
subintervalos[0] = 0
subintervalos[1] = h
for i in range(2,n):
   subintervalos[i] = subintervalos[1]*i

