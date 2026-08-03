#E18.py)aplicar un filtro de desenfoque gaussiano a una imagen. Mostrar la imagen original y la filtrada. Hacer la convolución manual desde la
#celda (1,1) hasta la (n-1, n-1), Usar  el kernel
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def aplicar_gaussiano_manual(imagen):
    # Definimos el kernel Gaussiano 3x3
    kernel = np.array([
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ])
    
    # Comprobamos las dimensiones (soporte para RGB o escala de grises)
    if len(imagen.shape) == 3:
        filas, columnas, canales = imagen.shape
    else:
        filas, columnas = imagen.shape
        canales = 1
        # Reestructuramos temporalmente para facilitar el código
        imagen = imagen.reshape((filas, columnas, 1)) 
        
    # Creamos una matriz de ceros para almacenar el resultado.
    # Usamos float32 para evitar errores de redondeo al multiplicar fracciones.
    imagen_filtrada = np.zeros(imagen.shape, dtype=np.float32)
    
    # Convolución manual desde (1,1) hasta (n-1, n-1) para evitar salirnos de los bordes
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            for c in range(canales):
                # 1. Extraemos la "vecindad" 3x3 alrededor del píxel actual (i, j)
                region = imagen[i-1 : i+2, j-1 : j+2, c]
                
                # 2. Multiplicamos la región por el kernel (elemento a elemento) y sumamos todo
                # Nota: Una convolución matemática estricta rota el kernel 180°, 
                # pero como el kernel gaussiano es simétrico, no es necesario.
                nuevo_valor = np.sum(region * kernel)
                
                # 3. Asignamos el resultado al píxel central
                imagen_filtrada[i, j, c] = nuevo_valor
                
    # Restauramos la forma original si era en escala de grises
    if canales == 1:
        imagen_filtrada = imagen_filtrada.reshape((filas, columnas))
        
    # Aseguramos que los valores se mantengan en el rango válido [0, 1] o [0, 255]
    if imagen.dtype == np.uint8:
        imagen_filtrada = np.clip(imagen_filtrada, 0, 255).astype(np.uint8)
    else:
        imagen_filtrada = np.clip(imagen_filtrada, 0.0, 1.0)
        
    return imagen_filtrada

def principal():
    ruta_imagen = 'furbo.jpg' # Cambia esto por la ruta de tu imagen
    
    try:
        # Cargar imagen
        imagen_original = mpimg.imread(ruta_imagen)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen '{ruta_imagen}'.")
        return

    print("Aplicando filtro Gaussiano manual...")
    print("Esto tomará varios segundos dependiendo de la resolución de la imagen.")
    
    # Aplicar el filtro
    imagen_filtrada = aplicar_gaussiano_manual(imagen_original)

    # Mostrar las imágenes
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    ax[0].imshow(imagen_original, cmap='gray' if len(imagen_original.shape) == 2 else None)
    ax[0].set_title("Imagen Original")
    ax[0].axis('off')
    
    ax[1].imshow(imagen_filtrada, cmap='gray' if len(imagen_filtrada.shape) == 2 else None)
    ax[1].set_title("Filtro Gaussiano 3x3 (Convolución Manual)")
    ax[1].axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    principal()