## Escribe un programa que pida al usuario una cadena de texto y determine
## cuántas veces aparece cada letra en la cadena.

cadena = input("ingrese una cadena de texto: \n")

letras_escrutadas = []
repeticiones = {}

for letra in cadena:
    if (letra not in letras_escrutadas and letra.isalpha()):
        repeticiones[letra] = cadena.count(letra)
        letras_escrutadas.append(letra)

print(repeticiones)