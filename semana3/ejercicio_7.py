## Escribe un programa que pida al usuario una palabra y determine si es un
## palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
## izquierda).

palabra = input("ingrese una palabra: \n")


if palabra == palabra[::-1]:
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} NO es un palíndromo")
