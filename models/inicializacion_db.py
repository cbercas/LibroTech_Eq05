# Archivo: T02_PR01\models\inicializacion_db.py

import models.database_manager as db  # Importar el módulo db que está dentro de models para manejar la conexión a la base de datos


# Función para crear las tablas necesarias en la base de datos
def create_tables():
    """
    Crear las tablas de Usuarios si no existen en la base de datos.
    
    Se asegura de que la tabla 'usuarios' exista, de lo contrario la crea.
    """
    # Definir los comandos SQL que se ejecutarán para crear las tablas
    # Se usa 'CREATE TABLE IF NOT EXISTS' para evitar errores si la tabla ya existe
    
    # Campo 'email' como clave primaria
    # Campo 'nombre_usuario' obligatorio
    # Campo 'password' obligatorio
    commands = (
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            email VARCHAR(255) PRIMARY KEY,  
            nombre_usuario VARCHAR(255) NOT NULL,  
            password VARCHAR(255) NOT NULL  
        )
        """,
          """
        CREATE TABLE IF NOT EXISTS libros (
            isbn VARCHAR(20) PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(255) NOT NULL,
            genero VARCHAR(100) NOT NULL,
            publicacion INT NOT NULL
        );
        """
    )
    
    try:
        # Conectarse a la base de datos utilizando la función connect_db() del archivo db
        conn = db.connect_db()
        # Verificar si la conexión se realizó correctamente
        if conn is not None:  # Hacemos explícita la condición
            with conn.cursor() as cur:  # Usamos un cursor para ejecutar comandos SQL
                # Ejecutar cada comando dentro de la tupla 'commands'
                for command in commands:
                    cur.execute(command)  # Ejecuta el comando SQL
                conn.commit()  # Confirmar (guardar) los cambios en la base de datos
                print("Tablas creadas correctamente.")
            conn.close()  # Cerrar la conexión a la base de datos
        else:
            print("No se pudo conectar a la base de datos.")
    except Exception as error:  # Capturar cualquier excepción que ocurra
        # Mostrar un mensaje de error si ocurre alguna excepción
        print(f"Error al crear las tablas: {error}")
# create_tables


# Función para insertar datos de ejemplo en la tabla 'usuarios'
def insert_data():
    """
    Insertar datos de ejemplo en la tabla 'usuarios' si no existen.
    
    Se insertan 3 usuarios de ejemplo y se utiliza 'ON CONFLICT' para evitar duplicados.
    """
    # Tupla que contiene los datos a insertar (email, nombre de usuario, contraseña)
    user_inserts = (
        ('usuario1@example.com', 'usuario1', 'usuario0?'),
        ('usuario2@example.com', 'usuario2', 'usuario0?'),
        ('usuario3@example.com', 'usuario3', 'usuario0?')
    )
    book_inserts = (
        ('978-0-06-088328-7', 'Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', 1967),
        ('978-0-452-28423-4', '1984', 'George Orwell', 'Ciencia ficción', 1949),
        ('978-1-59308-201-1', 'Orgullo y prejuicio', 'Jane Austen', 'Romance', 1813),
        ('978-0-618-12902-9', 'El señor de los anillos', 'J.R.R. Tolkien', 'Fantasía', 1954),
        ('978-0-14-243723-0', 'Don Quijote de la Mancha', 'Miguel de Cervantes', 'Aventura', 1605),
        ('978-0-14-044913-6', 'Crimen y castigo', 'Fiódor Dostoyevski', 'Drama psicológico', 1866),
        ('978-0-06-093546-7', 'Matar a un ruiseñor', 'Harper Lee', 'Drama', 1960),
        ('978-0-452-27352-9', 'La casa de los espíritus', 'Isabel Allende', 'Realismo mágico', 1982),
        ('978-0-7432-7356-5', 'El gran Gatsby', 'F. Scott Fitzgerald', 'Ficción', 1925),
        ('978-0-545-01022-1', 'Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', 1997),
        ('978-1-4516-7331-9', 'Fahrenheit 451', 'Ray Bradbury', 'Ciencia ficción', 1953),
        ('978-0-451-22244-5', 'La sombra del viento', 'Carlos Ruiz Zafón', 'Misterio', 2001),
        ('978-0-14-143984-6', 'Drácula', 'Bram Stoker', 'Terror', 1897),
        ('978-0-14-118227-1', 'La Metamorfosis', 'Franz Kafka', 'Ficción surrealista', 1915),
        ('978-0-14-044430-8', 'Los miserables', 'Victor Hugo', 'Drama', 1862),
        ('978-0-15-601219-5', 'El Principito', 'Antoine de Saint-Exupéry', 'Fábula', 1943),
        ('978-0-14-143955-6', 'Cumbres borrascosas', 'Emily Brontë', 'Romance gótico', 1847),
        ('978-0-385-50420-8', 'El código Da Vinci', 'Dan Brown', 'Suspenso', 2003),
        ('978-0-14-118280-3', 'Ulises', 'James Joyce', 'Ficción modernista', 1922),
        ('978-0-14-026886-7', 'La Odisea', 'Homero', 'Épico', -800)
    )
    
    # Definir la consulta SQL para insertar los datos en la tabla 'usuarios'
    user_insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """  # Se usa 'ON CONFLICT' para evitar errores de inserción si ya existe un usuario con el mismo email.
    
    book_insert_query = """
        INSERT INTO libros (isbn, titulo, autor, genero, publicacion)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (isbn) DO NOTHING;
        """  # Se usa 'ON CONFLICT' para evitar errores de inserción si ya existe un libro con el mismo ID.
    
    try:
        # Conectarse a la base de datos
        conn = db.connect_db()
        # Verificar si la conexión se realizó correctamente
        if conn is not None:  # Hacemos explícita la condición
            with conn.cursor() as cur:  # Crear un cursor para ejecutar comandos SQL
                # Iterar sobre los usuarios en la tupla 'inserts'
                for user in user_inserts:
                    cur.execute(user_insert_query, user)  # Ejecutar la consulta SQL para cada usuario
                conn.commit()  # Confirmar (guardar) los cambios en la base de datos
                print("Datos insertados correctamente.")
                for book in book_inserts:
                    cur.execute(book_insert_query, book)  # Ejecutar la consulta SQL para cada libro
                conn.commit()  # Confirmar (guardar) los cambios en la base de datos
                print("Datos de libros insertados correctamente.")
            conn.close()  # Cerrar la conexión a la base de datos
        else:
            print("No se pudo conectar a la base de datos.")
    except Exception as error:  # Capturar cualquier excepción que ocurra
        # Mostrar un mensaje de error si ocurre alguna excepción
        print(f"Error al insertar datos: {error}")
# insert_data

# Función para inicializar la base de datos, creando tablas e insertando datos de ejemplo
def init_db():
    """
    Inicializar la base de datos llamando a las funciones de creación de tablas e inserción de datos.
    """
    create_tables()  # Llamar a la función que crea las tablas
    insert_data()  # Llamar a la función que inserta los datos de ejemplo

# init_db
