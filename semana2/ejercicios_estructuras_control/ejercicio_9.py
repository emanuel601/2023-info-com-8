numeros = list(map(int,(input("ingrese 3 enteros: ").split())))

if numeros[0] >= numeros[1] and numeros[0] >= numeros[2]:
    print(f"el número {numeros[0]} es el mayor")
elif numeros[1] >= numeros[0] and numeros[1] >= numeros[2]:
    print(f"el número {numeros[1]} es el mayor")
else:
    print(f"el número {numeros[2]} es el mayor")