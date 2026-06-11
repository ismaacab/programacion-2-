#e15.py)importar en python una imagen en escala de grises y almacenarla en una matriz. Mostrar la imagen en pantalla
#luego ordenar los valores numericos para voltear la imagen horizontalmente y mostrar el resultado en pantalla.
# e15.py - Imagen en escala de grises → matriz → voltear horizontalmente

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ── 1. Cargar imagen y convertir a escala de grises ──────────────────────────
ruta = input("Ingresá la ruta de la imagen (ej: foto.jpg): ").strip()

img_pil   = Image.open(ruta).convert("L")   # "L" = escala de grises
matriz    = np.array(img_pil)               # almacena en matriz numpy (filas x cols)

print(f"\nMatriz cargada: {matriz.shape[0]} filas x {matriz.shape[1]} columnas")
print("Primeras 3 filas de la matriz:")
print(matriz[:3])

# ── 2. Voltear horizontalmente (espejo izquierda ↔ derecha) ──────────────────
#   Cada fila se invierte: fila[j] → fila[n-1-j]
#   Con numpy: [:, ::-1]  /  también se puede usar np.fliplr()
matriz_volteada = matriz[:, ::-1]

# ── 3. Mostrar ambas imágenes ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(matriz,          cmap="gray", vmin=0, vmax=255)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(matriz_volteada, cmap="gray", vmin=0, vmax=255)
axes[1].set_title("Volteada horizontalmente")
axes[1].axis("off")

plt.tight_layout()
plt.show()