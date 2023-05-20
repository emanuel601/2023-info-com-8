from random import randint

## Juego adivinar número entre 1 y 100

nombre_jugador = input('Hola como es tu nombre? \n')  # pedimos al jugador que ingrese su nombre

while not nombre_jugador.isalpha():                   # introducimos un while para tener un mínimo de validación en el nombre
    nombre_jugador = input('Por favor ingresá un nombre con caracteres alfabeticos \n')
else:
    print(f"Hola {nombre_jugador}! Podras adivinar el numero sorpresa del 1 al 100? tenes 8 intentos!")

    numero_ganador = randint(1,100)                   # calculo el número ganador
    # print(numero_ganador)

    ganador = False                                   # Introduzco esta variable, en caso de que el juego termine sin Ganador
    contador_intentos = 1                             # Inicializo el contador en 1
    while contador_intentos <= 8:
        intento = input(f"ingresá un número entero entre 1 y 100 (te quedan {8 - contador_intentos + 1}) intentos \n")
        if not intento.isdigit():                     # Implemento validación del número propuesto por el jugador
            print('el valor ingresado no es un número entero')
        elif int(intento) < 0 and int(intento) > 100:
            print('el valor ingresado no se encuentra entre 0 y 100')
        else:                                         # Si el numero propuesto es validado, aumento el contador en +1
            contador_intentos += 1

            numero_intento = int(intento)
            if numero_intento == numero_ganador:      # Si el numero propuesto es ganador, aumento el contador para terminar el while
                contador_intentos = 9
                ganador = True                        # cambio de estado el booleano, para en al final evitar el mensaje de derrota
                print(f'felicitaciones el número {numero_ganador} es el ganador!!')
            elif numero_ganador > numero_intento:     # establezco los mensajes para los números propuestos bajos o altos
                print(f'el numero {numero_intento} es muy bajo')
            else:
                print(f'el numero {numero_intento} es muy alto')

if not ganador:                                       # si el booleano no cambió de estado y se acabaron los intentos, muestra el número ganador
    print(f'perdiste! el número ganador era {numero_ganador}')