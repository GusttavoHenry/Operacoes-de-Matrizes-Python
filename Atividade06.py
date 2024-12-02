import numpy as np

# Definindo as matrizes A e B
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# 1. Soma das duas matrizes C = A + B
C = A + B
print("C = A + B:\n", C)

# 2. Produto elemento a elemento D = A * B
D = A * B
print("D = A * B:\n", D)

# 3. Produto matricial E = A @ B
E = A @ B
print("E = A @ B:\n", E)

# 4. Soma de todos os elementos da matriz C
soma_C = np.sum(C)
print("Soma dos elementos de C:", soma_C)

# 5. Transposta da matriz D
DT = D.T
print("Transposta de D:\n", DT)

# 6. Valor máximo e mínimo da matriz E
max_E = np.max(E)
min_E = np.min(E)
print("Valor máximo de E:", max_E)
print("Valor mínimo de E:", min_E)