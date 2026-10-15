#E22.py)Hacer una aplicacion con GUI  para cifrar un mensaje con cifrado Vigenere. Debe funcionar para mensajes con "Ñ", Generar .exe.import tkinter as tk.
import tkinter as tk
from tkinter import ttk, messagebox

# Alfabeto en español (27 letras incluida la ñ)
ALFABETO_LOWER = "abcdefghijklmnñopqrstuvwxyz"
ALFABETO_UPPER = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = len(ALFABETO_LOWER)  # 27


def vigenere_transform(texto, clave, modo='cifrar'):
    """
    Cifra o descifra un texto mediante el algoritmo Vigenère
    respetando el alfabeto en español con 'Ñ'.
    """
    if not clave:
        raise ValueError("Debes ingresar una clave.")

#  clave para pasar los desplazamientos numéricos
    clave_indices = []
    for char in clave:
        if char in ALFABETO_LOWER:
            clave_indices.append(ALFABETO_LOWER.index(char))
        elif char in ALFABETO_UPPER:
            clave_indices.append(ALFABETO_UPPER.index(char))

    if not clave_indices:
        raise ValueError("La clave debe contener al menos una letra válida.")

    resultado = []
    idx_clave = 0
    len_clave = len(clave_indices)

    for char in texto:
        if char in ALFABETO_LOWER:
            idx_orig = ALFABETO_LOWER.index(char)
            shift = clave_indices[idx_clave % len_clave]
            
            if modo == 'cifrar':
                nuevo_idx = (idx_orig + shift) % N
            else:
                nuevo_idx = (idx_orig - shift) % N
                
            resultado.append(ALFABETO_LOWER[nuevo_idx])
            idx_clave += 1

        elif char in ALFABETO_UPPER:
            idx_orig = ALFABETO_UPPER.index(char)
            shift = clave_indices[idx_clave % len_clave]
            
            if modo == 'cifrar':
                nuevo_idx = (idx_orig + shift) % N
            else:
                nuevo_idx = (idx_orig - shift) % N
                
            resultado.append(ALFABETO_UPPER[nuevo_idx])
            idx_clave += 1

        else:
# Los espacios, números y símbolos se mantienen igual
            resultado.append(char)

    return "".join(resultado)


class VigenereDarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado Vigenère")
        self.root.geometry("450x430")
        self.root.resizable(False, False)
        
# Estilo Dark + Celeste para la interfaz grafica
        BG_COLOR = "#1e1e1e"
        TEXT_COLOR = "#ffffff"
        ACCENT_CELESTE = "#00bcd4"
        TEXT_AREA_BG = "#121212"

        self.root.configure(bg=BG_COLOR)

# Configurar Estilos TTK
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure(
            "Celeste.TButton",
            font=("Helvetica", 9, "bold"),
            background="#252526",
            foreground=ACCENT_CELESTE,
            bordercolor=ACCENT_CELESTE,
            lightcolor=ACCENT_CELESTE,
            darkcolor=ACCENT_CELESTE,
            borderwidth=1,
            focusthickness=1,
            focuscolor=ACCENT_CELESTE
        )
        style.map(
            "Celeste.TButton",
            background=[("active", ACCENT_CELESTE)],
            foreground=[("active", "#000000")]
        )

        # Marco Principal Interfaz
        main_frame = tk.Frame(root, bg=BG_COLOR, highlightbackground=ACCENT_CELESTE, highlightthickness=1)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Título
        lbl_titulo = tk.Label(
            main_frame, 
            text="Cifrador / Descifrador Vigenère", 
            font=("Helvetica", 12, "bold"),
            bg=BG_COLOR,
            fg=ACCENT_CELESTE
        )
        lbl_titulo.pack(pady=(10, 6))

        # Entrada de Clave
        lbl_clave = tk.Label(main_frame, text="Palabra Clave (Secreta):", font=("Helvetica", 9, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
        lbl_clave.pack(anchor=tk.W, padx=12, pady=(4, 0))

        self.entry_clave = tk.Entry(
            main_frame, 
            font=("Helvetica", 10), 
            bg=TEXT_AREA_BG, 
            fg=TEXT_COLOR, 
            insertbackground=TEXT_COLOR,
            highlightbackground=ACCENT_CELESTE,
            highlightcolor=ACCENT_CELESTE,
            highlightthickness=1,
            bd=0
        )
        self.entry_clave.pack(fill=tk.X, padx=12, pady=2, ipady=3)

        # Mensaje de Entrada
        lbl_entrada = tk.Label(main_frame, text="Mensaje de Entrada:", font=("Helvetica", 9, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
        lbl_entrada.pack(anchor=tk.W, padx=12, pady=(8, 0))

        self.txt_entrada = tk.Text(
            main_frame, 
            height=3, 
            font=("Consolas", 9), 
            bg=TEXT_AREA_BG, 
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            highlightbackground=ACCENT_CELESTE,
            highlightcolor=ACCENT_CELESTE,
            highlightthickness=1,
            bd=0
        )
        self.txt_entrada.pack(fill=tk.X, padx=12, pady=2)

        # Botones para Cifrar / Descifrar
        frame_botones = tk.Frame(main_frame, bg=BG_COLOR)
        frame_botones.pack(fill=tk.X, padx=12, pady=10)

        btn_cifrar = ttk.Button(frame_botones, text="🔒 Cifrar", style="Celeste.TButton", command=self.cifrar)
        btn_cifrar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 4))

        btn_descifrar = ttk.Button(frame_botones, text="🔓 Descifrar", style="Celeste.TButton", command=self.descifrar)
        btn_descifrar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(4, 0))

        # Mensaje de Salida
        lbl_salida = tk.Label(main_frame, text="Resultado:", font=("Helvetica", 9, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
        lbl_salida.pack(anchor=tk.W, padx=12, pady=(6, 0))

        self.txt_salida = tk.Text(
            main_frame, 
            height=3, 
            font=("Consolas", 10, "bold"), 
            bg=TEXT_AREA_BG, 
            fg=ACCENT_CELESTE,
            insertbackground=TEXT_COLOR,
            highlightbackground=ACCENT_CELESTE,
            highlightcolor=ACCENT_CELESTE,
            highlightthickness=1,
            bd=0
        )
        self.txt_salida.pack(fill=tk.X, padx=12, pady=2)

        # Botón Copiar
        btn_copiar = ttk.Button(main_frame, text="📋 Copiar Resultado", style="Celeste.TButton", command=self.copiar_resultado)
        btn_copiar.pack(pady=10)

    def cifrar(self):
        self.procesar('cifrar')

    def descifrar(self):
        self.procesar('descifrar')

    def procesar(self, modo):
        clave = self.entry_clave.get().strip()
        texto = self.txt_entrada.get("1.0", tk.END).rstrip('\n')

        if not texto:
            messagebox.showwarning("Atención", "Ingresa un mensaje para procesar.")
            return

        try:
            resultado = vigenere_transform(texto, clave, modo=modo)
            self.txt_salida.delete("1.0", tk.END)
            self.txt_salida.insert(tk.END, resultado)
        except ValueError as e:
            messagebox.showerror("Error de Clave", str(e))

    def copiar_resultado(self):
        resultado = self.txt_salida.get("1.0", tk.END).rstrip('\n')
        if resultado:
            self.root.clipboard_clear()
            self.root.clipboard_append(resultado)
            messagebox.showinfo("Copiado", "El resultado ha sido copiado al portapapeles.")


if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereDarkApp(root)
    root.mainloop()