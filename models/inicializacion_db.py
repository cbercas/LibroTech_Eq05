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
            isbn SERIAL PRIMARY KEY,  -- Generar un ID único para cada libro
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
        ('Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', 1967),
        ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela', 1605),
        ('1984', 'George Orwell', 'Distopía', 1949)
    )
    
    # Definir la consulta SQL para insertar los datos en la tabla 'usuarios'
    user_insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """  # Se usa 'ON CONFLICT' para evitar errores de inserción si ya existe un usuario con el mismo email.
    
    book_insert_query = """
        INSERT INTO libros (titulo, autor, genero, publicacion)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (titulo) DO NOTHING;
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
