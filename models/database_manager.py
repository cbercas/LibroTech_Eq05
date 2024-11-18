import psycopg  # Importamos el módulo `psycopg`, que es una biblioteca para trabajar con PostgreSQL desde Python.

# Función para conectar a la base de datos PostgreSQL
def connect_db():
    """
    Conectar a la base de datos PostgreSQL y devolver la conexión.
    
    :return: Objeto de conexión a la base de datos o None en caso de error.
    """
    try:
        # Intentamos crear una conexión a la base de datos usando los datos proporcionados
        conn = psycopg.connect(
            dbname="eq_05_librotech_db",  # Nombre de la base de datos
            user="admin",  # Usuario de la base de datos
            password="0000",  # Contraseña del usuario
            host="localhost",  # Dirección del servidor de la base de datos
            port="60000" # Puerto en el que escucha PostgreSQL              # Puerto en el que se ejecuta PostgreSQL
        )
        return conn  # Si la conexión es exitosa, se devuelve el objeto `conn`
    except Exception as error:
        # Si ocurre algún error durante la conexión, se captura la excepción y se imprime un mensaje de error
        print(f"Error al conectar con la base de datos: {error}")
        return None  # En caso de error, se devuelve `None` para indicar que no se pudo conectar
# connect_db

# Función para cerrar la conexión a la base de datos PostgreSQL
def close_connection(conn):
    """
    Cerrar la conexión a la base de datos PostgreSQL.
    
    :param conn: La conexión a la base de datos que se desea cerrar.
    """
    if conn is not None:  # Verificamos si la conexión existe (no es None)
        try:
            conn.close()  # Intentamos cerrar la conexión si está activa
        except Exception as error:
            # Si ocurre algún error al cerrar la conexión, se captura la excepción y se imprime un mensaje de error
            print(f"Error al cerrar la conexión a la base de datos: {error}")
# close_connection

