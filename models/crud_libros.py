from models import database_manager
from models.libro import Libro
from PySide6.QtWidgets import QMainWindow, QMessageBox  # Importar QMessageBox para mostrar mensajes de error


class CRUDLibro:
    def obtener_libros(self):
            """
            Método para obtener un libro de la base de datos.
           
            :return: Un objeto de la clase Libro si se encuentra, None en caso contrario.
            """
            # Definir la consulta SQL para obtener un libro
            print( "He llegado al crud de libro")  # Mensaje de error

            query = "SELECT isbn,titulo,autor,genero,publicacion FROM libros"
            # Conectar a la base de datos utilizando la función connect_db
            conn = database_manager.connect_db()
            if conn is None:  # Si no hay conexión, no se puede continuar
                return None

            try:
                # Ejecutar la consulta SQL dentro de un bloque con el cursor
                with conn.cursor() as cursor:
                    cursor.execute(query)  # Ejecutar la consulta con el parámetro email
                    filas = cursor.fetchall()  # Obtener todas las filas
                    if filas is not None:  # Comparación explícita de que el resultado no es None
                        # Desempaqueta la tupla 'filas' y pasa cada valor como un argumento separado 
                        # (isbn, titulo, autor, genero, publicacion) al constructor de la clase 'Libro'
                        return [Libro(isbn=fila[0], titulo=fila[1], autor=fila[2], genero=fila[3], publicacion=fila[4]) for fila in filas]

                    return None  # Si no hay resultados, retornar None
            except Exception as error:
                print(f"Error al obtener libro: {error}")  # Mostrar el error en caso de excepción
                return None
            finally:
                database_manager.close_connection(conn)  # Cerrar la conexión al terminar
        # obtener_libros