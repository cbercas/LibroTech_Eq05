from PySide6.QtWidgets import QMainWindow, QMessageBox, QSizeGrip  # Importar QMessageBox para mostrar mensajes de error
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve
from PySide6 import QtCore, QtGui
from views.qt.login import Ui_MainWindow
from views.register_windows import RegisterWindow
from views.home_windows import HomeWindow
from controllers.usuario_controller import UsuarioController


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configurar las banderas de la ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.setWindowOpacity(1)

        # Conectar los botones a sus funciones respectivas
        self.ui.login_button.clicked.connect(self.slot_on_button_login_clicked)
        self.ui.register_button.clicked.connect(self.slot_on_button_crear_cuenta_clicked)

        # Control barra de títulos
        self.ui.btn_minimize.clicked.connect(self.control_bt_minimizar)
        self.ui.btn_maximize.clicked.connect(self.control_bt_maximizar)
        self.ui.btn_close.clicked.connect(lambda: self.close())

        self.usuario_controller = UsuarioController()

        # Variable para almacenar la posición de la última ventana mostrada
        self.last_position = None

        # Guardamos el tamaño original de la ventana
        self.original_size = self.size()

        # SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

    def limpiar_inputs(self):
        """Limpia los campos de texto del formulario de inicio de sesión."""
        self.ui.email_editline.clear()
        self.ui.password_editline.clear()
        self.ui.remember_checkbox.setChecked(False)

    @Slot()
    def mostrar_login(self):
        """Muestra la ventana de login y limpia los inputs."""
        self.limpiar_inputs()
        self.show()

    @Slot()
    def slot_on_button_login_clicked(self):  
        print("Hemos pulsado el botón de login")
        name = self.ui.email_editline.text().strip()  # Usar .strip() para eliminar espacios
        password = self.ui.password_editline.text()

        # Verificar si los campos están vacíos
        if not name or not password:
            QMessageBox.warning(self, "Error de Login", "Por favor, completa todos los campos.")
            return

        # Verificar credenciales del usuario
        if self.usuario_controller.verificar_usuario(name, password):
            # Ocultar login y mostrar home
            self.hide()

            # Crear y configurar HomeWindow
            self.home_window = HomeWindow(login_window=self)

            # Mostrar HomeWindow
            self.home_window.show()
        else:
            QMessageBox.warning(self, "Error de Login", "Nombre de usuario o contraseña incorrectos.")  # Mensaje de error
            print("Error al iniciar sesión")

    @Slot()
    def slot_on_button_crear_cuenta_clicked(self):
        """Oculta la ventana de login y muestra la de registro en la última posición registrada"""
        print("Hemos pulsado el botón de registro")

        # Comprobar si ya existe una ventana de registro
        if hasattr(self, 'registro_window') and self.registro_window.isVisible():
            print("La ventana de registro ya está abierta.")
            return

        # Guardar la posición actual de login antes de ocultarla
        self.last_position = self.pos()
        self.hide()

        # Crear y configurar la ventana de registro
        self.registro_window = RegisterWindow()  # No pasamos `self` como parent
        self.registro_window.setWindowTitle("Registro - La Estantería de Don Librote")

        # Conectar la señal para volver a la ventana de login
        self.registro_window.volver_signal.connect(self.mostrar_login)

        # Mover la ventana de registro a la última posición registrada
        if self.last_position:
            self.registro_window.move(self.last_position)

        # Mostrar la ventana de registro
        self.registro_window.show()

        # Al cerrar registro, guardar su posición actual y volver a mostrar login
        #self.registro_window.destroyed.connect(self.update_position_and_show_login)

    @Slot()
    def update_position_and_show_login(self):
        """Actualiza la última posición registrada y vuelve a mostrar la ventana de login"""
        # Guardar la posición actual de la ventana de registro si está visible
        if self.registro_window:
            self.last_position = self.registro_window.pos()

        # Mover login a la última posición registrada y mostrarlo
        if self.last_position:
            self.move(self.last_position)

        self.show()

    def control_bt_minimizar(self):
            self.showMinimized()

    def control_bt_normal(self): 
        self.showNormal()
        self.ui.btn_maximize.show()

    def control_bt_maximizar(self): 
        if self.isMaximized():
            self.restore_window()
        else:
            self.showMaximized()

    def restore_window(self):
        self.resize(self.original_size)
        screen_geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        center_position = screen_geometry.center() - self.rect().center()
        self.move(center_position)
        self.showNormal()


    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not (self.ui.btn_minimize.underMouse() or self.ui.btn_maximize.underMouse() or self.ui.btn_close.underMouse()):
                self.clickPosition = event.globalPosition().toPoint()
                self.is_dragging = True
                self.was_maximized = self.isMaximized()
            else:
                self.is_dragging = False

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            # Restaurar ventana si estaba maximizada
            if self.was_maximized:
                self.restore_window()
                self.clickPosition = event.globalPosition().toPoint() - self.rect().topLeft()

            # Mover la ventana
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()

            # Detectar si la ventana se arrastra hacia los bordes
            screen_geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()
            cursor_position = event.globalPosition().toPoint()

            # Detectar borde superior (maximizar)
            if cursor_position.y() <= screen_geometry.top():
                self.showMaximized()
                self.is_dragging = False  # Detener el arrastre

            # Detectar borde izquierdo (ajustar a la mitad izquierda)
            elif cursor_position.x() <= screen_geometry.left():
                self.resize(screen_geometry.width() // 2, screen_geometry.height())
                self.move(screen_geometry.topLeft())
                self.is_dragging = False  # Detener el arrastre

            # Detectar borde derecho (ajustar a la mitad derecha)
            elif cursor_position.x() >= screen_geometry.right() - 1:
                self.resize(screen_geometry.width() // 2, screen_geometry.height())
                self.move(screen_geometry.right() - self.width(), screen_geometry.top())
                self.is_dragging = False  # Detener el arrastre

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = False
            self.was_maximized = False