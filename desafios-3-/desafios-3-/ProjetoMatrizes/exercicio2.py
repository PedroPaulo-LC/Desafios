# Vendas: 2 linhas (lojas) x 3 colunas (produtos)
semana1 = [[10, 15, 20], [5, 8, 12]]
semana2 = [[12, 18, 25], [7, 10, 15]]

soma = [[0, 0, 0], [0, 0, 0]]
total = 0

for i in range(2):
    for j in range(3):
        soma[i][j] = semana1[i][j] + semana2[i][j]
        total += soma[i][j]

print("Soma das vendas:")
for linha in soma:
    print(linha)
print(f"Total geral: {total}")
