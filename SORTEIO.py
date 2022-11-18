"""

ATIVIDADE 04

Utilizando funções, crie a lógica de um programa

que sorteie seis números aleatórios,

inteiros e NÃO REPETIDOS para um jogo de loteria.

"""

import random

numeros = []

for i in range(1, 61):

    numeros.append(i)



print(numeros)



print(random.sample(numeros, k=6))