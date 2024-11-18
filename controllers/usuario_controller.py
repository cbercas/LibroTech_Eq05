# Archivo: T02_PR01\controllers\usuario_controller.py

from models.crud_usuario import CRUDUsuario  # Importar el CRUD que gestiona las operaciones de la base de datos
from models.usuario import Usuario  # Importar la clase Usuario para manipular objetos de tipo Usuario


class UsuarioController:
    """
    Controlador que maneja las interacciones entre las vistas (login y registro) y el modelo (usuario).
    """

    def __init__(self):
        # Instancia del CRUD para realizar operaciones con la base de datos
        self.crud_usuario = CRUDUsuario()  
    # __init__

    def registrar_usuario(self, email, nombre_usuario, password, password_confirmada):
        """
        Método para registrar un nuevo usuario en la base de datos.

        :param email: Correo electrónico del nuevo usuario (clave primaria).
        :param nombre_usuario: Nombre de usuario.
        :param password: Contraseña del usuario.
        :param password_confirmada: Confirmación de la contraseña.
        :return: Un objeto Usuario si el registro fue exitoso, o None en caso de error.
        """
        # Validar que las contraseñas coincidan
        if password != password_confirmada:  # Comparación explícita para verificar que ambas contraseñas coinciden
            print("Las contraseñas no coinciden.")  # Imprimir mensaje de error si las contraseñas no coinciden
            return None  # Retornar None si hay un error en las contraseñas

        # Verificar si ya existe un usuario con el email proporcionado
        usuario_existente = self.crud_usuario.obtener_usuario(email)  # Buscar en la base de datos si ya existe el usuario
        if usuario_existente is not None:  # Si el usuario ya existe, el condicional es explícito
            print(f"Ya existe un usuario con el correo: {email}")  # Imprimir mensaje de error si el usuario ya existe
            return None  # Retornar None si ya existe un usuario con ese correo

        # Si no existe, crear un nuevo usuario en la base de datos
        if self.crud_usuario.crear_usuario(email, nombre_usuario, password):  # Intentar crear el nuevo usuario
            print("Usuario creado exitosamente.")  # Mensaje indicando que el usuario fue creado
            # Retornar el nuevo objeto Usuario
            return Usuario(email, nombre_usuario, password)  # Crear y retornar el objeto Usuario
        else:
            print("Error al crear el usuario.")  # Imprimir mensaje de error si hubo un problema en la creación
            return None  # Retornar None si hubo un error en la creación del usuario
    # registrar_usuario

    def verificar_usuario(self, email, password):
        """
        Método para verificar si un usuario existe en la base de datos y las credenciales son correctas.

        :param email: Correo electrónico del usuario.
        :param password: Contraseña del usuario.
        :return: Un objeto Usuario si las credenciales son correctas, o None si son incorrectas.
        """
        usuario = self.crud_usuario.obtener_usuario(email)  # Obtener el usuario de la base de datos por el email
        if usuario is not None and usuario.get_password == password:  # Comparar si el usuario existe y la contraseña es correcta
            print("Usuario verificado correctamente.")  # Mensaje de éxito si el usuario fue verificado
            return usuario  # Retornar el objeto Usuario si las credenciales son correctas
        else:
            print("Credenciales incorrectas.")  # Mensaje de error si las credenciales no coinciden
            return None  # Retornar None si las credenciales son incorrectas
    # verificar_usuario

# UsuarioController
