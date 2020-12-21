
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
n = int(input("defina o numero inteiro de seguimentos n: "))

h = (b - a)/n #passo
print("passo utilizado: ", h)

subint = [0]*(n+1) #vetor de subintervalos


#preenchendo o vetor com os subintervalos
for i in range(len(subint)):
    subint[i] = h*i    

resto1 = (n) % 2
resto2 = (n) % 3
result = 0

print(" intervalos utilizados: ",subint)
#verificando se o numero de subintervalos é par
if resto1 == 0 :
    print("o numero de subintervalos é par, será resolvida com simpson 1/3")
    
    
    # if n == 2:
    #     result = calc_umterco(h ,subint[0],subint[1],subint[2])
    #     print("O intervalo total é: ",result)
    # elif n == 3:
    #     result = calc_umterco(h ,subint[0],subint[1],subint[2]) + calc_umterco(h ,subint[2],subint[3],subint[4])
    #     print("O intervalo total é: ",result)
    # elif n == 7:
    #     result = calc_umterco(h ,subint[0],subint[1],subint[2]) + calc_umterco(h ,subint[2],subint[3],subint[4]) + calc_umterco(h ,subint[4],subint[5],subint[6]) 
    #     print("O intervalo total é: ",result)
    
elif resto2 == 0:
    print("o numero de subintervalos é divisivel por 3, será resolvida com simpson 3/8")
  

else :
    print(" o numero de subintervalos não é par e nem divisivel por 3,será resolvida com simpson composta")
   
    result = calc_umterco(h ,subint[0],subint[1],subint[2]) + calc_tresoitavos(h, subint[2], subint[3],subint[4],subint[5])

    print("O intervalo total é: ",result)




# subintervalos = {
#     0 : h,
#     h : h*2,
#     h*2 : h*3,
#     h*3 : h*4,
#     h*4 : h*5
# }




