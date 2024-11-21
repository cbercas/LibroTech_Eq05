import unittest
from PySide6.QtWidgets import QApplication, QPushButton, QWidget
from PySide6.QtCore import Signal

# Clase que contiene el botón de retroceso
class BackButton(QWidget):
    back_pressed = Signal()  # Señal que emite cuando se presiona el botón de retroceso

    def __init__(self):
        super().__init__()

        self.back_button = QPushButton("Volver", self)  # Botón de retroceso
        self.back_button.clicked.connect(self.emit_back)  # Conectar el clic del botón a la función

    def emit_back(self):
        """Emite la señal de retroceso cuando se hace clic en el botón"""
        self.back_pressed.emit()


# Instancia global de QApplication para evitar errores de múltiples instancias
app = QApplication([])

# Clase que contiene las pruebas unitarias
class TestBackButton(unittest.TestCase):
    def setUp(self):
        """Configurar el entorno para las pruebas"""
        self.back_button_widget = BackButton()  # Instanciar el widget que contiene el botón de retroceso

    def tearDown(self):
        """Limpiar después de cada prueba"""
        self.back_button_widget.deleteLater()  # Eliminar el widget para evitar fugas de memoria

    def test_back_button_click(self):
        """Probar que al hacer clic en el botón de retroceso se emite la señal correctamente"""
        # Crear un 'spy' para capturar la señal
        result = []

        def spy():
            result.append("Retroceso")

        # Conectar la señal back_pressed al spy
        self.back_button_widget.back_pressed.connect(spy)

        # Hacer clic en el botón de retroceso
        self.back_button_widget.back_button.click()

        # Verificar que la señal fue emitida
        self.assertEqual(result, ["Retroceso"])

# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == "__main__":
    unittest.main()
