## Escribe un programa que pida al usuario un número y calcule su factorial.
## Un factorial es el producto que resulta de multiplicar un número entero positivo
## dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
## de 4 es 4! = 4 × 3 × 2 × 1 = 24.


numero = int(input("ingrese un número entero positivo: \n"))

factorial = 1

for valor in range(1, numero+1):
    factorial *= valor

print(f"el factorial de {numero} es: {factorial}")