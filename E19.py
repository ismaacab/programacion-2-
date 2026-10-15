import random
import tkinter as tk
from tkinter import messagebox
import platform

class AdivinaNumeroThonny:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número - Thonny")
        self.root.geometry("420x450")
        self.root.config(bg="#E0F2FE")  # Celeste suave
        self.root.resizable(False, False)

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.sistema = platform.system()

        # Título
        self.titulo = tk.Label(
            root, 
            text="🎯 Adivina el Número", 
            font=("Arial", 18, "bold"), 
            bg="#E0F2FE", 
            fg="#0F172A"  # Negro/Gris muy oscuro
        )
        self.titulo.pack(pady=20)

        # Instrucción
        self.instruccion = tk.Label(
            root, 
            text="He pensado en un número del 1 al 100.\n¿Cuál crees que es?", 
            font=("Arial", 11), 
            bg="#E0F2FE", 
            fg="#1E293B",
            justify="center"
        )
        self.instruccion.pack(pady=5)

        # Campo de entrada
        self.entrada = tk.Entry(
            root, 
            font=("Arial", 16), 
            justify="center", 
            bg="#FFFFFF", 
            fg="#0F172A",
            relief="solid",
            bd=1
        )
        self.entrada.pack(pady=15, ipady=5, ipadx=10)
        self.entrada.focus()
        
        # Vincular Enter
        self.entrada.bind("<Return>", lambda event: self.verificar_intento())

        # Botón de Adivinar
        self.btn_adivinar = tk.Button(
            root, 
            text="Adivinar", 
            font=("Arial", 12, "bold"), 
            bg="#38BDF8",  # Celeste vivo
            fg="#0F172A", 
            activebackground="#0EA5E9",
            activeforeground="#000000",
            relief="raised",
            bd=2,
            cursor="hand2",
            command=self.verificar_intento
        )
        self.btn_adivinar.pack(pady=5, ipadx=20, ipady=5)

        # Etiqueta de pistas
        self.lbl_pista = tk.Label(
            root, 
            text="", 
            font=("Arial", 11, "bold"), 
            bg="#E0F2FE", 
            fg="#0369A1"
        )
        self.lbl_pista.pack(pady=15)

        # Contador de intentos
        self.lbl_intentos = tk.Label(
            root, 
            text="Intentos: 0", 
            font=("Arial", 10), 
            bg="#E0F2FE", 
            fg="#334155"
        )
        self.lbl_intentos.pack(pady=5)

        # Botón de Reiniciar
        self.btn_reiniciar = tk.Button(
            root, 
            text="Jugar de nuevo", 
            font=("Arial", 10, "bold"), 
            bg="#94A3B8", 
            fg="#0F172A",
            state="disabled",
            command=self.reiniciar_juego
        )
        self.btn_reiniciar.pack(pady=10)

    def reproducir_sonido(self, tipo):
        """Genera un sonido simple según la plataforma sin instalar nada extra"""
        try:
            if self.sistema == "Windows":
                import winsound
                if tipo == "click":
                    winsound.Beep(1000, 50)  # Tono corto y agudo
                elif tipo == "error":
                    winsound.Beep(400, 150)  # Tono grave
                elif tipo == "win":
                    winsound.Beep(1200, 100)
                    winsound.Beep(1500, 150)
            else:
                # En Linux/Mac usa el sonido por defecto de la terminal si está disponible
                print('\a', end='') 
        except:
            pass

    def verificar_intento(self):
        texto_ingresado = self.entrada.get()
        
        if not texto_ingresado.isdigit():
            self.reproducir_sonido("error")
            messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
            self.entrada.delete(0, tk.END)
            return

        intento = int(texto_ingresado)
        self.intentos += 1
        self.lbl_intentos.config(text=f"Intentos: {self.intentos}")

        if intento < 1 or intento > 100:
            self.reproducir_sonido("error")
            self.lbl_pista.config(text="⚠️ Debe ser entre 1 y 100.", fg="#B91C1C")
        elif intento < self.numero_secreto:
            self.reproducir_sonido("click")
            self.lbl_pista.config(text="📈 Demasiado bajo. ¡Sube más!", fg="#0369A1")
        elif intento > self.numero_secreto:
            self.reproducir_sonido("click")
            self.lbl_pista.config(text="📉 Demasiado alto. ¡Baja un poco!", fg="#0369A1")
        else:
            self.reproducir_sonido("win")
            self.lbl_pista.config(
                text=f"🎉 ¡Felicidades! ¡Era el {self.numero_secreto}!", 
                fg="#15803D"
            )
            messagebox.showinfo("¡Ganaste!", f"¡Adivinaste el número en {self.intentos} intentos!")
            self.btn_adivinar.config(state="disabled")
            self.entrada.config(state="disabled")
            self.btn_reiniciar.config(state="normal", bg="#38BDF8")

        self.entrada.delete(0, tk.END)

    def reiniciar_juego(self):
        self.reproducir_sonido("click")
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.lbl_intentos.config(text="Intentos: 0")
        self.lbl_pista.config(text="")
        self.entrada.config(state="normal")
        self.btn_adivinar.config(state="normal")
        self.btn_reiniciar.config(state="disabled", bg="#94A3B8")
        self.entrada.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaNumeroThonny(root)
    root.mainloop()