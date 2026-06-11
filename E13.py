#E13.py)implementar en python una funcion para aplicar cifrado cesar a una cadena. se debe pasar el mensaje y el desplazamiento como parametros.
#La misma funcion debe decifrar el mensaje si se aplica un desplazamiento negativo.
def cifrado_cesar(mensaje: str, desplazamiento: int) -> str:
    resultado = []

    for caracter in mensaje:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado.append(nuevo_caracter)
        else:
            resultado.append(caracter)

    return ''.join(resultado)


mensaje = input("Ingrese el mensaje: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
print(cifrado_cesar(mensaje, desplazamiento))