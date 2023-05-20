
##################### Datos programa #######################
condiciones = {'año': 2000, 'metros': 60, 'habitaciones': 2, 'garaje': [True, False], 'zona': ['A','B','C'],
                'estado': ['Disponible', 'Reservado', 'Vendido']}
lista_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


################################### funciones ########################################

def seleccionar_inmueble(accion, lista=lista_inmuebles):    # Selecciona inmuebles para editar o eliminar.
    cargador = True                                         # Devuelve una tupla con una inmueble y la posición
                                                            # de este en la lista: (inmueble, posición)
                                                            # En caso de cancelar la selección, devuelve una tupla
                                                            # con las cadenas ("Empty","Empty") 
    while cargador:
        seleccion = input(f"introduzca el número del inmueble que desea {accion}, '0' para cancelar: \n")
        if seleccion.isalpha():
            print(f"ingrese un valor apropiado")
        elif int(seleccion) == 0:
            print(f"Perfecto, no va a {accion} ninguna propiedad")
            cargador = False
            return 'Empty', 'Empty'
        elif int(seleccion) in range(1, len(lista)+1):
            cargador = False
            return lista_inmuebles[int(seleccion)-1], int(seleccion)-1
        else:
            print(f"ingrese un valor apropiado")



def mostrar():                                       # Función mostrar inmuebles
    contador = 0
    print("inmuebles:\n")
    for inmueble in lista_inmuebles:
        contador += 1
        print(f"{contador}. {inmueble}")
    print('\n')

def agregar(campos):                                  # Función para agregar inmuebles
    inmueble = {}
    for key, value in campos.items():
        cargador = True
        while cargador == True:
            if isinstance(value, int):
                valor = input(f"ingrese el valor de {key} ({key} debe ser mayor o igual a {value}): ")
                if valor.isnumeric():
                    valor = int(valor)
                    if valor >= value:
                        inmueble[key] = valor
                        cargador = False
                else:
                    print(f"ingrese un valor apropiado para {key}")
            else:
                contador = 0
                seleccionador = {}
                print(f"Por favor seleccione un valor para {key}")
                for item in value:
                    contador += 1
                    print(f"{contador}. {item}")
                    seleccionador[contador] = item
                valor = input(f"ingrese su selección: ")
                if valor.isalpha():
                    print(f"ingrese un valor apropiado para {key} \n")
                elif valor == '':
                    print(f"ingrese un valor apropiado para {key} \n")
                elif int(valor) in range(1, contador+1):
                    inmueble[key] = seleccionador[int(valor)]
                    cargador = False
                else:
                    print(f"ingrese un valor apropiado para {key} \n")
    lista_inmuebles.append(inmueble)
    print(inmueble)

def editar(campos = condiciones):        # Función para editar inmuebles
    mostrar()
    actividad = 'editar'
    inmueble = seleccionar_inmueble(accion=actividad)
    if isinstance(inmueble[1], int):  # funciona con valores enteros, si inmueble[1] toma valor "Empty" significa
                                      # que al selecionar tomaron la opción "cancelar" y por tanto no se realizará
                                      # la edición.
        for key, value in inmueble[0].items():
            cargador = True
            while cargador == True:
                print(f"{key}: {value}")
                if isinstance(campos[key], int):
                    cambio = input(f"Si no desea editar el valor de {key}, presione 'ENTER'"
                                f"\nSi lo modifica, deberá ingresar un número mayor o igual a {campos[key]}: ")
                    if cambio == '':
                        print(f"no se registraron cambios en el atributo {key} \n")
                        cargador = False
                    elif cambio.isnumeric():
                        if int(cambio) >= campos[key]:
                            inmueble[0][key] = int(cambio)
                            print('cambios regristrados')
                            cargador = False
                        else:
                            print(f'valores no registrados por estar fuera de rango, vuelva a ingresar {key} \n')
                    else:
                        print(f"valor inválido, vuelva a ingresar {key} \n")
                else:
                    contador = 0
                    seleccionador = {}
                    #print(f"Por favor seleccione un valor para {key}")
                    
                    print(f"Si no desea editar el valor de {key}, presione 'ENTER'"
                                  f"\nSi lo modifica, deberá selecionar alguna de las opciones")
                    for item in campos[key]:
                        contador += 1
                        print(f"{contador}. {item}")
                        seleccionador[contador] = item
                    valor = input()
                    if valor == '':
                        print(f"no se registraron cambios en el atributo {key} \n")
                        cargador = False
                    elif valor.isalpha():
                            print(f"ingrese un valor apropiado para {key} \n")
                    elif int(valor) in range(1, contador+1):
                        inmueble[0][key] = seleccionador[int(valor)]
                        cargador = False
                        print('cambios regristrados \n')
                    else:
                        print(f"ingrese un valor apropiado para {key} \n")

            


