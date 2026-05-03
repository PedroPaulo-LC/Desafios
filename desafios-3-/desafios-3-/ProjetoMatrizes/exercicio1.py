import random

# Matriz 3x3 com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo com números aleatórios
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 100)

print("Matriz 3x3 aleatória:")
for linha in matriz:
    print(linha)
