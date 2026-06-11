#e14.py)declarar una matriz de 4 filas y 4 columnas con numeros sucesivos a partir del 1 en cada celda,
#calcula la suma y la mltiplicacion de la contra diagonal.Mostrar en pantalla estos valores y los elementos.
M = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9,  10, 11, 12],
     [13, 14, 15, 16]]

print("--- Matriz ---")
for fila in M:
    print(fila)

suma = 0
multi = 1
contra_diagonal = []

n = len(M)  # 4

for i in range(n):
    j = (n - 1) - i          # contra diagonal: (0,3) (1,2) (2,1) (3,0)
    elemento = M[i][j]
    contra_diagonal.append(elemento)
    suma  += elemento
    multi *= elemento

print("\n--- Contra Diagonal ---")
print(f"Elementos:      {contra_diagonal}")
print(f"Suma:           {suma}")
print(f"Multiplicación: {multi}")