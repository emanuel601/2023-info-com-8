## Escribe un programa que pida al usuario un número y luego imprima si ese
## número es un número perfecto o no. Un número perfecto es aquel que es igual a
## la suma de sus divisores propios (excluyendo el propio número).
## Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
## puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

numero_a_testear = int(input("ingrese un número entero positivo: \n"))

divisores = []

for numero in range(1, numero_a_testear):
    if numero_a_testear % numero == 0:
        divisores.append(numero)

if sum(divisores) == numero_a_testear:
    print(f'el número {numero_a_testear} es un número perfecto y sus divisores son: {divisores}')
else:
    print(f'el número {numero_a_testear} NO es un número perfecto')