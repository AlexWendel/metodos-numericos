
# Dados
A = input("Digite a matriz: Ex:[[1,2,3],[4,5,6]]\n")
A = eval(A)
VetSol = input("Digite o vetor solução inicial: Ex:[1,2,3]\n")
VetSol = eval(VetSol)
ErroMin = input("Digite o erro minímo: Ex: pow(10,-1) ou 0.00001\n")
ErroMin = eval(ErroMin)
linhas = len(A)
colunas = len(A[0])
rounding = 6
erro = 100000000
iteracoes = 0

def printmatrix(matrix):
    for i, item in enumerate(matrix):
        print(f"A[{i}]=", item)


def applySolutions(lastSol):
    newSolutions = lastSol.copy()
    for i in range(0,linhas):
        x = A[i][colunas-1]
        for j in range(0,colunas-1):
            if i != j:
                x -= A[i][j]*newSolutions[j]
        x /= A[i][i]
        newSolutions[i] = round(x,rounding)
    return newSolutions

def getError(newSolutions):
    try:
        return abs((newSolutions[0] - VetSol[0])/VetSol[0])
    except ZeroDivisionError:
        return 1000000000

printmatrix(A)
while(erro >= ErroMin):
    print('\nInteração: '+str(iteracoes))
    newSolutions = applySolutions(VetSol)
    print("Soluções: "+str(newSolutions))
    erro = getError(newSolutions)
    print("Erro: "+ str(erro))
    VetSol = newSolutions.copy()
    iteracoes+=1
