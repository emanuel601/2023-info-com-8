## Escribe un programa que pida al usuario una lista de números separados por
## comas y calcule su promedio.



lista = list(input("ingrese una lista de números separados por coma, para calcular su promedio: \n").split(','))

suma = 0
count = 0

for numero in lista:
    count += 1
    suma += float(numero)

promedio = suma / count

print(f"el promedio es: {round(promedio, 2)}")