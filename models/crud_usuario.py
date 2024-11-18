# Archivo: T02_PR01\models\crud_usuario.py

#import psycopg  # Importar la biblioteca `psycopg` para trabajar con PostgreSQL
from models import database_manager  # Importar el módulo 'db' desde el paquete 'models' para manejar la conexión a la base de datos
from models.usuario import Usuario  # Importar la clase Usuario para representar los datos del usuario

class CRUDUsuario:
    """
    Clase que implementa operaciones CRUD para la tabla 'usuarios' en la base de datos.
    """

    def crear_usuario(self, email, nombre_usuario, password):
        """
        Método para crear un nuevo usuario en la base de datos.
        
        :param email: Correo electrónico del nuevo usuario (clave primaria).
        :param nombre_usuario: Nombre de usuario.
        :param password: Contraseña del usuario.
        :return: True si el usuario fue creado correctamente, False en caso de error.
        """
        # Definir la consulta SQL para insertar el nuevo usuario en la base de datos
        query = """
        INSERT INTO usuarios (email, nombre_usuario, password) 
        VALUES (%s, %s, %s)
        """
        # Conectar a la base de datos utilizando la función connect_db
        conn = database_manager.connect_db()
        if conn is None:  # Si no hay conexión, no se puede continuar
            return False

        try:
            # Ejecutar la consulta SQL dentro de un bloque con el cursor
            with conn.cursor() as cursor:
                cursor.execute(query, (email, nombre_usuario, password))  # Ejecutar la consulta con los parámetros
                conn.commit()  # Confirmar los cambios en la base de datos
                return True  # Indicar que la operación fue exitosa
        except Exception as error:
            print(f"Error al crear usuario: {error}")  # Mostrar el error en caso de excepción
            return False
        finally:
            database_manager.close_connection(conn)  # Cerrar la conexión al terminar
    # crear_usuario

    def obtener_usuario(self, email):
        """
        Método para obtener un usuario de la base de datos por su email.
        
        :param email: Correo electrónico del usuario que se desea obtener.
        :return: Un objeto de la clase Usuario si se encuentra, None en caso contrario.
        """
        # Definir la consulta SQL para obtener un usuario por su email
        query = "SELECT email, nombre_usuario, password FROM usuarios WHERE email = %s"
        # Conectar a la base de datos utilizando la función connect_db
        conn = database_manager.connect_db()
        if conn is None:  # Si no hay conexión, no se puede continuar
            return None

        try:
            # Ejecutar la consulta SQL dentro de un bloque con el cursor
            with conn.cursor() as cursor:
                cursor.execute(query, (email,))  # Ejecutar la consulta con el parámetro email
                resultado = cursor.fetchone()  # Obtener el primer resultado
                if resultado is not None:  # Comparación explícita de que el resultado no es None
                    # Desempaqueta la tupla 'resultado' y pasa cada valor como un argumento separado 
                    # (email, nombre_usuario, password) al constructor de la clase 'Usuario'
                    return Usuario(*resultado)
                return None  # Si no hay resultados, retornar None
        except Exception as error:
            print(f"Error al obtener usuario: {error}")  # Mostrar el error en caso de excepción
            return None
        finally:
            database_manager.close_connection(conn)  # Cerrar la conexión al terminar
    # obtener_usuario

    def actualizar_usuario(self, email, nuevo_nombre_usuario=None, nueva_password=None):
        """
        Método para actualizar los datos de un usuario en la base de datos.
        
        :param email: Correo electrónico del usuario a actualizar (clave primaria).
        :param nuevo_nombre_usuario: Nuevo nombre de usuario (opcional).
        :param nueva_password: Nueva contraseña (opcional).
        :return: True si los datos se actualizaron correctamente, False en caso de error.
        """
        # Definir la consulta SQL para actualizar un usuario por su email
        query = "UPDATE usuarios SET nombre_usuario = %s, password = %s WHERE email = %s"
        # Conectar a la base de datos utilizando la función connect_db
        conn = database_manager.connect_db()
        if conn is None:  # Si no hay conexión, no se puede continuar
            return False

        try:
            # Ejecutar la consulta SQL dentro de un bloque con el cursor
            with conn.cursor() as cursor:
                cursor.execute(query, (nuevo_nombre_usuario, nueva_password, email))  # Ejecutar la consulta
                conn.commit()  # Confirmar los cambios en la base de datos
                return True  # Indicar que la operación fue exitosa
        except Exception as error:
            print(f"Error al actualizar usuario: {error}")  # Mostrar el error en caso de excepción
            return False
        finally:
            database_manager.close_connection(conn)  # Cerrar la conexión al terminar
    # actualizar_usuario

    def eliminar_usuario(self, email):
        """
        Método para eliminar un usuario de la base de datos.
        
        :param email: Correo electrónico del usuario a eliminar.
        :return: True si el usuario fue eliminado correctamente, False en caso de error.
        """
        # Definir la consulta SQL para eliminar un usuario por su email
        query = "DELETE FROM usuarios WHERE email = %s"
        # Conectar a la base de datos utilizando la función connect_db
        conn = database_manager.connect_db()
        if conn is None:  # Si no hay conexión, no se puede continuar
            return False

        try:
            # Ejecutar la consulta SQL dentro de un bloque con el cursor
            with conn.cursor() as cursor:
                cursor.execute(query, (email,))  # Ejecutar la consulta con el parámetro email
                conn.commit()  # Confirmar los cambios en la base de datos
                return True  # Indicar que la operación fue exitosa
        except Exception as error:
            print(f"Error al eliminar usuario: {error}")  # Mostrar el error en caso de excepción
            return False
        finally:
            database_manager.close_connection(conn)  # Cerrar la conexión al terminar
    # eliminar_usuario

    def listar_usuarios(self):
        """
        Método para obtener una lista de todos los usuarios registrados en la base de datos.
        
        :return: Lista de objetos Usuario, o lista vacía en caso de error.
        """
        # Definir la consulta SQL para obtener todos los usuarios
        query = "SELECT email, nombre_usuario, password FROM usuarios"
        # Conectar a la base de datos utilizando la función connect_db
        conn = database_manager.connect_db()
        if conn is None:  # Si no hay conexión, no se puede continuar
            return []

        try:
            # Ejecutar la consulta SQL dentro de un bloque con el cursor
            with conn.cursor() as cursor:
                cursor.execute(query)  # Ejecutar la consulta
                resultados = cursor.fetchall()  # Obtener todos los resultados
                if resultados:  # Verificar si `resultados` contiene datos
                    # Retorna una lista de objetos Usuario
                    return [Usuario(*row) for row in resultados]
                return []  # Retorna una lista vacía si no hay resultados
        except Exception as error:
            print(f"Error al listar usuarios: {error}")  # Mostrar el error en caso de excepción
            return []
        finally:
            database_manager.close_connection(conn)  # Cerrar la conexión al terminar
    # listar_usuarios
# CRUDUsuario
