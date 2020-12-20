


def funcx(x):
    fx = (0.2 + 25*x -(200*x)**2 -(675*x)**3 -(900*x)**4 + (400*x)**5)     
    return fx




def calc_umterco(h,a,ab,b):#utiliza polinomios de 2 graus, 
                        #so vale para numeros pares no intervalo
    return (h/3)*(funcx(a) + 4*(funcx(ab)) + funcx(b))


def calc_tresoitavos(h,a,x2,x3,b):#utiliza polinomios de 3 grau
      #so vale para numeros de intervalos divisiveis por 3
    return (3*h/8)*(funcx(a) + 3*(x2) + 3*funcx(x3) + funcx(b))






a = input("Defina o começo do intervalo inicial: ")
b = input("Defina o fim do intervalo inicial: ")
print("intervalo inicial definido como [",a,";",b,"]")
n = input("defina o numero de seguimentos n: ")

passo = (b - a)/n

# subintervalos = []
# subintervalos[0] = 0
# subintervalos[1] = passo
# for i in range(2,n):
#    subintervalos[i] = subintervalos[1]*i