def eliminar(lista = lista_inmuebles):      # Función para eliminar inmuebles
    mostrar()
    actividad = 'eliminar'
    inmueble = seleccionar_inmueble(accion=actividad)

    if isinstance(inmueble[1], int): # funciona con valores enteros, si inmueble[1] toma valor "Empty" significa
                                     # que al selecionar, tomaron la opción "cancelar" y por tanto no se realizará
                                     # la operación eliminar.

        eliminado = lista_inmuebles.pop(inmueble[1])
        print(f"ha eliminado el inmueble {eliminado}")
    

def agregar_eliminar_editar(campos=condiciones, lista=lista_inmuebles):    # Funcion madre de agregar, eliminar o modificar los valores de una propiedad
    if len(lista) == 0:                                                    # si no hay valores previos, manda directamente a agregar
        agregar(campos)
    else:
    
        mostrar()
        accion = input("Seleccione su acción:\n"
              " 1. Agregar inmueble \n 2. Editar inmueble  \n 3. Eliminar inmueble \n") # consulta que hacer
        if accion.isalpha():
            print("selección incorrecta")
        elif int(accion) ==1:
            agregar(campos)
        elif int(accion) ==3:
            eliminar()
        elif int(accion) ==2:
            editar()

def cambiar_estado(campos=condiciones):
    mostrar()
    actividad = "cambiar estado"
    inmueble = seleccionar_inmueble(accion=actividad)
    print(inmueble[0])
    cargador = True
    key = 'estado'
    while cargador:
            contador = 0
            seleccionador = {}
            print(f"Si no desea editar el valor {inmueble[0]['estado']}, presione 'ENTER'"
            f"\nSi lo modifica, deberá selecionar alguna de las opciones: ")
                    
            for item in campos[key]:
                        contador += 1
                        print(f"{contador}. {item}")
                        seleccionador[contador] = item
            valor = input()
            if valor == '':
                    print(f"no se registraron cambios en el atributo {key} \n")
                    cargador = False
            elif valor.isalpha():
                    print(f"ingrese un valor apropiado para {key} \n")
            elif int(valor) in range(1, contador+1):
                inmueble[0][key] = seleccionador[int(valor)]
                cargador = False
                print(inmueble[0])
                print('cambios regristrados \n')
            else:
                    print(f"ingrese un valor apropiado para {key} \n")

def presupuesto(monto, lista= lista_inmuebles):
    alcanza_para = []
    inmueble_con_precio = {}
    for inmueble in lista:
        if inmueble['zona'] == 'A':
            #print('entro')
            precio = ((inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 
                      + inmueble['garaje'] * 1500) * (1 - (2023 - inmueble['año']) / 100)) 
            #print(precio)
        elif inmueble['zona'] == 'B':
            precio = ((inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 
                      + inmueble['garaje'] * 1500) * (1 - (2023 - inmueble['año']) / 100)) * 1.5
        else:
            precio = ((inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 
                      + inmueble['garaje'] * 1500) * (1 - (2023 - inmueble['año']) / 100)) * 2
        
        if (inmueble['estado'] == 'Reservado' or inmueble['estado'] == 'Disponible') and precio <= monto:
            #print('entro')
            inmueble_con_precio = {}
            for key, value in inmueble.items():
                inmueble_con_precio[key] = inmueble[key]
            inmueble_con_precio['precio'] = precio
            alcanza_para.append(inmueble_con_precio)
    return alcanza_para



##################### Programa #####################################

continuar = True
while continuar:                                 # Bucle principal del programa
    operacion = True

    while operacion:                             # Bucle de consulta sobre operacion a realizar
        print(f"Bienvenidos al sismtema de Gestion Inmobinfo \n"
              f"Propiedades Disponibles:")
        mostrar()
        pregunta_operacion = input("Seleccione su operación deseada: \n"
                                   "\n a) Agregar, editar y eliminar inmuebles a la lista"
                                   "\n b) Cambiar el estado de un inmueble, sin modificar sus demás datos."
                                   "\n c) Hacer búsqueda de inmuebles en función de un presupuesto dado."
                                   "\n d) Para Salir \n")
        if pregunta_operacion == "a":
            operacion = False
            agregar_eliminar_editar()
        elif pregunta_operacion == "b":
            operacion = False
            cambiar_estado()
            if len(lista_inmuebles) == 0:
                print("la lista está vacía")
        elif pregunta_operacion == "c":
            if len(lista_inmuebles) == 0:
                print("la lista está vacía")
            else:
                
                bucleador = True
                while bucleador:
                    valor = input('ingrese un monto para el presupuesto: ')
                    if valor == '':
                        print("valor inválido")
                    elif valor.isalpha():
                        print("valor inválido")
                    else:
                        print("\n los inmuebles disponibles por ese monto son: \n")
                        for inmueble in presupuesto(int(valor)):
                            print(inmueble)
                        bucleador = False
            operacion = False
            
                
        elif pregunta_operacion == "d":
            break
        else:
            print("no ingresó una opción válida")
    
    pregunta_final = input('Si desea finalizar ingrese "y", si desea realizar otra operación ingrese cualquier caracter: \n')
    if pregunta_final == 'y':
        continuar = False
