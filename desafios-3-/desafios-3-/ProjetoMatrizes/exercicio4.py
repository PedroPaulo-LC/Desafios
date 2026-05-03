import numpy as np

print("🧮 ANALISADOR DE SISTEMAS LINEARES 🧮")
print("-" * 40)

# Gera uma matriz 3x3 com coeficientes aleatórios inteiros entre -10 e 10
# (o limite superior exclusivo é 11 para que o 10 possa aparecer)
coeficientes = np.random.randint(-10, 11, size=(3, 3))

print("Matriz de Coeficientes do Sistema (Gerada Aleatoriamente):")
print(coeficientes)
print("-" * 40)

# Calculando o determinante
determinante = np.linalg.det(coeficientes)

print(f"Determinante calculado: {determinante:.2f}")

# Verificando se o sistema é resolvível
if abs(determinante) > 0.0001:  # Usamos abs() e um valor pequeno para evitar erros de arredondamento do Python
    print("\n✅ Conclusão: O sistema é RESOLVÍVEL (a matriz possui inversa).")
else:
    print("\n❌ Conclusão: O sistema NÃO é resolvível (a matriz é singular).")