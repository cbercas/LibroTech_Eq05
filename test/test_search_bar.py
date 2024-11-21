import unittest
from PySide6.QtWidgets import QApplication, QLineEdit
from Componentes_EQ05 import SearchBar  # Asegúrate de que el import sea correcto

# Crear una única instancia de QApplication para todas las pruebas
app = QApplication([])  # Mover QApplication fuera de las pruebas

class TestSearchBar(unittest.TestCase):
    def setUp(self):
        """Configurar el entorno para las pruebas"""
        self.search_bar = SearchBar()  # Instanciar el componente a probar

    def tearDown(self):
        """Limpiar después de cada prueba"""
        self.search_bar.deleteLater()  # Eliminar el widget para evitar fugas de memoria

    def test_search_input(self):
        """Prueba que la búsqueda emite la señal correctamente"""
        # Crear un 'spy' para conectar con la señal
        result = []

        def spy(value):
            result.append(value)

        self.search_bar.search_submitted.connect(spy)  # Conectar la señal
        self.search_bar.search_submitted.emit("Don Quijote")  # Emitir la señal

        self.assertEqual(result, ["Don Quijote"])  # Verificar que la señal envió el valor esperado

    def test_input_text(self):
        """Probar que el texto introducido es correcto"""
        self.search_bar.search_input.setText("Don Quijote")
        self.assertEqual(self.search_bar.search_input.text(), "Don Quijote")  # Verificar el texto

if __name__ == "__main__":
    unittest.main()
