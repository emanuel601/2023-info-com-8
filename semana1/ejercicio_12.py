fecha_de_nacimiento = input('ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
edad = 2023 - int(fecha_de_nacimiento.split("/")[2])
print(f'su edad es: {edad} años')