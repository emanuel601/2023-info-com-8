# Desafio 8 - Tecnopower
# Integrantes:
# Godoy, Diego Gabriel 
# Ortiz Kovalek, Emanuel 
# Baibiene, Facundo
# Alarcón, Julieta Guadalupe 
# Agudo, Néstor Adrian
# Bernardis, Mariela Iris
# Sagania, Facundo
# Maidana, Emiliano
# Roldán, Ignacio
# Nasir, Yamil Alí

import datetime 
dictusuarios = {}
dictnombre = {}
dictarticulos = {}
dictcomentarios = {}

#clase Articulo
# id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
class Articulo:
	def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
		self.id = id
		self.id_usuario = id_usuario
		self.titulo = titulo
		self.resumen = resumen
		self.contenido = contenido
		self.fecha_publicacion = fecha_publicacion
		self.imagen = imagen
		self.estado = estado

#clase Comentario
# id, id_articulo, id_usuario, contenido, fecha_hora, estado
class Comentario:
	def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
		self.id = id
		self.id_articulo = id_articulo
		self.id_usuario = id_usuario
		self.contenido = contenido
		self.fecha_hora = fecha_hora
		self.estado = estado


#Clase Usuario
#atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
#métodos: login(), registrar()
class Usuario:
	def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
		self.id = id
		self.nombre = nombre.title() # Para que la primer letra del nombre esté siempre en mayúscula
		self.apellido = apellido.title()
		self.telefono = telefono
		self.username = username
		self.email = email
		self.contraseña = contraseña
		self.fecha_registro = fecha_registro
		self.avatar = avatar
		self.estado = estado
		self.online = online

	def login(self): # Lógica para realizar el inicio de sesión
		global dictusuarios
		dictusuarios[self.username].online = True	# El usuario está en linea

	def logout(self):
		global dictusuarios
		dictusuarios[self.username].online = False

	def registrar(self): # Lógica para realizar el registro
		global dictusuarios
		dictusuarios[self.username] = self	# Almacenar al usuario en el dict
		dictnombre[self.id] = f"{self.nombre} {self.apellido}"
		
	def comentar(self,id_art): # Lógica para realizar un comentario
		return Comentario(
			id=1+len(dictcomentarios), 
			id_articulo=id_art, 
			id_usuario=self.id,
			contenido=input("Ingrese contenido: "), 
			fecha_hora=datetime.datetime.now(), 
			estado=input("Ingrese estado: "))
		
	

#Clase Publico(Usuario)
#atributo: es_publico
#métodos: registrar(), comentar()
class Publico(Usuario):
	def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
		super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
		self.es_publico = True


#clase Colaborador(Usuario)
#atributos: es_colaborador
#métodos: registrar(), comentar(), publicar()
class Colaborador(Usuario):
	def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
		super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
		self.es_colaborador = True

	def publicar(self): # Lógica para publicar un artículo
		return Articulo(
			id=1+len(dictarticulos),
			id_usuario=self.id,
			titulo=input("Ingrese titulo: "),
			resumen=input("Ingrese resumen: "),
			contenido=input("Ingrese contenido: "),
			fecha_publicacion=datetime.date.today(),
			imagen=input("Ingrese imagen: "),
			estado=input("Ingrese estado: "))



# Código para los diálogos de interacción con el usuario
def menu_inicio():
	while True:
		print("¿Qué desea hacer?")
		print("0. Salir")
		print("1. Registrarse")
		print("2. Iniciar sesión")
		opcion = input("> ")
		if opcion == '0':
			print("Adios!")
			exit()

		elif opcion == '1':
			registrar_usuario()

		elif opcion == '2':
			tmp = login_usuario()
			if(tmp != None): 
				menu_usuario(tmp)

		else:
			print("Opción no válida.")

def menu_usuario(usuario):
	global dictarticulos
	colaborador = isinstance(usuario, Colaborador)
	print(f"Bienvenido, {usuario.nombre}!")
	while True:
		print("¿Qué desea hacer?")
		print("0. Cerrar sesión")
		print("1. Ver artículos")
		if colaborador: 
			print("2. Crear artículo")
		opcion = input("> ")
		if(opcion == '0'):
			usuario.logout()
			return
		elif(opcion == '1'):
			menu_select_articulos(usuario)
		elif(colaborador and opcion == '2'): # lógica para el colaborador
			new_article = usuario.publicar()
			dictarticulos[new_article.id] = new_article
		else:
			print("Elija una opción valida.")

