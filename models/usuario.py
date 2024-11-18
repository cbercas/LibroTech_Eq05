class Usuario:
    def __init__(self, email, nombre_usuario, password):
        """
        Constructor para la clase Usuario.

        :param email: Correo electrónico del usuario.
        :param nombre_usuario: Nombre de usuario.
        :param password: Contraseña del usuario.
        """
        # Almacena el email del usuario (atributo privado)
        self._email = email  
        # Almacena el nombre de usuario (atributo privado)
        self._nombre_usuario = nombre_usuario  
        # Almacena la contraseña del usuario (atributo privado)
        self._password = password  
    # __init__

    # Getters
    @property
    def get_email(self):
        """
        Getter para obtener el email del usuario.
        :return: Correo electrónico del usuario.
        """
        return self._email  # Devuelve el email almacenado
    # get_email

    @property
    def get_nombre_usuario(self):
        """
        Getter para obtener el nombre de usuario.
        :return: Nombre de usuario.
        """
        return self._nombre_usuario  # Devuelve el nombre de usuario almacenado
    # get_nombre_usuario

    @property
    def get_password(self):
        """
        Getter para obtener la contraseña del usuario.
        :return: Contraseña del usuario.
        """
        return self._password  # Devuelve la contraseña almacenada
    # get_password

    # Setters
    @get_email.setter
    def set_email(self, nuevo_email):
        """
        Setter para establecer un nuevo email.
        :param nuevo_email: Nuevo correo electrónico.
        """
        self._email = nuevo_email  # Establece un nuevo valor de email
    # set_email

    @get_nombre_usuario.setter
    def set_nombre_usuario(self, nuevo_nombre_usuario):
        """
        Setter para establecer un nuevo nombre de usuario.
        :param nuevo_nombre_usuario: Nuevo nombre de usuario.
        """
        self._nombre_usuario = nuevo_nombre_usuario  # Establece un nuevo valor de nombre de usuario
    # set_nombre_usuario

    @get_password.setter
    def set_password(self, nueva_password):
        """
        Setter para establecer una nueva contraseña.
        :param nueva_password: Nueva contraseña.
        """
        self._password = nueva_password  # Establece un nuevo valor de contraseña
    # set_password

    # Método para representar al usuario como una cadena
    def __str__(self):
        """
        Representación en cadena del objeto Usuario.
        :return: Representación en formato de cadena del usuario.
        """
        return f"Usuario: {self.get_nombre_usuario}, Email: {self.get_email}"  # Devuelve una representación legible
    # __str__

    # Método para representación oficial (útil para debugging y desarrollo)
    def __repr__(self):
        """
        Representación formal del objeto Usuario, más detallada y útil para desarrolladores.
        :return: Representación en formato de cadena del usuario, incluyendo detalles internos.
        """
        return f"Usuario(email={self._email!r}, nombre_usuario={self._nombre_usuario!r}, password={self._password!r})"  
        # Devuelve una representación detallada para desarrolladores
    # __repr__

    # Método para cambiar la contraseña
    def cambiar_password(self, nueva_password):
        """
        Método para cambiar la contraseña del usuario.
        :param nueva_password: Nueva contraseña del usuario.
        """
        self._password = nueva_password  # Cambia la contraseña del usuario
    # cambiar_password

# Usuario

"""
Explicación de __str__ y __repr__:

- **__str__**:
  - Este método está diseñado para devolver una representación amigable para los usuarios finales.
  - Se utiliza cuando se imprime el objeto o se convierte a cadena, por ejemplo, al usar `print(objeto)`.
  - En este caso, simplemente devuelve información básica del usuario como "Usuario: nombre, Email: email".

- **__repr__**:
  - Este método devuelve una representación oficial del objeto, pensada para desarrolladores.
  - Es útil para debugging o desarrollo, ya que muestra una representación más completa y precisa del estado interno del objeto.
  - Se utiliza cuando se llama a `repr(objeto)` o en el intérprete interactivo.

- **Diferencias entre __str__ y __repr__**:
  - `__str__` está orientado a mostrar una salida legible para usuarios, mientras que `__repr__` está pensado para mostrar detalles más técnicos que ayudan en el desarrollo o depuración.
  - Si `__str__` no está definido, Python usará `__repr__` como fallback.
"""

"""
Explicación sobre los métodos Getters y Setters:

- **Getters**: 
  - Se utilizan para obtener el valor de un atributo privado. 
  - En Python, el decorador `@property` permite definir un método getter sin necesidad de llamarlo explícitamente como un método.
  
- **Setters**: 
  - Se utilizan para establecer o cambiar el valor de un atributo privado.
  - En Python, el decorador `@setter` se asocia con el getter correspondiente y permite modificar el valor del atributo de manera controlada.

- **Uso correcto**: 
  - Es importante seguir esta convención para mantener los atributos encapsulados y proporcionar una forma controlada de acceder o modificar sus valores.
"""
