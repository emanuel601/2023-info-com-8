numero1, numero2 = input("ingrese 2 números: \n").split()

numero1 = float(numero1)
numero2 = float(numero2)

if numero1 > numero2:
    print(f"{numero1} es mayor a {numero2}")
elif numero1 < numero2:
    print(f"{numero2} es mayor {numero1}")
else:
    print("los números son iguales")