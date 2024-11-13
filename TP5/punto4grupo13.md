Paso 1: Determinar las Dependencias Funcionales (DFs)

codigoSucursal -> domicilioSucursal, telefonoSucursal: El codigoSucursal corresponde a una sucursal puntual para la cual conocemos el domicilio, teléfono, las fosas que tiene y los mecánicos que trabajan en la misma.

codigoSucursal, codigoFosa -> largoFosa, anchoFosa: De las fosas conocemos el código, el mismo es un número secuencial para cada sucursal (dos sucursales podrían tener el código de fosa 1, pero serían dos fosas distintas). También registramos el largo y ancho de las mismas.

codigoSucursal, codigoFosa -> patenteAuto: En una Fosa se arreglan autos, hay que registrar para cada fosa qué autos se arreglaron en la misma. De los autos conocemos la patente, la marca, el modelo y el cliente que lo acercó.

patenteAuto -> marcaAuto, modeloAuto, dniCliente: Para un auto registramos un único cliente, pero un cliente puede tener varios autos.

dniCliente -> nombreCliente, celularCliente: Para los clientes registramos el dni, el nombre y el celular.

dniMecanico -> nombreMecanico, emailMecanico: Para los mecánicos registramos el dni, el nombre y el email.




Paso 2: Determinar las Claves Candidatas

(codigoSucursal, codigoFosa) dado que cada combinación de sucursal y fosa deben de tener un auto, cliente, y mecánico específicos.




Paso 3: Diseño en Tercera Forma Normal (3FN)

1. Tabla Taller

    codigoSucursal (Clave foranea que referencia a Sucursal)
    cosdigoFosa (Clave foranea que referencia a Fosa)
    Clave primaria compuesta: (codigoSucursal, codigoFosa)

2. Tabla Sucursal

    codigoSucursal (Clave primaria)
    domicilioSucursal 
    telefonoSucursal

3. Tabla Fosa

    codigoSucursal (Clave foranea que referencia a Sucursal)
    codigoFosa (Clave primaria)
    largoFosa
    anchoFosa

4. Tabla Auto

    dniCliente (Clave foranea que referenia a Cliente)
    patenteAuto (Clave primaria)
    marcaAuto
    modeloAuto
    

5. Tabla Cliente

    dniCliente (Clave primaria)
    nombreCliente
    celularCliente

6. Tabla Mecanico

    dniMecanico (Clave primaria)
    nombreMecanico
    emailMecanico