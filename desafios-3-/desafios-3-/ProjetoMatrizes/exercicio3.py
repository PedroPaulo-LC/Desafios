import numpy as np

# Gera uma matriz 3x3 com notas aleatórias entre 0 e 10
# O np.round(_, 1) arredonda para ter apenas 1 casa decimal (ex: 7.5)
notas = np.round(np.random.uniform(0, 10, size=(3, 3)), 1)

print("Matriz de notas gerada aleatoriamente:")
print(notas)
print("-" * 30)

# Calculando a média por linha (axis=1)
medias = np.mean(notas, axis=1)

print("Médias dos alunos:")
for i, media in enumerate(medias):
    print(f"Aluno {i+1}: {media:.2f}") 