import customtkinter as ctk

from login import mostrar_login
from menu import mostrar_menu
#from cadastro import mostrar_cadastro

ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul


janela = ctk.CTk()
janela.title("Sistema de Gestão")
janela.geometry("750x550")
janela.minsize(650, 450)


# Funções de navegação
def abrir_login():
    mostrar_login(janela, abrir_menu)

def abrir_menu():
    mostrar_menu(janela, abrir_login, abrir_cadastro)

def abrir_cadastro():
    mostrar_cadastro(janela, abrir_menu)


# Primeira tela a ser exibida
abrir_login()            

# Mantém a janela aberta
janela.mainloop()   
