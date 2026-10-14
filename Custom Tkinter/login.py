# import customtkinter as ctk
# from tkinter import messagebox
 
# def mostrar_login(janela, abrir_menu):
 
#     # Remove os componentes da tela anterior
#     for componente in janela.winfo_children():
#         componente.destroy()
 
#     janela.title("Login - Sistema de Gestão")
 
#     titulo = ctk.CTkLabel(
#         janela,
#         text="Sistema de Gestão",
#         font=("Arial", 26, "bold")
#     )
#     titulo.pack(pady=(60, 25))
 
#     usuario = ctk.CTkEntry(
#         janela,
#         width=280,
#         placeholder_text="Digite seu usuário"
#     )
#     usuario.pack(pady=10)
 
#     senha = ctk.CTkEntry(
#         janela,
#         width=280,
#         placeholder_text="Digite sua senha",
#         show="*"
#     )
#     senha.pack(pady=10)
 
#     def validar_login():
#         nome_usuario = usuario.get()
#         senha_digitada = senha.get()
 
#         if nome_usuario == "admin" and senha_digitada == "1234":
#             abrir_menu()
#         else:
#             messagebox.showerror(
#                 "Erro",
#                 "Usuário ou senha incorretos!"
#             )
 
#     botao = ctk.CTkButton(
#         janela,
#         text="Entrar",
#         width=280,
#         command=validar_login
#     )
#     botao.pack(pady=20)
 
#     ctk.CTkLabel(
#         janela,
#         text="Usuário: admin | Senha: 1234",
#         text_color="gray"
#     ).pack(pady=5)







# ------------------    Codifo gerado pelo visual code --------------------------
# import customtkinter as ctk
# from tkinter import messagebox

# def mostrar_login(janela, abrir_menu):
#     # Limpa a janela antes de exibir o login
#     for componente in janela.winfo_children():
#         componente.destroy()

#     # Criação do frame de login
#     # janela.tittle("Login - Sistema de Gestão")  

#     # Título do login
#     label_titulo = ctk.CTkLabel(janela, text="Login - Sistema de Gestão", font=("Arial", 50))
#     label_titulo.pack(pady=20)

#     # Campo de usuário
#     label_usuario = ctk.CTkLabel(janela, text="Usuário:")
#     label_usuario.pack(pady=5)
#     entry_usuario = ctk.CTkEntry(janela, width=280)
#     entry_usuario.pack(pady=5)

#     # Campo de senha
#     label_senha = ctk.CTkLabel(janela, text="Senha:")
#     label_senha.pack(pady=5)
#     entry_senha = ctk.CTkEntry(janela, show="*", width=280)
#     entry_senha.pack(pady=5)

#     # Função para validar o login
#     def validar_login():
#         usuario = entry_usuario.get()
#         senha = entry_senha.get()
#         if usuario == "admin" and senha == "1234":  # Exemplo de validação simples
#             abrir_menu()
#         else:
#             messagebox.showerror("Erro", "Usuário ou senha incorretos!")

#     # Botão de login
#     botao_login = ctk.CTkButton(janela, text="Entrar", width=280, command=validar_login)
#     botao_login.pack(pady=20)


import customtkinter as ctk
from tkinter import messagebox

# ---------- Paleta ----------
COR_FUNDO = "#0F172A"        # azul-ardósia escuro
COR_CARD = "#1E293B"         # cartão de login
COR_CAMPO = "#0F172A"        # fundo dos campos
COR_BORDA = "#334155"
COR_TEXTO = "#F1F5F9"
COR_TEXTO_SUAVE = "#94A3B8"
COR_DESTAQUE = "#3B82F6"
COR_DESTAQUE_HOVER = "#2563EB"
COR_ERRO = "#F87171"

FONTE = "Segoe UI"