def menu_select_articulos(usuario):
	if len(dictarticulos) == 0:
		print("No hay artículos :(")
		return

	for id in dictarticulos: # Por cada artículo en el diccionario mostrar una versión breve.
		titulo = dictarticulos[id].titulo
		autor = dictnombre[dictarticulos[id].id_usuario]
		resumen = dictarticulos[id].resumen
		print(f'{id}: {titulo} (por {autor})')
		print(f'\t- {resumen}')

	articuloID = input("Seleccione un artículo (segun ID): ")
	
	if(articuloID.isnumeric() and dictarticulos.get(int(articuloID)) != None): # Si la entrada es valida y el artículo existe
		menu_articulo(int(articuloID), usuario)	# Abrir el artículo específico.
	else:
		print("Artículo invalido.")

def menu_articulo(artID, usuario):
	# Leer datos importantes del artículo
	titulo = dictarticulos[artID].titulo
	autor = dictnombre[dictarticulos[artID].id_usuario]
	fecha = dictarticulos[artID].fecha_publicacion
	contenido = dictarticulos[artID].contenido
	imagen = dictarticulos[artID].imagen
# Escribir el artículo de forma detallada.
	print(f"\n'{titulo}'")
	print(f"por {autor}")
	print(str(fecha))
	print("-----------------------------")
	print(contenido)
	print(f"Imágen: {imagen}")
	print("-----------------------------\n")

	while True:
		print("¿Qué desea hacer?")
		print("0. Salir")
		print("1. Listar comentarios")
		print("2. Hacer un comentario")
		opcion = input("> ")
		if(opcion == '0'):
			return
		elif(opcion == '1'):
			mostrar_comentarios(artID) # lógica para ver comentarios
		elif(opcion == '2'):		   # lógica para hacer comentarios
			new_coment = usuario.comentar(artID)
			dictcomentarios[new_coment.id] = new_coment

def registrar_usuario():
	# Solicitar información del usuario
	id = 1+len(dictusuarios)
	nombre = input("Nombre: ")
	apellido = input("Apellido: ")
	telefono = input("Teléfono: ")
	username = input("Username: ")
	email = input("Email: ")
	contraseña = input("Contraseña: ")
	fecha_registro = datetime.date.today()
	avatar = input("Avatar: ")
	estado = input("Estado: ")
	colaborador = input("Quiere ser usuario público o colaborador? (P/C): ") == 'C' or 'c'
	online = False	# Hasta que no haga login, el usuario no está en linea

	if dictusuarios.get(username) != None: # Si el usuario existe
		print(f"Ya existe un usuario con el nombre {username}!")
		return

	if colaborador:
		usuario = Colaborador(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
	else:
		usuario = Publico(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)

	usuario.registrar()

def login_usuario():
	# Solicitar credenciales al usuario
	username = input("Username: ")
	contraseña = input("Contraseña: ")

	# Verificar si el usuario está registrado
	usuario_registrado = dictusuarios.get(username) != None 
	if not usuario_registrado:
		print(f"El usuario {username} no existe!")
		return

	contraseña_correcta = (contraseña == dictusuarios[username].contraseña)
	if not contraseña_correcta:
		print(f"Contraseña incorrecta!")
		return 

	# Recuperar la instancia del usuario
	usuario = dictusuarios.get(username)

	usuario.login()

	return usuario

def mostrar_comentarios(articulo_id):
	comentarios_articulo = []
	for comentario_id in dictcomentarios:
		comentario = dictcomentarios[comentario_id]
		if comentario.id_articulo == articulo_id:
			comentarios_articulo.append(comentario)

	if comentarios_articulo:
		print("Comentarios:")
		for comentario in comentarios_articulo:
			print(f" ({str(comentario.fecha_hora)}) {dictnombre[comentario.id_usuario]} dice:")
			print(f"\t {comentario.contenido}\n")
		  
	else:
		print("No hay comentarios para este artículo.")


# Iniciar el menu principal
menu_inicio()
