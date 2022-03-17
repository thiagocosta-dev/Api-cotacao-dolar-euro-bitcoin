import requests
from tkinter import *

#  Fazer a janela
janela = Tk()
janela.title('API Cotação')
janela.geometry('200x175')
janela.config(bg='#daa520')


#  Textos (Dolar, Euro e Bitcoin) na parte superior
dolar = Label(text='DÓLAR', font=('sans', 10, 'bold'), bg='#daa520')
dolar.place(x=10, y=15)
euro = Label(text='EURO', font=('sans', 10, 'bold'), bg='#daa520')
euro.place(x=10, y=60)
bit = Label(text='BITCOIN', font=('sans', 10, 'bold'), bg='#daa520')
bit.place(x=10, y=105)


#  Função para pegar valores
def valores():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacoes_dolar = cotacoes['USDBRL']['bid']
    cotacoes_euro = cotacoes['EURBRL']['bid']
    cotacoes_bitcoin = cotacoes['BTCBRL']['bid']
    dolar_label = Label(text=cotacoes_dolar, bg='#ffffff')
    dolar_label.place(x=130, y=15)
    euro_label = Label(text=cotacoes_euro, bg='#ffffff')
    euro_label.place(x=130, y=60)
    bitcoin_label = Label(text=cotacoes_bitcoin, bg='#ffffff')
    bitcoin_label.place(x=130, y=105)


#  Botão para atualizar valores
atualiza = Button(janela, width=10, height=1, text='Atualizar', command=valores)
atualiza.place(x=50, y=135)


#  Cifrão das moedas

dolar_cifra = Label(text='US$                 ', bg='#ffffff')
dolar_cifra.place(x=90, y=15)
euro_cifra = Label(text='€                     ', bg='#ffffff')
euro_cifra.place(x=90, y=60)
bitcoin_cifra = Label(text='₿                     ', bg='#ffffff')
bitcoin_cifra.place(x=90, y=105)

janela.mainloop()
