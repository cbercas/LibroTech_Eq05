/* https://www.postgresqltutorial.com/ */

-- Crear la tabla de Usuarios si no existe
CREATE TABLE IF NOT EXISTS Usuarios (
    email VARCHAR(255) PRIMARY KEY, -- El email será la clave primaria
    nombre_usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

/* Crear la tabla de Libros si no existe */
CREATE TABLE IF NOT EXISTS Libros (
    isbn SERIAL PRIMARY KEY,       -- Identificador único del libro (clave primaria)
    titulo VARCHAR(255) NOT NULL,      -- Título del libro
    autor VARCHAR(255) NOT NULL,       -- Autor del libro
    genero VARCHAR(100),               -- Género del libro
    publicacion INT                    -- Año de publicación del libro
);

-- Insertar datos de prueba en la tabla Usuarios
INSERT INTO Usuarios (email, nombre_usuario, password)
VALUES 
('usuario1@example.com', 'usuario1', 'password1'),
('usuario2@example.com', 'usuario2', 'password2'),
('usuario3@example.com', 'usuario3', 'password3');

/* Insertar datos de prueba en la tabla Libros */
INSERT INTO Libros (titulo, autor, genero, publicacion)
VALUES 
    ('Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', 1967),
    ('1984', 'George Orwell', 'Ciencia ficción', 1949),
    ('Orgullo y prejuicio', 'Jane Austen', 'Romance', 1813),
    ('El señor de los anillos', 'J.R.R. Tolkien', 'Fantasía', 1954),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Aventura', 1605),
    ('Crimen y castigo', 'Fiódor Dostoyevski', 'Drama psicológico', 1866),
    ('Matar a un ruiseñor', 'Harper Lee', 'Drama', 1960),
    ('La casa de los espíritus', 'Isabel Allende', 'Realismo mágico', 1982),
    ('El gran Gatsby', 'F. Scott Fitzgerald', 'Ficción', 1925),
    ('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', 1997),
    ('Fahrenheit 451', 'Ray Bradbury', 'Ciencia ficción', 1953),
    ('La sombra del viento', 'Carlos Ruiz Zafón', 'Misterio', 2001),
    ('Drácula', 'Bram Stoker', 'Terror', 1897),
    ('La Metamorfosis', 'Franz Kafka', 'Ficción surrealista', 1915),
    ('Los miserables', 'Victor Hugo', 'Drama', 1862),
    ('El Principito', 'Antoine de Saint-Exupéry', 'Fábula', 1943),
    ('Cumbres borrascosas', 'Emily Brontë', 'Romance gótico', 1847),
    ('El código Da Vinci', 'Dan Brown', 'Suspenso', 2003),
    ('Ulises', 'James Joyce', 'Ficción modernista', 1922),
    ('La Odisea', 'Homero', 'Épico', -800); 
     -- Para fechas aproximadas, puede usarse un valor negativo o un campo diferente

-- Seleccionar todos los registros de la tabla Usuarios
SELECT * FROM Usuarios;

/* Seleccionar todos los registros de la tabla Libros */
SELECT * FROM Libros;


-- Eliminar todos los registros de la tabla Usuarios sin eliminar su estructura
TRUNCATE TABLE Usuarios;

/* Eliminar todos los registros de la tabla Libros sin eliminar su estructura */
TRUNCATE TABLE Libros;


-- Eliminar la tabla Usuarios si existe
DROP TABLE IF EXISTS Usuarios;

/* Eliminar la tabla Libros si existe */
DROP TABLE IF EXISTS Libros;