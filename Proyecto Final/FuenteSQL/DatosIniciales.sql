--Tablas rellenadas automaticamente con datos brindados por IA


INSERT INTO Usuarios (dni, nombre, apellido, email, telefono, fecha_registro) VALUES
('10000001', 'Juan', 'Pérez', 'juan.perez@email.com', '1111111111', '2023-01-15'),
('10000002', 'Ana', 'García', 'ana.garcia@email.com', '2222222222', '2023-03-10'),
('10000003', 'Luis', 'Martínez', 'luis.martinez@email.com', '3333333333', '2023-06-05'),
('10000004', 'María', 'López', 'maria.lopez@email.com', '4444444444', '2023-08-20'),
('10000005', 'Carlos', 'Rodríguez', 'carlos.rodriguez@email.com', '5555555555', '2023-10-10'),
('10000006', 'Laura', 'Fernández', 'laura.fernandez@email.com', '6666666666', '2024-01-25'),
('10000007', 'Roberto', 'Gómez', 'roberto.gomez@email.com', '7777777777', '2024-03-15'),
('10000008', 'Sofía', 'Romero', 'sofia.romero@email.com', '8888888888', '2024-05-05'),
('10000009', 'Martín', 'Díaz', 'martin.diaz@email.com', '9999999999', '2024-07-30'),
('10000010', 'Julia', 'Torres', 'julia.torres@email.com', '1010101010', '2024-09-20');

INSERT INTO Libros (titulo, autor, genero, editorial, anio_publicacion) VALUES
('El Principito', 'Antoine de Saint-Exupéry', 'Ficción', 'Salamandra', 1943),
('1984', 'George Orwell', 'Distopía', 'Secker & Warburg', 1949),
('Cien Años de Soledad', 'Gabriel García Márquez', 'Realismo Mágico', 'Sudamericana', 1967),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Clásico', 'Francisco de Robles', 1605),
('Matar a un Ruiseñor', 'Harper Lee', 'Drama', 'J.B. Lippincott & Co.', 1960),
('Orgullo y Prejuicio', 'Jane Austen', 'Romance', 'T. Egerton', 1813),
('La Odisea', 'Homero', 'Épica', 'Desconocido', -700),
('Crimen y Castigo', 'Fiódor Dostoyevski', 'Filosofía', 'The Russian Messenger', 1866),
('El Hobbit', 'J.R.R. Tolkien', 'Fantasía', 'Allen & Unwin', 1937),
('Las Aventuras de Sherlock Holmes', 'Arthur Conan Doyle', 'Misterio', 'George Newnes', 1892);

INSERT INTO Prestamos (dni_usuario, libro_id, fecha_prestamo, fecha_devolucion) VALUES
('10000001', 1, '2024-01-10', '2024-01-20'),
('10000002', 2, '2024-03-05', '2024-03-15'),
('10000003', 3, '2024-04-01', '2024-04-10'),
('10000004', 4, '2024-05-20', '2024-05-30'),
('10000005', 5, '2024-06-10', NULL),
('10000006', 6, '2024-07-15', '2024-07-25'),
('10000007', 7, '2024-08-05', '2024-08-15'),
('10000008', 8, '2024-09-01', NULL),
('10000009', 9, '2024-10-20', '2024-11-01'),
('10000010', 10, '2024-11-10', NULL);

INSERT INTO Cuotas (dni_usuario, monto, mes, anio, estado_pago) VALUES
('10000001', 150.00, 1, 2024, 'PAGADO'),
('10000002', 200.00, 2, 2024, 'PAGADO'),
('10000003', 180.00, 3, 2024, 'PENDIENTE'),
('10000004', 220.00, 4, 2024, 'PAGADO'),
('10000005', 170.00, 5, 2024, 'PENDIENTE'),
('10000006', 190.00, 6, 2024, 'PAGADO'),
('10000007', 210.00, 7, 2024, 'PENDIENTE'),
('10000008', 200.00, 8, 2024, 'PAGADO'),
('10000009', 195.00, 9, 2024, 'PAGADO'),
('10000010', 185.00, 10, 2024, 'PENDIENTE');
