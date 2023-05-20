## Escribe un programa que pida al usuario un número y luego imprima un
## triángulo de números como el siguiente:
## 1
## 2 2
## 3 3 3
## 4 4 4 4
## 5 5 5 5 5

numero_final = int(input("ingrese un número entero positivo: \n"))



for numero in range(1,numero_final+1):
    print(numero * f'{numero} ')
