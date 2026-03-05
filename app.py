import customtkinter as ctk

# Configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TunicoQuestApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tunico Quest - Sistema de Recompensas")
        self.geometry("1000x600")
        self.configure(fg_color="#0b0f19") # Fundo azul escuro profundo

        # Variável de saldo (iniciando com 48h como na imagem)
        self.saldo_horas = 48

        self.setup_ui()

    def setup_ui(self):
        # --- TÍTULO PRINCIPAL ---
        self.titulo = ctk.CTkLabel(self, text="TUNICO QUEST - SISTEMA DE RECOMPENSAS GAMER", 
                                  font=("Orbitron", 24, "bold"), text_color="#50f2d3")
        self.titulo.pack(pady=20)

        # --- CONTAINER PRINCIPAL (Split Horizontal) ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20)

        # Lado Esquerdo: Cards de Tarefas
        self.left_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10)

        # Lado Direito: Legenda e Progresso
        self.right_frame = ctk.CTkFrame(self.main_container, fg_color="#161b28", border_color="#3a445b", border_width=2)
        self.right_frame.pack(side="right", fill="both", padx=10, pady=10, ipadx=20)

        self.create_top_bar()
        self.create_task_cards()
        self.create_legend()

    def create_top_bar(self):
        # Card do Saldo de Horas
        self.saldo_frame = ctk.CTkFrame(self.left_frame, fg_color="#1a1f2e", border_color="#4d4dff", border_width=1)
        self.saldo_frame.pack(fill="x", pady=10)

        self.lbl_saldo_txt = ctk.CTkLabel(self.saldo_frame, text="🎮 SALDO DE HORAS JOGO:", font=("Arial", 18, "bold"))
        self.lbl_saldo_txt.pack(side="left", padx=20, pady=15)

        self.lbl_horas = ctk.CTkLabel(self.saldo_frame, text=f"{self.saldo_horas}h", 
                                     font=("Arial", 32, "bold"), text_color="#00ffff")
        self.lbl_horas.pack(side="right", padx=20)

    def create_task_cards(self):
        tarefas = [
            ("FEZ O DEVER DE CASA", "📚"),
            ("leitura", "👨‍🏫"),
            ("SE COMPORTOU BEM", "😊"),
            ("NÃO XINGOU", "💬"),
            ("OBEDECEU EM CASA", "🧹"),
            ("FOI DEITAR NO HORÁRIO", "⏰")
        ]

        # Grid de 2 colunas para os cards
        grid_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True)

        for i, (nome, icone) in enumerate(tarefas):
            row = i // 2
            col = i % 2
            
            card = ctk.CTkFrame(grid_frame, fg_color="#1a1f2e", border_color="#31e89f", border_width=1)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            lbl_icon = ctk.CTkLabel(card, text=icone, font=("Arial", 25))
            lbl_icon.pack(side="left", padx=15)

            info_frame = ctk.CTkFrame(card, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, pady=10)

            ctk.CTkLabel(info_frame, text=nome, font=("Arial", 12, "bold")).pack(anchor="w")
            
            # Barra de progresso fictícia
            prog = ctk.CTkProgressBar(info_frame, progress_color="#31e89f", height=8)
            prog.set(0.6)
            prog.pack(fill="x", pady=5, padx=(0, 20))

            # Botões +/-
            btn_frame = ctk.CTkFrame(card, fg_color="transparent")
            btn_frame.pack(side="right", padx=10)
            
            ctk.CTkButton(btn_frame, text="-", width=30, fg_color="#2b313e", command=self.update_saldo_minus).pack(side="left", padx=2)
            ctk.CTkButton(btn_frame, text="+", width=30, fg_color="#2b313e", command=self.update_saldo_plus).pack(side="left", padx=2)

    def create_legend(self):
        title_leg = ctk.CTkLabel(self.right_frame, text="LEGENDA DE PONTOS", font=("Arial", 16, "bold"), text_color="white")
        title_leg.pack(pady=20)

        legendas = [
            ("🟡 PONTO = 1 HORA JOGO"),
            ("✅ PERFEITO = 1 PONTO"),
            ("⭐ DIFICULDADE = 2 PONTOS")
        ]

        for text in legendas:
            ctk.CTkLabel(self.right_frame, text=text, font=("Arial", 13), text_color="#f0f0f0").pack(pady=5, anchor="w", padx=10)

    def update_saldo_plus(self):
        self.saldo_horas += 1
        self.lbl_horas.configure(text=f"{self.saldo_horas}h")

    def update_saldo_minus(self):
        if self.saldo_horas > 0:
            self.saldo_horas -= 1
            self.lbl_horas.configure(text=f"{self.saldo_horas}h")

if __name__ == "__main__":
    app = TunicoQuestApp()
    app.mainloop()
