"""

ATIVIDADE 04

Utilizando funções, crie a lógica de um programa

que sorteie seis números aleatórios,

inteiros e NÃO REPETIDOS para um jogo de loteria.

https://dontpad.herokuapp.com/aaf

"""

import tkinter as tk

import random


def sorteio():
    numeros = []

    for i in range(1, 61):
        numeros.append(i)
    lable01["text"]=random.sample(numeros, k=6)

tela = tk.Tk()

tela.title("Sorteio")

botao01 = tk.Button(tela, text="APERTE PARA SORTEAR", font=("arial", 11), bg="#181d29", command=sorteio)

lable01= tk.Label(tela,text="")

botao01.pack()

lable01.pack()

tela.mainloop()





