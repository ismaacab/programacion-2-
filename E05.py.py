#el profe tiene X cantidad de caramelos para repartir en Y cantidad de estudiantes.los estudiantes deben recibir un numero entero de caramelos. preguntar al usuario cuantos caramelos se reparten entre cuantos estudiantes y luego indicar cuantos caramelos le toca a cada uno y cuantos sobran en la bolsa

car= int(input("cantidad de caramelos: "))
est= int(input("cantidad de estudiantes: "))
div= car//est
res= car%est
print("se dan ", div, " caramelo(s) a cada estudiante y sobran ", res)
