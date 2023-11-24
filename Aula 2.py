# from tkinter import *

#  Personalizando Janelas. Efeitando as coisas CustomTkinter

# Tudo isso pertence ao TKinter
#janela = Tk()
#janela.geometry("500x300")

#def clique():
#    print("Fazer Login")
    

#texto = Label(janela, text="Fazer Login")
#texto.pack(padx=30, pady= 10)

#botao = Button(janela, text="Login", command=clique)
#botao.pack(padx=10, pady= 10)

#janela.mainloop()

# Já para efeitar iremos utilizar o customtkinter, nao vem instalado
# temo que baixar pip install customtkinter

from customtkinter import *


#parametros Tkinter
set_appearance_mode("dark")
set_default_color_theme("dark-blue")


## parametros Tkinter



janela = CTk()
janela.geometry("600x400")

def clique():
   print("Fazer Login")

texto = CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

# entradas
email = CTkEntry(janela, placeholder_text="Seu E-mail")
email.pack(padx=10, pady=10)
senha = CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)
## entradas

# checkbox

checkbox = CTkCheckBox(janela, text="Lembrar senha")
checkbox.pack(padx=10, pady=10)


## checkbox

# botoes
botao = CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)
botao_Cadastrar = CTkButton(janela, text="Cadastrar")
botao_Cadastrar.pack(padx=10, pady=10)
bota_Esqueci = CTkButton(janela, text="Esqueci a senha")
bota_Esqueci.pack(padx=10, pady=10)

## botoes



janela.mainloop()

