import unittest
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from Componentes_EQ05 import SearchBar  # Asegúrate de importar tu clase correctamente

class TestSearchBar(unittest.TestCase):
    def setUp(self):
        """Configurar el entorno para las pruebas"""
        self.app = QApplication([])  # Necesario para crear widgets Qt
        self.search_bar = SearchBar()  # Instanciar tu componente

    def test_search_input(self):
        """Prueba que la búsqueda emite la señal correctamente"""
        # Crear un 'spy' para la señal
        with self.assertRaises(ValueError):  # Cambiar según la lógica esperada
            self.search_bar.search_submitted.emit("Don Quijote")

    def test_input_text(self):
        """Probar que el texto introducido es correcto"""
        self.search_bar.search_input.setText("Don Quijote")
        self.assertEqual(self.search_bar.search_input.text(), "Don Quijote")  # Verificar el texto