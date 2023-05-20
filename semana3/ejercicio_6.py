## Escribe un programa que pida al usuario una palabra y luego imprima la misma
## palabra pero con las letras en orden inverso.

palabra = input("ingrese una palabra: \n")

palabra_revertida = ''

for letra in palabra[::-1]:
    palabra_revertida += letra

print(palabra_revertida)