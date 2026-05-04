# diseñar un programa que pida la fecha de nacimiento del usuario, e indique su edad en 2 formatos: cantidad  de días totales, y años-meses-dias. Mostrar en pantalla la fecha de nacimiento en formato Epoch/timestamp.
import  time
a= int(input("año de nacimiento: "))
m= int(input("mes de nacimiento: "))
d= int(input("día de nacimiento: "))
fecha= time.struct_time((a, m, d, 0, 0, 0, 0, 0, -1))
e_nac= time.mktime(fecha)
e_act = time.time()
seg = e_act - e_nac
dias=int(seg//86400)
res_a = dias // 365
res_m = (dias % 365) // 30
res_d = (dias % 365) % 30

print("Edad en días: ", dias)
print("Edad en A-M-D: ", res_a, "a, ", res_m, "m, ", res_d, "d.")
