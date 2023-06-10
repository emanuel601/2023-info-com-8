-- Entrega 7 - Tecnopower
-- Integrantes:
-- Godoy, Diego Gabriel 
-- Ortiz Kovalek, Emanuel 
-- Baibiene, Facundo
-- Alarcón, Julieta Guadalupe 
-- Agudo, Néstor Adrian
-- Bernardis, Mariela Iris
-- Sagania, Facundo
-- Maidana, Emiliano
-- Roldán, Ignacio
-- Nasir, Yamil Alí

CREATE DATABASE Blog;
USE Blog;
CREATE TABLE Usuarios (
  id INT AUTO_INCREMENT,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  username VARCHAR(50),
  email VARCHAR(100),
  telefono INT,
  avatar VARCHAR(250),
  contrasenia VARCHAR(100),
  estado BOOLEAN,
  es_publico BOOLEAN,
  es_colaborador BOOLEAN,
  es_admin BOOLEAN,
  fecha_creacion DATE,
  PRIMARY KEY(id)
);

CREATE TABLE Articulo (
  id INT AUTO_INCREMENT,
  id_usuario INT,
  titulo VARCHAR(255),
  resumen TEXT,
  contenido TEXT,
  fecha_publicacion DATE,
  estado BOOLEAN,
  imagen VARCHAR(255),
  PRIMARY KEY(id),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
);

CREATE TABLE Comentario (
  id INT AUTO_INCREMENT,
  id_articulo INT,
  id_usuario INT,
  contenido TEXT,
  fecha_hora DATETIME,
  estado BOOLEAN,
  PRIMARY KEY(id),
  FOREIGN KEY (id_articulo) REFERENCES Articulo(id),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
);



CREATE TABLE Categoria (
  id INT AUTO_INCREMENT,
  id_categoria INT,
  nombre VARCHAR(255),
  descripcion TEXT,
  imagen VARCHAR(255),
  estado BOOLEAN,
  PRIMARY KEY(id),
  FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
);

CREATE TABLE Categoria_Articulo (
  id INT AUTO_INCREMENT,
  id_articulo INT,
  id_categoria INT,
  PRIMARY KEY(id),
  FOREIGN KEY (id_articulo) REFERENCES Articulo(id),
  FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
);

--  Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol
--  de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos:
--  es_publico, es_colaborador y es_admin son booleanos

INSERT INTO Usuarios (nombre, apellido, username, email, contrasenia, estado, es_publico, es_colaborador, es_admin, avatar, fecha_creacion)
VALUES
  -- Usuario con rol de admin
  ('Admin', 'Pepe', 'adminiUsuario', 'admin@example.com', 'contrasenia_admin', true, false, false, true, 'http://miserverdeimg.com/admin.jpg', '2023-06-08'),

  -- Usuarios con rol de colaborador
  ('Colaborador1', 'Apellido1', 'colaborador1', 'colaborador1@example.com', 'contrasenia_colaborador1', true, false, true, false, 'http://miserverdeimg.com/colaborador1.jpg', '2023-06-08'),
  ('Colaborador2', 'Apellido2', 'colaborador2', 'colaborador2@example.com', 'contrasenia_colaborador2', true, false, true, false, 'http://miserverdeimg.com/colaborador2.jpg', '2023-06-08'),
  ('Colaborador3', 'Apellido3', 'colaborador3', 'colaborador3@example.com', 'contrasenia_colaborador3', true, false, true, false, 'http://miserverdeimg.com/colaborador3.jpg', '2023-06-08'),
  ('Colaborador4', 'Apellido4', 'colaborador4', 'colaborador4@example.com', 'contrasenia_colaborador4', true, false, true, false, 'http://miserverdeimg.com/colaborador4.jpg', '2023-06-08'),

  -- Usuarios con rol de público
  ('Usuario1', 'Apellido1', 'publico1', 'publico1@example.com', 'contrasenia_publico1', true, true, false, false, 'http://miserverdeimg.com/publico1.jpg', '2023-06-08'),
  ('Usuario2', 'Apellido2', 'publico2', 'publico2@example.com', 'contrasenia_publico2', true, true, false, false, 'http://miserverdeimg.com/publico2.jpg', '2023-06-08'),
  ('Usuario3', 'Apellido3', 'publico3', 'publico3@example.com', 'contrasenia_publico3', true, true, false, false, 'http://miserverdeimg.com/publico3.jpg', '2023-06-08'),
  ('Usuario4', 'Apellido4', 'publico4', 'publico4@example.com', 'contrasenia_publico4', true, true, false, false, 'http://miserverdeimg.com/publico4.jpg', '2023-06-08'),
  ('Usuario5', 'Apellido5', 'publico5', 'publico5@example.com', 'contrasenia_publico5', true, true, false, false, 'http://miserverdeimg.com/publico5.jpg', '2023-06-08');

-- Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios
-- agregado con rol de colaborador.

UPDATE Usuarios
SET es_colaborador = false, es_admin = true
WHERE id = 2;

--  Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
--  estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
--  Booleano.

INSERT INTO Articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES
  -- Artículos con estado TRUE
  (1, 'Artículo 1', 'Resumen del artículo 1', 'Contenido del artículo 1', '2023-06-08', true, 'http://miserverdeimg.com/imagen1.jpg'),
  (2, 'Artículo 2', 'Resumen del artículo 2', 'Contenido del artículo 2', '2023-06-09', true, 'http://miserverdeimg.com/imagen2.jpg'),
  (3, 'Artículo 3', 'Resumen del artículo 3', 'Contenido del artículo 3', '2023-06-10', true, 'http://miserverdeimg.com/imagen3.jpg'),

  -- Artículo con estado FALSE
  (4, 'Artículo 4', 'Resumen del artículo 4', 'Contenido del artículo 4', '2023-06-11', false, 'http://miserverdeimg.com/imagen4.jpg');

  
--  Agregar el comando necesario para eliminar el artículo que tenga estado FALSE

DELETE FROM Articulo
WHERE estado = false;

--  Agregar el comando necesario que introduzca 3 comentarios al primer artículo
--  agregado y 2 comentarios al segundo artículo

INSERT INTO Comentario (id_articulo, id_usuario, contenido, fecha_hora, estado)
VALUES
  -- Insertando 3 comentarios en el primer artículo
  (1, 1, 'Uhh loco mira que pro', '2023-06-08 10:00:00', true),
  (1, 2, 'Eaa meooo', '2023-06-08 11:00:00', true),
  (1, 3, 'Sera que funcionara?', '2023-06-08 12:00:00', true);


INSERT INTO Comentario (id_articulo, id_usuario, contenido, fecha_hora, estado)
VALUES
  -- Insertamos los 2 comentarios en el segundo artículo (ID: 2)
  (2, 1, 'See ameo todo peola', '2023-06-09 10:00:00', true),
  (2, 2, 'vamo a ve', '2023-06-09 11:00:00', true);


-- Agregar el comando necesario para listar todos los artículos que tengan
-- comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
-- nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
-- comentario, agrupados por artículos.

SELECT
  Articulo.titulo,
  Articulo.fecha_publicacion,
  Usuarios.nombre AS nombre_usuario,
  Comentario.fecha_hora AS fecha_hora_comentario
FROM
  Articulo
  INNER JOIN Comentario ON Articulo.id = Comentario.id_articulo
  INNER JOIN Usuarios ON Comentario.id_usuario = Usuarios.id
GROUP BY
  Articulo.id, Articulo.titulo, Articulo.fecha_publicacion,
  Usuarios.nombre, Comentario.fecha_hora;