# import customtkinter as ctk
 
 
# def mostrar_menu(janela, abrir_login, abrir_cadastro):
 
#     for componente in janela.winfo_children():
#         componente.destroy()
 
#     janela.title("Menu Principal")
 
#     titulo = ctk.CTkLabel(
#         janela,
#         text="Menu Principal",
#         font=("Arial", 28, "bold")
#     )
#     titulo.pack(pady=(35, 10))
 
#     ctk.CTkLabel(
#         janela,
#         text="Selecione uma opção abaixo"
#     ).pack(pady=(0, 20))
 
#     area_cards = ctk.CTkFrame(
#         janela,
#         fg_color="transparent"
#     )
#     area_cards.pack(pady=10)
 
#     # Card Clientes
#     clientes = ctk.CTkFrame(
#         area_cards,
#         width=190,
#         height=180
#     )
#     clientes.grid(row=0, column=0, padx=8, pady=10)
#     clientes.pack_propagate(False)
 
#     ctk.CTkLabel(
#         clientes,
#         text="Clientes",
#         font=("Arial", 20, "bold")
#     ).pack(pady=(30, 15))
 
#     ctk.CTkLabel(
#         clientes,
#         text="Cadastro de clientes"
#     ).pack(pady=5)
 
#     ctk.CTkButton(
#         clientes,
#         text="Acessar",
#         command=abrir_cadastro
#     ).pack(pady=15)
 
#     # Card Produtos
#     produtos = ctk.CTkFrame(
#         area_cards,
#         width=190,
#         height=180
#     )
#     produtos.grid(row=0, column=1, padx=8, pady=10)
#     produtos.pack_propagate(False)
 
#     ctk.CTkLabel(
#         produtos,
#         text="Produtos",
#         font=("Arial", 20, "bold")
#     ).pack(pady=(30, 15))
 
#     ctk.CTkLabel(
#         produtos,
#         text="Gestão de produtos"
#     ).pack(pady=5)
 
#     ctk.CTkButton(
#         produtos,
#         text="Em breve",
#         state="disabled"
#     ).pack(pady=15)
 
#     # Card Relatórios
#     relatorios = ctk.CTkFrame(
#         area_cards,
#         width=190,
#         height=180
#     )
#     relatorios.grid(row=0, column=2, padx=8, pady=10)
#     relatorios.pack_propagate(False)
 
#     ctk.CTkLabel(
#         relatorios,
#         text="Relatórios",
#         font=("Arial", 20, "bold")
#     ).pack(pady=(30, 15))
 
#     ctk.CTkLabel(
#         relatorios,
#         text="Consultar informações"
#     ).pack(pady=5)
 
#     ctk.CTkButton(
#         relatorios,
#         text="Em breve",
#         state="disabled"
#     ).pack(pady=15)
 
#     ctk.CTkButton(
#         janela,
#         text="Sair",
#         fg_color="gray",
#         command=abrir_login
#     ).pack(pady=20)


import customtkinter as ctk

# ---------- Paleta (mesma do login) ----------
COR_FUNDO = "#0F172A"
COR_CARD = "#1E293B"
COR_BORDA = "#334155"
COR_TEXTO = "#F1F5F9"
COR_TEXTO_SUAVE = "#94A3B8"
COR_DESTAQUE = "#3B82F6"
COR_DESTAQUE_HOVER = "#2563EB"
COR_DESABILITADO = "#334155"
COR_SAIR_HOVER = "#7F1D1D"

FONTE = "Segoe UI"


def criar_card(pai, coluna, titulo, descricao, texto_botao, comando=None):
    """Cria um card do menu. Sem comando, o botão fica desabilitado."""
    ativo = comando is not None

    card = ctk.CTkFrame(
        pai,
        width=220,
        height=220,
        corner_radius=20,
        fg_color=COR_CARD,
        border_width=1,
        border_color=COR_BORDA,
    )
    card.grid(row=0, column=coluna, padx=12, pady=10)
    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text=titulo,
        font=(FONTE, 22, "bold"),
        text_color=COR_TEXTO if ativo else COR_TEXTO_SUAVE,
    ).pack(pady=(34, 6))

    ctk.CTkLabel(
        card,
        text=descricao,
        font=(FONTE, 13),
        text_color=COR_TEXTO_SUAVE,
    ).pack(pady=(0, 18))

    if ativo:
        ctk.CTkButton(
            card,
            text=texto_botao,
            height=40,
            corner_radius=10,
            font=(FONTE, 14, "bold"),
            fg_color=COR_DESTAQUE,
            hover_color=COR_DESTAQUE_HOVER,
            command=comando,
        ).pack(fill="x", padx=28)
    else:
        ctk.CTkButton(
            card,
            text=texto_botao,
            height=40,
            corner_radius=10,
            font=(FONTE, 14),
            fg_color=COR_DESABILITADO,
            text_color_disabled=COR_TEXTO_SUAVE,
            state="disabled",
        ).pack(fill="x", padx=28)

    return card


def mostrar_menu(janela, abrir_login, abrir_cadastro):
    # Limpa a janela antes de exibir o menu
    for componente in janela.winfo_children():
        componente.destroy()

    janela.title("Menu Principal")
    janela.configure(fg_color=COR_FUNDO)

    # Container central que agrupa tudo e mantém o conjunto centralizado
    conteudo = ctk.CTkFrame(janela, fg_color="transparent")
    conteudo.place(relx=0.5, rely=0.5, anchor="center")

    # Cabeçalho
    ctk.CTkLabel(
        conteudo,
        text="Menu Principal",
        font=(FONTE, 32, "bold"),
        text_color=COR_TEXTO,
    ).pack(pady=(0, 4))

    ctk.CTkLabel(
        conteudo,
        text="Selecione uma opção abaixo",
        font=(FONTE, 15),
        text_color=COR_TEXTO_SUAVE,
    ).pack(pady=(0, 24))

    # Cards
    area_cards = ctk.CTkFrame(conteudo, fg_color="transparent")
    area_cards.pack()

    criar_card(
        area_cards, 0,
        "Clientes", "Cadastro de clientes",
        "Acessar", abrir_cadastro,
    )
    criar_card(
        area_cards, 1,
        "Produtos", "Gestão de produtos",
        "Em breve",
    )
    criar_card(
        area_cards, 2,
        "Relatórios", "Consultar informações",
        "Em breve",
    )

    # Botão de sair
    ctk.CTkButton(
        conteudo,
        text="Sair",
        width=160,
        height=40,
        corner_radius=10,
        font=(FONTE, 14),
        fg_color="transparent",
        border_width=1,
        border_color=COR_BORDA,
        text_color=COR_TEXTO_SUAVE,
        hover_color=COR_SAIR_HOVER,
        command=abrir_login,
    ).pack(pady=(28, 0))


# ---------- Teste rápido ----------
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.geometry("900x600")
    app.minsize(820, 560)

    mostrar_menu(
        app,
        abrir_login=lambda: print("Voltar ao login"),
        abrir_cadastro=lambda: print("Abrir cadastro"),
    )
    app.mainloop()