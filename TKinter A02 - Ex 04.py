import requests
import tkinter as tk

#print(cotacao['USD']['bid'])
#print(cotacao['EUR']['bid'])

def cot():

    requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL")
    cotacao = requisicao.json()
    lable01["text"] = f"DOLAR {cotacao['USD']['bid']}"
    lable02["text"] = f"EURO {cotacao['EUR']['bid']}"

tela = tk.Tk()

tela.title("DOLAR EURO")

botao01 = tk.Button(tela, text="COTAÇÃO", font=("arial", 11), bg="#9fadcc", command=cot)

lable01= tk.Label(tela,text="")
lable02= tk.Label(tela,text="")

botao01.pack()

lable01.pack()
lable02.pack()