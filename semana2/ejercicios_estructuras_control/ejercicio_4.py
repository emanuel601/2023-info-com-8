nota = float(input("ingrese su calificación: \n"))

if nota >= 5 and nota >=0 and nota <= 10:
    print("Está aprobado")
elif nota > 0 and nota < 5:
    print("desaprobó")
else:
    print("ingrese un valor válido")
