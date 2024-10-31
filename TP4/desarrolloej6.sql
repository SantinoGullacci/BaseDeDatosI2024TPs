CREATE PROCEDURE MigrarClientes()
BEGIN
    DECLARE ClienteId INT;
    DECLARE NombreCompleto VARCHAR(150);
    DECLARE Telefono VARCHAR(20);
    DECLARE Direccion VARCHAR(255);
    DECLARE FechaRegistro DATETIME;
    DECLARE Nombre VARCHAR(100);
    DECLARE Apellido VARCHAR(50);
    DECLARE PosUltimoEspacio INT;
    DECLARE done INT DEFAULT FALSE;

    DECLARE cursor_clientes CURSOR FOR
        SELECT ClienteId, NombreCompleto, Telefono, Direccion, FechaRegistro FROM ClientesAntiguos;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursor_clientes;

    FETCH cursor_clientes INTO ClienteId, NombreCompleto, Telefono, Direccion, FechaRegistro;

    WHILE NOT done DO
        SET PosUltimoEspacio = LENGTH(NombreCompleto) - LOCATE(' ', REVERSE(NombreCompleto)) + 1;

        SET Nombre = LEFT(NombreCompleto, PosUltimoEspacio - 1);
        SET Apellido = RIGHT(NombreCompleto, LENGTH(NombreCompleto) - PosUltimoEspacio);

        INSERT INTO ClientesActuales (Nombre, Apellido, Telefono, Direccion, FechaRegistro)
        VALUES (Nombre, Apellido, Telefono, Direccion, FechaRegistro);

        FETCH cursor_clientes INTO ClienteId, NombreCompleto, Telefono, Direccion, FechaRegistro;
    END WHILE;

    CLOSE cursor_clientes;
END;