#escribir una función donde el usuario ingresa un numero entero positivo (validarlo)
#y calcular el factorial
def fac(num):
    a= 1
    for i in range(2, num+1):
        a= a * i
    return a

factorial= fac(int(input("num a factorizar: ")))
print("el factorial del numero es",factorial)
