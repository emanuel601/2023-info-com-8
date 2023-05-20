## Escribe un programa que pida al usuario un número y luego imprima un
## triángulo de asteriscos con esa cantidad de filas.
## *
## **
## ***
## ****
## *****

lado = int(input("ingrese un número entero positivo: \n"))

longitud = ''

for numero in range(1, lado+1):
    longitud += '*' 
    print(longitud)