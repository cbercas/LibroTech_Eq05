import unittest
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Signal

class SearchButton(QWidget):
    search_submitted = Signal(str)  # Señal que emite el texto cuando se hace clic en el botón

    def __init__(self):
        super().__init__()

        self.search_input = QLineEdit(self)  # Campo de entrada
        self.search_button = QPushButton("Buscar", self)  # Botón de búsqueda
        self.search_button.clicked.connect(self.emit_search)  # Conectar el clic del botón a la función

        layout = QVBoxLayout(self)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)

    def emit_search(self):
        """Emite la señal con el texto del campo de entrada cuando se hace clic en el botón"""
        self.search_submitted.emit(self.search_input.text())

# Instancia global de QApplication para evitar errores de múltiples instancias
app = QApplication([])

class TestSearchButton(unittest.TestCase):
    def setUp(self):
        """Configurar el entorno para las pruebas"""
        self.search_button_widget = SearchButton()  # Instanciar el widget que contiene el botón de búsqueda

    def tearDown(self):
        """Limpiar después de cada prueba"""
        self.search_button_widget.deleteLater()  # Eliminar el widget para evitar fugas de memoria

    def test_search_button_click(self):
        """Probar que al hacer clic en el botón de búsqueda se emite la señal correctamente"""
        # Crear un 'spy' para capturar la señal
        result = []

        def spy(value):
            result.append(value)

        # Conectar la señal search_submitted al spy
        self.search_button_widget.search_submitted.connect(spy)

        # Establecer un texto en el campo de entrada
        self.search_button_widget.search_input.setText("Don Quijote")

        # Hacer clic en el botón de búsqueda
        self.search_button_widget.search_button.click()

        # Verificar que la señal fue emitida con el valor correcto
        self.assertEqual(result, ["Don Quijote"])

if __name__ == "__main__":
    unittest.main()
