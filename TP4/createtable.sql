CREATE TABLE ClientesAntiguos (
    ClienteId INT PRIMARY KEY IDENTITY(1,1),
    NombreCompleto VARCHAR(150) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    FechaRegistro DATETIME NOT NULL
);

CREATE TABLE ClientesActuales (
    ClienteId INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    FechaRegistro DATE NOT NULL
);
