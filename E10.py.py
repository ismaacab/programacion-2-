# escribir una función para conventir temperatura de celcius a Fahrenheit y otra función para la conversión opuesta
p= int (input("convertir \nFarenheit a celcius (1) \ncelcius a farenheit(2): "))

def f_a_c(f):
    cel=(f - 32) * 5/9
    return cel
def c_a_f(c):
    fa= (c* 9/5) + 32
    return fa
if p==1:
    f=int (input("ingrese la temperatura:  "))
    print(f_a_c(f))
else:
    c=int(input("ingrese la temperatura: "))
    print(c_a_f(c))

