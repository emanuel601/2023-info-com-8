caracter = input("ingrese un caracter: \n")

if caracter.isnumeric():
    print("Es un número")
elif caracter.isupper():
    print("es una letra mayúscula")
elif caracter.islower():
    print("es una letra minúscula")
elif caracter.isascii():
    print("Es un caracter especial")
else:
    print("no es ni una: letra mayúscula, minúscula, caracter especial o número")