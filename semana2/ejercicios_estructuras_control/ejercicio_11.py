numero1, numero2 = list(map(int,(input("ingrese 2 números múltiplos de 2: ").split())))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f"el resultado es: {numero1 + numero2}")
else:
    print("al menos uno de los números no es múltiplo de dos") 