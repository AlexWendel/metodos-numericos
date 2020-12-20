#Dados da matriz
A = input("Digite a matriz: Ex:[[1,2,3],[4,5,6]]\n")
A = eval(A) #Traduz a string com a matriz para uma matriz regular em python
linhas = len(A) #Captura a quantidade de linhas da matriz
colunas = len(A[0]) #Captura a quantidade de colunas da matriz usando a primeira linha
rounding = 6 #Quantiade de casas decimais usadas para o arredondamento

def printmatrix(matrix): #Printa a matriz
    for i, item in enumerate(matrix):
        print(f"A[{i}]=", item)


def getMultiplierCoeficient(column, endline, matrix): #Método para obter os multiplicadores a partir do pivo
    pivot = matrix[column][column]
    multipliers = []
    for i in range(0, endline):
        if i < column:
            multipliers.append(0) #Gera um multiplicador 0 para as colunas que ja foram zeradas
        else:
            try:
                multipliers.append(A[i][column]/pivot)
            except ZeroDivisionError:
                multipliers.append(0)
    return multipliers


def applyElimination(startline, endline, endcolumn, matrix, multipliers): #Método para aplicar os multiplicadores obtidos na matriz
    for i in range(startline+1, endline):
        for j in range(startline, endcolumn):
            A[i][j] = round((multipliers[i]*A[startline][j] - A[i][j]), rounding)
    return A

print("Matriz inicial:")
printmatrix(A)
for i in range(0, linhas):
    multiplier = getMultiplierCoeficient(i, linhas, A)
    print(f"Multipliers Pivot {i}: {multiplier}")
    A = applyElimination(i, linhas, colunas, A, multiplier)
print("Matriz final:")

for j in range(0,linhas): #Reordenação da matriz se necessário
    for k in range(0,colunas):
        if j > k:
            if A[j][k] != 0:
                temp = A[j]
                A[j]=A[j-1]
                A[j-1]=temp

printmatrix(A)

solution = []
for i in range(0, linhas-1):
    solution.append(0)
solution.append(round(A[linhas-1][colunas-1]/A[linhas-1]
                      [colunas-2], rounding))  #Último coeficiente dependente desconhecido sempre é a sua divisão com o termo independente da linha

for i in range(linhas-2, -1, -1):  #Loop para obter os coeficientes depententes da penultima linha para a primeira
    sum = 0
    for j in range(colunas-2, -1, -1):
        if A[i][j] != 0 and A[i][j-1] != 0:
            sum = A[i][j] * solution[j] + sum

    solution[i] = round((-sum + A[i][colunas-1])/A[i][i],rounding) #Divide a soma dos termos dependentes conhecidos e o termo independente pelo termo depentende desconhecido

print(f"Vetor solução {solution}T")