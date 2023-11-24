import requests
from tkinter import *

# Criando janelas e botões

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]

    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto_cotacao["text"] = f'''
    Dolar: {cotacao_dolar}
    BTC: {cotacao_btc}'''

   

# Interface
# Janela
janela = Tk()
janela.title("Cotação Atual de Moedas")
##


texto_inicial = Label(janela, text="Clique no botão para exibir a cotação")
texto_inicial.grid(column=0, row=0,)

botao = Button(janela, text="Revelar", command=pegar_cotacoes)
botao.grid(column=0, row=1)

texto_cotacao = Label(janela, text="0")
texto_cotacao.grid(column=0, row=2)


janela.mainloop()
# Fim da Interface