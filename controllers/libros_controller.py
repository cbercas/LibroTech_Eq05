
from models.crud_libros import CRUDLibro  # Importar el CRUD que gestiona las operaciones de la base de datos
from models.libro import Libro  # Importar la clase Libro para manipular objetos de tipo Usuario
from PySide6.QtWidgets import QMainWindow, QMessageBox  # Importar QMessageBox para mostrar mensajes de error


class LibroController:
    """
    Controlador que maneja las interacciones con los objetos libros
    """

    def __init__(self):
        # Instancia del CRUD para realizar operaciones con la base de datos
        print("iniciando controller libro")
        self.crud_libro = CRUDLibro()  
    # __init__

    def obtener_libros(self):
        
        print("He llegado al controller de obtener libro.")  # Mensaje de error

        """
        Método para obtener los libros existentes en la base de datos 
        """
        libros = self.crud_libro.obtener_libros()  # Obtener los libros de la base de datos
      
        return libros  # Retornar libros
 
