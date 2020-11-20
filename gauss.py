
#Dados da matriz
A = [[1,1,1,1,1,15],[1,2,3,4,5,35],[1,3,6,10,15,70],[1,4,10,20,35,126],[1,5,15,35,70,210]]
linhas = 5
colunas = 6

def printMatrice(matrice): 
    for i,item in enumerate(matrice):
        print(f"A[{i}]=",item)

def getMultiplierCoeficient(column,endline,matrice):
    pivot = matrice[column][column]
    multipliers = []
    for i in range(0,endline):
        if i < column:
            multipliers.append(0)
        else:
            multipliers.append(A[i][column]/pivot)
    return multipliers

def applyElimination(startline,endline,endcolumn,matrice,multipliers):
    for i in range(startline+1,endline):
        for j in range(startline,endcolumn):
            A[i][j] = multipliers[i]*A[startline][j] - A[i][j]
    return A
    
printMatrice(A)
for i in range(0,linhas):
    multiplier =  getMultiplierCoeficient(i,linhas,A)
    print(f"Multipliers Pivot {i}: {multiplier}")
    A = applyElimination(i,linhas,colunas,A,multiplier)
printMatrice(A)

solution = []
for i in range(0,linhas-1):
    solution.append(0)
solution.append(A[linhas-1][colunas-1])

for i in range(linhas-2,-1,-1):
    sum = 0
    for j in range(colunas-2,-1,-1):
        if A[i][j] != 0 and solution[j-1]==0:
            sum = A[i][j]* 1 + sum
        else:
            sum = A[i][j]*solution[j-1] + sum

    solution[i]= sum - A[i][colunas-1]

print(f"Solução {solution}")