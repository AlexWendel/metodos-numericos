
#Dados da matriz
A = input("Digite a matriz: Ex:[[1,2,3],[4,5,6]]\n")
A = eval(A)
linhas = len(A)
colunas = len(A[0])
rounding = 6

def printmatrix(matrix):
    for i, item in enumerate(matrix):
        print(f"A[{i}]=", item)


def getMultiplierCoeficient(column, endline, matrix):
    pivot = matrix[column][column]
    multipliers = []
    for i in range(0, endline):
        if i < column:
            multipliers.append(0)
        else:
            try:
                multipliers.append(round(A[i][column]/pivot, rounding))
            except ZeroDivisionError:
                multipliers.append(0)
    return multipliers


def applyElimination(startline, endline, endcolumn, matrix, multipliers):
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

for j in range(0,linhas): #Matrix rearrangement if needed 
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
                      [colunas-2], rounding))  # Last line

for i in range(linhas-2, -1, -1):  # Last to first line
    sum = 0
    for j in range(colunas-2, -1, -1):  # Last to first column of dependent terms
        if A[i][j] != 0 and A[i][j-1] != 0:
            sum = A[i][j] * solution[j] + sum

    solution[i] = round((-sum + A[i][colunas-1])/A[i][i],rounding) #Divide the sum of know dependent terms and the independent term by the unknown dependent term of the line

print(f"Vetor solução {solution}T")