numero = float(input('ingrese un numero decimal: '))

numero_str = str(numero)

entero = numero_str.split(".")[0]
decimal = numero_str.split(".")[1]

print(f'entero: {entero}, decimal: {decimal}')