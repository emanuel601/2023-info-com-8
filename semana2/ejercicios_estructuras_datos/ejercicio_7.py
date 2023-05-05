## Crear un diccionario con los nombres de tres ciudades y sus respectivas
## poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
## población. Mostrar el diccionario resultante.


ciudades = {'Resistencia': 200, 'Corrientes': 250, 'Posadas': 200}

ciudad, poblacion = input("ingrese el nombre de una ciudad seguida de su población: ").split()

ciudades[ciudad] = int(poblacion)

print(ciudades)