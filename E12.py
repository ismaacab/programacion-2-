#implementar en python una función para aplicar cifrado cesar a una cadena se debe pasar el mensaje y el desplazamiento como parametros.
#La misma funcion debe decifrar el mensaje si se aplica un desplazamiento negativo.
def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""

    for char in mensaje:
        if char.isalpha():  # Verifica si el carácter es una letra
            ascii_offset = 65 if char.isupper() else 97
            nuevo_char = chr((ord(char) - ascii_offset + desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
            
        elif char.isdigit():  # Verifica si el carácter es un dígito
            nuevo_num = (int(char) + desplazamiento) % 10
            resultado += str(nuevo_num)
            
        else:  # Si no es letra ni número, se agrega sin cambios
            resultado += char

    return resultado

# ----------------------------
# Ingresa tus datos aqui
# ----------------------------
mensaje     = input("Ingresa el mensaje: ")
desplazamiento = int(input("Ingresa el desplazamiento (negativo para descifrar): "))
# ----------------------------

resultado = cifrado_cesar(mensaje, desplazamiento)
print(f"\nResultado: {resultado}")

