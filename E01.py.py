# utilizar la funcion input() y print() para preguntar el nombre de usuario. Saludar y preguntar su año de nacimiento. Calcular su edad
from datetime import datetime
nom= input("Nombre de usuario: ")
print("Hola, ", nom, ". Cuál es su año de nacimiento?")
nac= int(input())
ed= datetime.today().year - nac
print("Tienes o tendrías ", ed, " años :)")
