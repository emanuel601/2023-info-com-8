## Escribe un programa que imprima la suma de todos los números pares del 1 al
## 100.

suma = 0

for numero in range(1, 101):
    if numero % 2 == 0:
        
        suma += numero

print(f"la suma es: {suma}")