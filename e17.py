#e17.py) importar en python una imagen y almacenarla en una matriz. Implementar una funcion para rotar la imagen. Preguntar al
#usuario si quiere rotar 90 grados a la izquierda o a la derecha, o 180 grados. mostrar la imagen original y la rotada.no usar funciones ya establecidas
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rotar_imagen_manual(matriz, opcion):
#dimensiones de la imagen   
    dimensiones = matriz.shape
    filas = dimensiones[0]
    columnas = dimensiones[1]
    
    # Comprobamos si la imagen tiene canales de color (RGB) o es en escala de grises
    tiene_color = len(dimensiones) == 3
    
    if opcion == "derecha":
        # 90° a la derecha: las filas pasan a ser columnas y se invierte el orden
        if tiene_color:
            nueva_matriz = np.zeros((columnas, filas, dimensiones[2]), dtype=matriz.dtype)
        else:
            nueva_matriz = np.zeros((columnas, filas), dtype=matriz.dtype)
            
        for i in range(filas):
            for j in range(columnas):
                nueva_matriz[j][filas - 1 - i] = matriz[i][j]

    elif opcion == "izquierda":
        # 90° a la izquierda: las filas pasan a ser columnas, pero se invierte la otra coordenada
        if tiene_color:
            nueva_matriz = np.zeros((columnas, filas, dimensiones[2]), dtype=matriz.dtype)
        else:
            nueva_matriz = np.zeros((columnas, filas), dtype=matriz.dtype)
            
        for i in range(filas):
            for j in range(columnas):
                nueva_matriz[columnas - 1 - j][i] = matriz[i][j]

    elif opcion == "180":
        # 180°: Las dimensiones no cambian, pero se invierten tanto filas como columnas
        if tiene_color:
            nueva_matriz = np.zeros((filas, columnas, dimensiones[2]), dtype=matriz.dtype)
        else:
            nueva_matriz = np.zeros((filas, columnas), dtype=matriz.dtype)
            
        for i in range(filas):
            for j in range(columnas):
                nueva_matriz[filas - 1 - i][columnas - 1 - j] = matriz[i][j]
    else:
        print("Opción no válida.")
        return matriz

    return nueva_matriz

def principal():
 #cargamos la imagen   
    ruta_imagen = 'furbo.jpg' 
    try:
        imagen_original = mpimg.imread(ruta_imagen)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen '{ruta_imagen}'.")
        return

    #ROTACION DE LA IMAGEN
    print("¿Cómo deseas rotar la imagen?")
    print(" - 'derecha' (90 grados a la derecha)")
    print(" - 'izquierda' (90 grados a la izquierda)")
    print(" - '180' (180 grados)")
    opcion = input("Escribe tu opción: ").strip().lower()

    # 3. Aplicar la rotación
    print("Procesando imagen (esto puede tardar unos segundos dependiendo del tamaño)...")
    imagen_rotada = rotar_imagen_manual(imagen_original, opcion)

    # 4. Mostrar los resultados
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    ax[0].imshow(imagen_original)
    ax[0].set_title("Imagen Original")
    ax[0].axis('off')
    
    ax[1].imshow(imagen_rotada)
    ax[1].set_title(f"Imagen Rotada ({opcion})")
    ax[1].axis('off')
    
    plt.show()

# Ejecutar el programa
if __name__ == "__main__":
    principal()