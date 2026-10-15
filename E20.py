import tkinter as tk
from tkinter import ttk, messagebox
 
 
def cifrar_cesar(texto, desplazamiento, descifrar=False):
    """
    Aplica el cifrado César al texto dado.
    Si descifrar=True, invierte el desplazamiento.
    """
    resultado = []
    if descifrar:
        desplazamiento = -desplazamiento
 
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_pos = (ord(caracter) - base + desplazamiento) % 26
            resultado.append(chr(base + nueva_pos))
        else:
            # Los caracteres que no son letras (espacios, números, signos) no se modifican
            resultado.append(caracter)
 
    return ''.join(resultado)
 
 
class AppCifradoCesar:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado César")
        self.root.geometry("520x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")
 
        self._crear_widgets()
 
    def _crear_widgets(self):
        estilo_titulo = {"bg": "#f0f2f5", "font": ("Segoe UI", 16, "bold"), "fg": "#1a1a2e"}
        estilo_label = {"bg": "#f0f2f5", "font": ("Segoe UI", 10)}
 
        # Título
        tk.Label(self.root, text="🔐 Cifrado César", **estilo_titulo).pack(pady=(15, 10))
 
        # Texto de entrada
        tk.Label(self.root, text="Texto:", **estilo_label).pack(anchor="w", padx=30)
        self.entrada_texto = tk.Text(self.root, height=5, width=55, font=("Segoe UI", 10),
                                      wrap="word", relief="solid", borderwidth=1)
        self.entrada_texto.pack(padx=30, pady=(0, 10))
 
        # Frame para desplazamiento
        frame_despl = tk.Frame(self.root, bg="#f0f2f5")
        frame_despl.pack(fill="x", padx=30, pady=5)
 
        tk.Label(frame_despl, text="Desplazamiento (clave):", **estilo_label).pack(side="left")
        self.var_desplazamiento = tk.IntVar(value=3)
        spin = ttk.Spinbox(frame_despl, from_=1, to=25, textvariable=self.var_desplazamiento,
                            width=5, font=("Segoe UI", 10))
        spin.pack(side="left", padx=10)
 
        # Botones de acción
        frame_botones = tk.Frame(self.root, bg="#f0f2f5")
        frame_botones.pack(pady=15)
 
        btn_cifrar = tk.Button(frame_botones, text="Cifrar", width=15,
                                bg="#4361ee", fg="white", font=("Segoe UI", 10, "bold"),
                                relief="flat", command=self.cifrar)
        btn_cifrar.grid(row=0, column=0, padx=5)
 
        btn_descifrar = tk.Button(frame_botones, text="Descifrar", width=15,
                                   bg="#3a0ca3", fg="white", font=("Segoe UI", 10, "bold"),
                                   relief="flat", command=self.descifrar)
        btn_descifrar.grid(row=0, column=1, padx=5)
 
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", width=15,
                                 bg="#adb5bd", fg="white", font=("Segoe UI", 10, "bold"),
                                 relief="flat", command=self.limpiar)
        btn_limpiar.grid(row=0, column=2, padx=5)
 
        # Resultado
        tk.Label(self.root, text="Resultado:", **estilo_label).pack(anchor="w", padx=30)
        self.salida_texto = tk.Text(self.root, height=5, width=55, font=("Segoe UI", 10),
                                     wrap="word", relief="solid", borderwidth=1, bg="#eef1f5")
        self.salida_texto.pack(padx=30, pady=(0, 10))
 
        # Botón copiar
        btn_copiar = tk.Button(self.root, text="📋 Copiar resultado", bg="#06d6a0", fg="white",
                                font=("Segoe UI", 9, "bold"), relief="flat", command=self.copiar)
        btn_copiar.pack()
 
    def _obtener_texto_entrada(self):
        return self.entrada_texto.get("1.0", tk.END).rstrip("\n")
 
    def cifrar(self):
        texto = self._obtener_texto_entrada()
        if not texto:
            messagebox.showwarning("error", "Por favor ingresa un texto para cifrar.")
            return
        desplazamiento = self.var_desplazamiento.get()
        resultado = cifrar_cesar(texto, desplazamiento, descifrar=False)
        self._mostrar_resultado(resultado)
 
    def descifrar(self):
        texto = self._obtener_texto_entrada()
        if not texto:
            messagebox.showwarning("error", "Por favor ingresa un texto para descifrar.")
            return
        desplazamiento = self.var_desplazamiento.get()
        resultado = cifrar_cesar(texto, desplazamiento, descifrar=True)
        self._mostrar_resultado(resultado)
 
    def _mostrar_resultado(self, resultado):
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert("1.0", resultado)
 
    def limpiar(self):
        self.entrada_texto.delete("1.0", tk.END)
        self.salida_texto.delete("1.0", tk.END)
 
    def copiar(self):
        resultado = self.salida_texto.get("1.0", tk.END).rstrip("\n")
        if resultado:
            self.root.clipboard_clear()
            self.root.clipboard_append(resultado)
            messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")
        else:
            messagebox.showwarning("Aviso", "No hay resultado para copiar.")
 
 
if __name__ == "__main__":
    root = tk.Tk()
    app = AppCifradoCesar(root)
    root.mainloop()