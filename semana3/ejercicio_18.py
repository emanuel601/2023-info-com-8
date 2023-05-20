## Escribe un programa que pida al usuario un número y luego imprima un
## triángulo de números como el siguiente:
## 1
## 2 3
## 4 5 6
## 7 8 9 10

numero_final = int(input("ingrese un número entero positivo: \n"))

contador = 1


for numero in range(1,numero_final+1):
    linea = ''
    for i in range(contador, contador + numero):
        contador += 1
        linea += f"{i}" + ' '
    print(linea)
