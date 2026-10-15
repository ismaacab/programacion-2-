import random
import tkinter as tk
from tkinter import font

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera - Modern Edition")
        self.root.geometry("450x620")
        self.root.config(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.user_score = 0
        self.comp_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Fuentes personalizadas
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        score_font = font.Font(family="Helvetica", size=12)
        result_font = font.Font(family="Helvetica", size=14, weight="bold")
        choice_font = font.Font(family="Segoe UI Emoji", size=45)

        # Título principal
        title_label = tk.Label(self.root, text="Piedra, Papel o Tijera", font=title_font, bg="#1e1e2f", fg="#ffffff")
        title_label.pack(pady=20)

        # Tarjeta de Marcador
        score_frame = tk.Frame(self.root, bg="#2d2d44", padx=20, pady=10)
        score_frame.pack(pady=10, fill="x", padx=30)
        
        self.score_label = tk.Label(
            score_frame, 
            text=f"Jugador: {self.user_score} | Computadora: {self.comp_score}", 
            font=score_font, 
            bg="#2d2d44", 
            fg="#4ecca3"
        )
        self.score_label.pack()

        # Área de visualización de elecciones (Jugador vs Computadora)
        display_frame = tk.Frame(self.root, bg="#1e1e2f")
        display_frame.pack(pady=20)

        # Elección del Jugador
        p_frame = tk.Frame(display_frame, bg="#2d2d44", padx=15, pady=10)
        p_frame.grid(row=0, column=0, padx=15)
        tk.Label(p_frame, text="Tú", font=score_font, bg="#2d2d44", fg="#a0a0c0").pack()
        self.p_choice_label = tk.Label(p_frame, text="❓", font=choice_font, bg="#2d2d44", fg="#ffffff")
        self.p_choice_label.pack(pady=5)

        # Letrero VS
        vs_label = tk.Label(display_frame, text="VS", font=font.Font(family="Helvetica", size=14, weight="bold"), bg="#1e1e2f", fg="#ff6584")
        vs_label.grid(row=0, column=1, padx=10)

        # Elección de la Computadora
        c_frame = tk.Frame(display_frame, bg="#2d2d44", padx=15, pady=10)
        c_frame.grid(row=0, column=2, padx=15)
        tk.Label(c_frame, text="Computadora", font=score_font, bg="#2d2d44", fg="#a0a0c0").pack()
        self.c_choice_label = tk.Label(c_frame, text="❓", font=choice_font, bg="#2d2d44", fg="#ffffff")
        self.c_choice_label.pack(pady=5)

        # Mensaje de resultado de la ronda
        self.result_label = tk.Label(self.root, text="¡Elige una opción para comenzar!", font=result_font, bg="#1e1e2f", fg="#f0db4f")
        self.result_label.pack(pady=15)

        # Botones de selección
        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=15)

        btn_style = {"font": ("Helvetica", 11, "bold"), "width": 10, "bd": 0, "cursor": "hand2", "relief": "flat"}

        self.btn_piedra = tk.Button(btn_frame, text="Piedra 🪨", bg="#4ecca3", fg="#1e1e2f", **btn_style, command=lambda: self.play("piedra"))
        self.btn_piedra.grid(row=0, column=0, padx=8)

        self.btn_papel = tk.Button(btn_frame, text="Papel 📄", bg="#4ecca3", fg="#1e1e2f", **btn_style, command=lambda: self.play("papel"))
        self.btn_papel.grid(row=0, column=1, padx=8)

        self.btn_tijera = tk.Button(btn_frame, text="Tijera ✂️", bg="#4ecca3", fg="#1e1e2f", **btn_style, command=lambda: self.play("tijera"))
        self.btn_tijera.grid(row=0, column=2, padx=8)

        # Botón para reiniciar el marcador
        reset_btn = tk.Button(self.root, text="Reiniciar Marcador", font=("Helvetica", 10), bg="#ff6584", fg="#ffffff", bd=0, padx=15, pady=6, cursor="hand2", command=self.reset_game)
        reset_btn.pack(pady=15)

    def play(self, user_choice):
        options = {"piedra": "🪨", "papel": "📄", "tijera": "✂️"}
        choices = ["piedra", "papel", "tijera"]
        comp_choice = random.choice(choices)

        # Actualizar visuales con emojis
        self.p_choice_label.config(text=options[user_choice])
        self.c_choice_label.config(text=options[comp_choice])

        # Lógica del ganador
        if user_choice == comp_choice:
            self.result_label.config(text="🤝 ¡Empate!", fg="#f0db4f")
        elif (user_choice == "piedra" and comp_choice == "tijera") or \
             (user_choice == "papel" and comp_choice == "piedra") or \
             (user_choice == "tijera" and comp_choice == "papel"):
            self.result_label.config(text="🎉 ¡Ganaste esta ronda!", fg="#4ecca3")
            self.user_score += 1
        else:
            self.result_label.config(text="😢 ¡Perdiste esta ronda!", fg="#ff6584")
            self.comp_score += 1

        # Actualizar el marcador en pantalla
        self.score_label.config(text=f"Jugador: {self.user_score} | Computadora: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text=f"Jugador: {self.user_score} | Computadora: {self.comp_score}")
        self.p_choice_label.config(text="❓")
        self.c_choice_label.config(text="❓")
        self.result_label.config(text="¡Marcador reiniciado! Elige una opción.", fg="#f0db4f")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()