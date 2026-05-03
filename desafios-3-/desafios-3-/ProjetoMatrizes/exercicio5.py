import numpy as np

# Gera matriz 2x3 de estoque com números inteiros (entre 10 e 100 unidades)
estoque = np.random.randint(10, 100, size=(2, 3))

# Gera matriz 2x1 de preços aleatórios (entre R$ 5.00 e R$ 50.00)
precos = np.round(np.random.uniform(5, 50, size=(2, 1)), 2)

print("Matriz de Estoque gerada (Produtos x Lojas):")
print(estoque)
print("\nMatriz de Preços gerada (Produtos x 1):")
print(precos)
print("-" * 30)

# Transpondo para Lojas x Produtos e multiplicando pelos preços
estoque_t = estoque.T
totais = np.dot(estoque_t, precos)

print("Totais por loja (R$):")
for i, total in enumerate(totais):
    print(f"Loja {i+1}: R$ {total[0]:.2f}")
