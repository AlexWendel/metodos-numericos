def calc_func(x):
    return (0.2 + 25*x -(200*x)**2 -(675*x)**3 -(900*x)**4 + (400*x)**5)

# Utiliza polinômios de 2 graus
# Só vale para números pares no intervalo
def calc_umterco(h, a, ab, b):
    a = funcx(a)
    ab = funcx(ab)
    b = funcx(b)
    return (h/3) * (a + 4 * ab + b)

# Utiliza polinomios de 3 grau
# Só vale para números de intervalos divisíveis por 3
def calc_tresoitavos(h, a, x2, x3, b):      
    a = funcx(a)
    b = funcx(b)
    return (3*h/8) * (a + 3*func(x2) + 3*funcx(x3) + b)

dados = []
a, b = 0, 0.8
n = 5
h=(b-a)/n