def mostrar_login(janela, abrir_menu):
    # Limpa a janela antes de exibir o login
    for componente in janela.winfo_children():
        componente.destroy()

    janela.title("Login - Sistema de Gestão")
    janela.configure(fg_color=COR_FUNDO)

    # Container centralizado
    card = ctk.CTkFrame(
        janela,
        width=400,
        corner_radius=20,
        fg_color=COR_CARD,
        border_width=1,
        border_color=COR_BORDA,
    )
    card.place(relx=0.5, rely=0.5, anchor="center")

    # Cabeçalho
    ctk.CTkLabel(
        card,
        text="Sistema de Gestão",
        font=(FONTE, 28, "bold"),
        text_color=COR_TEXTO,
    ).pack(padx=40, pady=(40, 4))

    ctk.CTkLabel(
        card,
        text="Entre com sua conta para continuar",
        font=(FONTE, 14),
        text_color=COR_TEXTO_SUAVE,
    ).pack(padx=40, pady=(0, 28))

    # Campo de usuário
    ctk.CTkLabel(
        card, text="Usuário", font=(FONTE, 13, "bold"),
        text_color=COR_TEXTO_SUAVE, anchor="w",
    ).pack(fill="x", padx=40, pady=(0, 4))

    entry_usuario = ctk.CTkEntry(
        card,
        placeholder_text="Digite seu usuário",
        height=44,
        corner_radius=10,
        font=(FONTE, 14),
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
        text_color=COR_TEXTO,
    )
    entry_usuario.pack(fill="x", padx=40, pady=(0, 16))

    # Campo de senha
    ctk.CTkLabel(
        card, text="Senha", font=(FONTE, 13, "bold"),
        text_color=COR_TEXTO_SUAVE, anchor="w",
    ).pack(fill="x", padx=40, pady=(0, 4))

    entry_senha = ctk.CTkEntry(
        card,
        placeholder_text="Digite sua senha",
        show="•",
        height=44,
        corner_radius=10,
        font=(FONTE, 14),
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
        text_color=COR_TEXTO,
    )
    entry_senha.pack(fill="x", padx=40, pady=(0, 8))

    # Mostrar/ocultar senha
    def alternar_senha():
        entry_senha.configure(show="" if mostrar_var.get() else "•")

    mostrar_var = ctk.BooleanVar(value=False)
    ctk.CTkCheckBox(
        card,
        text="Mostrar senha",
        variable=mostrar_var,
        command=alternar_senha,
        font=(FONTE, 12),
        text_color=COR_TEXTO_SUAVE,
        fg_color=COR_DESTAQUE,
        hover_color=COR_DESTAQUE_HOVER,
        border_color=COR_BORDA,
        checkbox_width=18,
        checkbox_height=18,
    ).pack(anchor="w", padx=40, pady=(0, 12))

    # Mensagem de erro (inline, sem popup)
    label_erro = ctk.CTkLabel(
        card, text="", font=(FONTE, 12), text_color=COR_ERRO,
    )
    label_erro.pack(padx=40, pady=(0, 4))

    # Validação
    def validar_login(event=None):
        usuario = entry_usuario.get().strip()
        senha = entry_senha.get()

        if not usuario or not senha:
            label_erro.configure(text="Preencha usuário e senha.")
            return

        if usuario == "admin" and senha == "1234":  # Exemplo de validação simples
            abrir_menu()
        else:
            label_erro.configure(text="Usuário ou senha incorretos.")
            entry_senha.delete(0, "end")
            entry_senha.focus()

    # Botão de login
    ctk.CTkButton(
        card,
        text="Entrar",
        height=46,
        corner_radius=10,
        font=(FONTE, 15, "bold"),
        fg_color=COR_DESTAQUE,
        hover_color=COR_DESTAQUE_HOVER,
        command=validar_login,
    ).pack(fill="x", padx=40, pady=(4, 40))

    # Enter envia o formulário; foco inicial no usuário
    entry_usuario.bind("<Return>", lambda e: entry_senha.focus())
    entry_senha.bind("<Return>", validar_login)
    entry_usuario.focus()


# ---------- Teste rápido ----------
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.geometry("900x600")
    app.minsize(480, 560)

    def abrir_menu_teste():
        messagebox.showinfo("Login", "Login realizado com sucesso!")

    mostrar_login(app, abrir_menu_teste)
    app.mainloop()