## Escribe un programa que pida al usuario una cadena de texto y luego imprima
## la misma cadena pero con todas las vocales en mayúscula.

cadena = input("ingrese una cadena de texto: \n")

for letra in cadena:
    if letra in ("a","e","i","o","u"):
        cadena = cadena.replace(letra, letra.upper())


print(cadena)