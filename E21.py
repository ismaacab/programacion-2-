#E21.py)Hacer un conversor de unidades con TKINTER usar un optionMenu para elegir la categoria y un Combo Box para elegir para elegir la conversion. hcaer el .exe.
#A)Loongitud: M a KM; M a millas; CM a pulgadas; M a pies B)Temperatura: Celcius a Fahrenheit; Celsius a Kelvin; Fahrenheit a Kelvin.
#C)Masa: KG a LB; Gramos a onzas; Tn a Kg D)Velocidad: Km/h a Mph; Km/h a m/s; km/h a nudos. E) Volumen: Litros a galones; Litros a pies cubicos
#F)Monedas: Pesos a Dolares;pesos a reales, pesos a Euros. G)Informatica B- KB- MB- GB
import tkinter as tk
from tkinter import ttk, messagebox

# --- Funciones de Conversión ---
def actualizar_conversiones(*args):
    categoria = categoria_var.get()
    opciones = list(CONVERSIONES.get(categoria, {}).keys())
    combo_conversion['values'] = opciones
    if opciones:
        combo_conversion.set(opciones[0])

def convertir():
    try:
        valor = float(entry_valor.get())
        categoria = categoria_var.get()
        conversion = combo_conversion.get()
        
        formula = CONVERSIONES[categoria][conversion]
        resultado = formula(valor)
        
        lbl_resultado.config(text=f"Resultado: {resultado:.4f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")
    except KeyError:
        messagebox.showerror("Error", "Selección de conversión no válida.")

# --- Diccionario de Fórmulas ---
CONVERSIONES = {
    "Longitud": {
        "M a KM": lambda x: x / 1000,
        "M a Millas": lambda x: x * 0.000621371,
        "CM a Pulgadas": lambda x: x * 0.393701,
        "M a Pies": lambda x: x * 3.28084
    },
    "Temperatura": {
        "Celsius a Fahrenheit": lambda x: (x * 9/5) + 32,
        "Celsius a Kelvin": lambda x: x + 273.15,
        "Fahrenheit a Kelvin": lambda x: (x - 32) * 5/9 + 273.15
    },
    "Masa": {
        "KG a LB": lambda x: x * 2.20462,
        "Gramos a Onzas": lambda x: x * 0.035274,
        "Tn a KG": lambda x: x * 1000
    },
    "Velocidad": {
        "Km/h a Mph": lambda x: x * 0.621371,
        "Km/h a m/s": lambda x: x / 3.6,
        "Km/h a Nudos": lambda x: x * 0.539957
    },
    "Volumen": {
        "Litros a Galones": lambda x: x * 0.264172,
        "Litros a Pies Cúbicos": lambda x: x * 0.0353147
    },
    "Monedas": {
        "Pesos a Dólares": lambda x: x / 1000,   # Tasas de cambio fijas de ejemplo
        "Pesos a Reales": lambda x: x / 180,
        "Pesos a Euros": lambda x: x / 1100
    },
    "Informática": {
        "B a KB": lambda x: x / 1024,
        "KB a MB": lambda x: x / 1024,
        "MB a GB": lambda x: x / 1024
    }
}

# --- Interfaz Gráfica ---
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("380x300")
root.resizable(False, False)

# Entrada de valor
tk.Label(root, text="Valor a convertir:").pack(pady=5)
entry_valor = tk.Entry(root)
entry_valor.pack(pady=5)

# Opción de Categorías (OptionMenu)
tk.Label(root, text="Categoría:").pack(pady=5)
categorias = list(CONVERSIONES.keys())
categoria_var = tk.StringVar(root)
categoria_var.set(categorias[0])
categoria_var.trace_add("write", actualizar_conversiones)

option_menu = tk.OptionMenu(root, categoria_var, *categorias)
option_menu.pack(pady=5)

# Selección de Conversión (ComboBox)
tk.Label(root, text="Conversión:").pack(pady=5)
combo_conversion = ttk.Combobox(root, state="readonly")
combo_conversion.pack(pady=5)

# Botón Convertir
btn_convertir = tk.Button(root, text="Convertir", command=convertir)
btn_convertir.pack(pady=10)

# Etiqueta de Resultado
lbl_resultado = tk.Label(root, text="Resultado: -", font=("Arial", 11, "bold"))
lbl_resultado.pack(pady=5)

# Inicializar combo box con la primera categoría
actualizar_conversiones()

root.mainloop()