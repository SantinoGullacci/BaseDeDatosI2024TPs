1.Primera Forma Normal (1NF)

Todas las columnas de las tablas (Usuarios, Libros, Prestamos, Cuotas) contienen valores indivisibles. Por ejemplo, el campo nombre en la tabla Usuarios almacena un solo nombre por registro.
No hay columnas que contengan listas de valores (por ejemplo, no hay una columna que contenga multiples titulos de libros).
Cada fila es unica debido a la clave primaria definida en cada tabla.

2.Segunda Forma Normal (2NF)

En la tabla Usuarios, todas las columnas (nombre, apellido, email, telefono, fecha_registro) dependen completamente de la clave primaria dni.
En la tabla Libros, todas las columnas (titulo, autor, genero, editorial, anio_publicacion) dependen completamente de la clave primaria libro_id.
En Prestamos, todas las columnas (dni_usuario, libro_id, fecha_prestamo, fecha_devolucion) dependen completamente de la clave primaria id.
En Cuotas, todas las columnas (dni_usuario, monto, mes, anio, estado_pago) dependen completamente de la clave primaria id.
No hay dependencias parciales.

3.Tercera Forma Normal (3NF)

En Usuarios, no hay dependencias transitivas. Por ejemplo, email, telefono y fecha_registro dependen exclusivamente de dni.
En Libros, no hay dependencias transitivas. Cada columna (como titulo o autor) depende directamente de libro_id.
En Prestamos, no hay dependencias transitivas. La relacion entre dni_usuario y libro_id esta gestionada por claves externas, y las fechas (fecha_prestamo, fecha_devolucion) dependen solo de la clave primaria id.
En Cuotas, tampoco hay dependencias transitivas. Cada columna depende unicamente de la clave primaria id. La relacion entre dni_usuario y las cuotas esta correctamente gestionada mediante la clave foranea.