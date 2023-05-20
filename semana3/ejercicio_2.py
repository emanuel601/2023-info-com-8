## Escribe un programa que pida al usuario un número y calcule la suma de todos
## los números naturales del 1 hasta ese número.

numeros = int(input("ingrese un número entero positivo: \n"))

suma = 0

for numero in range(1,numeros+1):
    suma = suma + numero

print(f"El resultado de la suma es: {suma}")