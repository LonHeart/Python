from tkinter import *

# Multiplas Janelas e organização de Botões e Texto

def abrir_janela():
    janela_2 = Toplevel(janela_prinpal)
    janela_2.geometry("750x250")
    janela_2.title("Janela Nova")
    label_nome = Label(janela_2, text="nome")
    label_nome.grid(column=0, row=0, padx=325, pady=50)
    botão_voltar = Button(janela_2, text= "Cancelar", command=janela_2.destroy)
    botão_voltar.grid(column=0, row=1, padx=325, pady=100)



# Janela Principal
janela_prinpal = Tk()
janela_prinpal.geometry("750x250")
botão = Button(janela_prinpal, text="Proxima Janela", command= abrir_janela)
botão.grid(column=0, row=0, padx=325, pady=100)


janela_prinpal.mainloop()
##


