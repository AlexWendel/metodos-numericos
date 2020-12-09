
#Dados da matriz
A = [[1,1,1,1,1,15],[1,2,3,4,5,35],[1,3,6,10,15,70],[1,4,10,20,35,126],[1,5,15,35,70,210]]
linhas = 5
colunas = 6
rounding = 6

def printMatrice(matrice):
    for i, item in enumerate(matrice):
        print(f"A[{i}]=", item)


def getMultiplierCoeficient(column, endline, matrice):
    pivot = matrice[column][column]
    multipliers = []
    for i in range(0, endline):
        if i < column:
            multipliers.append(0)
        else:
            multipliers.append(round(A[i][column]/pivot, rounding))
    return multipliers


def applyElimination(startline, endline, endcolumn, matrice, multipliers):
    for i in range(startline+1, endline):
        for j in range(startline, endcolumn):
            A[i][j] = round((multipliers[i]*A[startline][j] - A[i][j]), rounding)
    return A


print("Matriz inicial:")
printMatrice(A)
for i in range(0, linhas):
    multiplier = getMultiplierCoeficient(i, linhas, A)
    print(f"Multipliers Pivot {i}: {multiplier}")
    A = applyElimination(i, linhas, colunas, A, multiplier)
print("Matriz final:")
printMatrice(A)

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