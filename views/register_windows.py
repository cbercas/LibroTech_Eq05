from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication  # Importar QMessageBox para mostrar mensajes de error
from PySide6.QtCore import Slot, Signal  # Importar Slot para la conexión de señales y slots
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from views.qt.register import Ui_MainWindow  # Importar la clase generada a partir del archivo .ui
from controllers.usuario_controller import UsuarioController  # Importar el controlador para manejar las operaciones de registro y validación del usuario

class RegisterWindow(QMainWindow):
    volver_signal = Signal()

    def __init__(self, parent=None):
        """
        Constructor de la clase RegisterWindow.
        
        :param parent: Ventana padre (en este caso, la ventana de login).
        """
        super().__init__(parent)  # Llamar al constructor de la clase base QMainWindow
        self.ui = Ui_MainWindow()  # Crear una instancia de la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz de usuario con el método setupUi

        # Conecta el botón "Login" a una señal
        self.ui.login_button.clicked.connect(self.enviar_volver_signal)

        # Conectar el botón "Crear Cuenta" al método para registrar un nuevo usuario
        self.ui.register_button.clicked.connect(self.slot_on_boton_crear_clicked)

        # Instanciar el controlador de usuarios que manejará las operaciones de validación, creación y gestión del usuario en la base de datos
        self.usuario_controller = UsuarioController()  # Este controlador interactúa con el modelo de usuario y la base de datos

        self.setWindowIcon(QIcon("img/library64.ico"))

        # Bandera para controlar el cierre del programa
        self.exit_program = True

    def enviar_volver_signal(self):
        """Emitir señal para volver a la ventana de login."""
        self.exit_program = False  # No salir del programa al cerrar
        self.volver_signal.emit()
        self.close()

    def closeEvent(self, event):
        """Controlar el comportamiento del cierre."""
        if self.exit_program:
            QApplication.quit()
        else:
            super().closeEvent(event)
        
    @Slot()
    def slot_on_boton_login_clicked(self):
        """
        Método que se ejecuta cuando se pulsa el botón 'Login'.
        Oculta la ventana de registro y muestra la ventana de login.
        """
        # Guardar la posición actual de la ventana de registro
        current_position = self.pos()
        
        # Ocultar la ventana de registro
        self.hide()

        # Llamar al método de la ventana de login para mostrarla nuevamente
        if self.parent() is not None:  # Verificar que existe una ventana padre
            self.parent().show()  # Mostrar la ventana de login
            self.parent().move(current_position)  # Mover la ventana de login a la posición actual

    @Slot()
    def slot_on_boton_crear_clicked(self):
        """
        Método para crear una cuenta nueva.
        Verifica que las contraseñas coinciden y luego llama al controlador para registrar al usuario.
        """
        # Obtener los datos ingresados por el usuario en los campos de texto
        email = self.ui.email_editline.text()
        nombre_usuario = self.ui.user_editline.text()
        password = self.ui.password_editline.text()
        password_confirmada = self.ui.password_confirm_editline.text()

        # Verificar si hay campos vacíos
        if not email or not nombre_usuario or not password or not password_confirmada:
            QMessageBox.warning(self, "Error de Registro", "Todos los campos son obligatorios. Por favor, completa todos los campos.")
            return

        # Verificar si las contraseñas coinciden
        if password != password_confirmada: 
            QMessageBox.warning(self, "Error de Registro", "Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")
            return
        
        # Verificar si los términos y condiciones están aceptados
        if not self.ui.terms_checkbox.isChecked():
            QMessageBox.warning(self, "Error de Registro", "Debes aceptar los términos y condiciones para continuar.")
            return

        # Intentar registrar al usuario a través del controlador
        if self.usuario_controller.registrar_usuario(email, nombre_usuario, password, password_confirmada):
            print("Usuario creado con éxito")  # Mensaje en consola si el registro fue exitoso          
            self.hide()
            if self.parent() is not None:
                self.parent().show()  # Mostrar la ventana de login si el registro fue exitoso          
        else:
            print("Error al crear el usuario")  # Si hay algún error en el proceso de registro

# RegistroWindow
