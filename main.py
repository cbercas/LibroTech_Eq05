from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from views.login_windows import LoginWindow
import models.inicializacion_db as initDB
import sys
import ctypes

# ID para que la app tenga un icono personalizado en la barra de tareas de windows
myappid = 'Proyecto_Equipo05'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainController:
    def __init__(self):
        # Crear la instancia de la aplicación
        self.app = QApplication(sys.argv)
        
        # Crear la ventana de login y configurarla
        self.login_window = LoginWindow() # Instanciar directamente LoginWindow (que hereda de QMainWindow)

        # Configurar ícono y título de la ventana de login
        self.login_window.setWindowIcon(QIcon("img/library64.ico"))
        self.login_window.setWindowTitle("Login - La Estantería de Don Librote")

        # Mostrar la ventana de login al iniciar
        self.login_window.show()

    # Método para ejecutar la aplicación
    def run(self):
        sys.exit(self.app.exec())

# Código principal
if __name__ == "__main__":
    # Inicializar la base de datos antes de iniciar la ventana
    initDB.init_db()
    
    # Crear el controlador principal y ejecutar la aplicación
    controller = MainController()
    controller.run()
