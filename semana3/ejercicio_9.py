## Escribe un programa que pida al usuario un número y luego imprima la
## secuencia de Fibonacci correspondiente a ese número.

numero = int(input("ingrese un número entero positivo: \n"))

secuencia = []
suma = 0

for i in range(numero+1):
    if i <= 1:
        suma += i
    else:
        suma = secuencia[i-1] + secuencia[i-2] 

    secuencia.append(suma)

print(f"la secuencia es: {secuencia}")
    


