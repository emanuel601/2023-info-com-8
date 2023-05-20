## Escribe un programa que pida al usuario una cadena de texto y luego imprima
## la misma cadena pero con cada palabra al revés

cadena = input("ingrese una cadena de texto: \n")

palabras_sueltas = list(cadena.split())

cadena_reversa = ''

for palabra in palabras_sueltas:
    cadena_reversa += palabra[::-1] + ' '

print(cadena_reversa)