# Escribir una función que calcule el area de un circulo, luego escribir una función que calcule el volumen de un cilindro llamando a la primera función. 
from math import pi

def area(radio):
    area= pi*(radio**2)
    return area

def vol(alto, radio):
    
    vol = area(radio) * alto
    return vol

r= int(input("radio: "))
h= int(input("alto: "))

print("area: ", area(r), "volumen: ", vol(h, r))
