# Importar en python una imagen a color y mostrarla. Definir una funcion para convertir imagenes en escala de grises
# y mostrar el resultado. No usar funciones integradas, en su lugar usar la formula .convert('L') para pasarlo a grises
# # grises= R*0.2989 + G*0.5870 + B*0.1140


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# 1) Crear una imagen fácil (franjas de colores) y guardarla
# ---------------------------------------------------------
alto, ancho = 200, 200
imagen_facil = np.zeros((alto, ancho, 3), dtype=np.uint8)

imagen_facil[:, 0:ancho//3]          = [255, 0, 0]   # franja roja
imagen_facil[:, ancho//3:2*ancho//3] = [0, 255, 0]   # franja verde
imagen_facil[:, 2*ancho//3:ancho]    = [0, 0, 255]   # franja azul

Image.fromarray(imagen_facil).save('floramarilla.jpg')

# ---------------------------------------------------------
# 2) Importar la imagen a color y mostrarla
# ---------------------------------------------------------
foto = Image.open('floramarilla.jpg')
foto = np.array(foto)
dimen = np.shape(foto)
print("Dimensiones de la imagen:", dimen)

plt.imshow(foto)
plt.title("Imagen original a color")
plt.axis('off')
plt.show()

# ---------------------------------------------------------
# 3) Función para convertir a escala de grises (sin funciones integradas)
#    grises = R*0.2989(74,72) + G*0.5870(5,8) + B*0.1140(2,2)
# ---------------------------------------------------------
def convertir(image_input):
    alto = image_input.shape[0]
    ancho = image_input.shape[1]
    grises = np.zeros((alto, ancho), dtype=np.uint8)

    for i in range(alto):
        for j in range(ancho):
            R = image_input[i, j, 0]
            G = image_input[i, j, 1]
            B = image_input[i, j, 2]

            val = int(R * 0.2989 + G * 0.5870 + B * 0.1140)
            grises[i, j] = max(0, min(255, val))

    return grises

# ---------------------------------------------------------
# 4) Aplicar la conversión y mostrar el resultado
# ---------------------------------------------------------
gris_converted = convertir(foto)

plt.imshow(gris_converted, cmap='gray')
plt.title("Imagen convertida a escala de grises")
plt.axis('off')
plt.show()