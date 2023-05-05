### Programa Analizador de Texto

texto = input("ingresar un texto, un artículo o una frase. \n") 

tres_letras = input("ingrese 3 letras seguidas a su elección. \n")


if len(tres_letras) == 3 and tres_letras.isalpha():      # verifico que hayan ingresado 3 caracteres y que sean letras
    # pregunta 1
    texto = texto.lower()                                # convierto las cadenas a minúscula
    tres_letras = tres_letras.lower()

    contador_letra1 = texto.count(tres_letras[0])        # obtengo el número de veces que se repite cada letra
    contador_letra2 = texto.count(tres_letras[1])
    contador_letra3 = texto.count(tres_letras[2])

    print(f"la letra {tres_letras[0]} se repite {contador_letra1} veces, letra {tres_letras[1]} se repite {contador_letra2} y finalmente la letra {tres_letras[2]} se repite {contador_letra3}")

    # pregunta 2

    numero_de_palabras = len(texto.split())              # separo el texto en palabras y luego las cuento

    print(f"la cantidad de palabras es: {numero_de_palabras}")

    # pregunta 3

    primera_letra = texto[0]                             # obtengo primera y última letra mediante sus índices
    ultima_letra = texto[-1]

    print(f"la primera letra es {primera_letra} y la última es {ultima_letra}")

    # pregunta 4
    texto_revertido = texto.split()
    texto_revertido.reverse()
    texto_revertido = ' '.join(texto_revertido)   # separo el texto, lo invierto y lo vuelvo a unir

    print(f"{texto_revertido}")

    # pregunta 5

    if 'python' in texto:                             # verifico que la palabra "python" se halle en texto
        print('la palabra "python" se encuentra en el texto')
    else:
        print('la palabra "python" no se encuentra en el texto')
else:
    print("las tres letras fueron ingresadas incorrectamente")


