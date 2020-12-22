import math
import numpy as np
from numpy import linalg

points = int(input("Quantidade de pontos: "))
degree = int(input("Digite o grau do polinômio: "))

x, y = np.zeros(points), np.zeros(points)
for i in range(points):
    x[i] = float(input("x" + str(i) +" = "))
    y[i] = float(input("y" + str(i) +" = "))

values = np.zeros((degree+1, points))
for i in range(len(values)):
    for j in range(points):
        values[i][j] = math.pow(x[j], i)

print(f"------------------------- Matriz -------------------------")
for i in values:
    print(i)
print("-----------------------------------------------------------\n")

A = np.zeros((degree+1, degree+1))
B = np.zeros(degree+1)
for i in range(len(A)):
    for j in range(len(A)):
        A[i][j] = values[i].dot(values[j])
        B[i] = values[i].dot(y)

for i, row in enumerate(A):
    print(f"{row} = {B[i]}")

result = np.linalg.solve(A, B)
result = [result[i] for i in range(len(result))]
print(f"Resultado X: {result}")    