#un cajero automatico solo entrega billetes de 1000 y 200. ingresar la cantidad que desea extraer el usuario y luego indicar cuantos billetes de 1000 y 200 se entregan.indicar el saldo que no se pudo extraer

saldo= int(input("cantidad a extraer: "))
b1000= saldo//1000
b200= (saldo%1000)//200
inextraible= (saldo%1000)%200
print("billetes de 1000: ", b1000, ". billetes de 200: ", b200, ". saldo inextraible: ", inextraible)
