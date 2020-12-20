
a = 0
b = 0,8
n = 5
passo = (b - a)/n


def funcx(x):
    fx = (0.2 + 25*x -(200*x)**2 -(675*x)**3 -(900*x)**4 + (400*x)**5)     
    return fx


# subintervalos = []

# for i in range(0,n):
#    subintervalos = [passo*2]

def calc_umterco(h,a,ab,b):#utiliza polinomios de 2 graus, 
                        #so vale para numeros pares no intervalo
    return (h/3)*(funcx(a) + 4*(funcx(ab)) + funcx(b))


def calc_tresoitavos(h,a,x2,x3,b):#utiliza polinomios de 3 grau
      #so vale para numeros de intervalos divisiveis por 3
    return (3*h/8)*(funcx(a) + 3*(x2) + 3*funcx(x3) + funcx(b))