from views.qt.ui_home import *
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QPropertyAnimation, Qt, QEasingCurve
from PySide6.QtWidgets import QSizeGrip, QMessageBox
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from controllers.libros_controller import LibroController
from PySide6.QtGui import QStandardItem, QStandardItemModel
from Componentes_EQ05 import SearchButton, SearchBar, BackButton
import sys
import ctypes

# Establecer el identificador único de la aplicación
myappid = 'proyectoInterfaces.Equipo05'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self, login_window=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_libros()
                

        # Guardar referencia al login
        self.login_window = login_window

        # Configurar las banderas de la ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.setWindowOpacity(1)

        # Icono de la aplicación (opcional, ayuda en la barra de tareas)
        self.setWindowIcon(QIcon("img/library64.ico"))

        # Guardamos el tamaño original de la ventana
        self.original_size = self.size()

        # SizeGrip
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        # Acceder a las páginas
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_gestion_libros.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_gestion_libros))

        # Conectar el botón de cerrar sesión al método de confirmación
        self.ui.btn_cerrar_sesion.clicked.connect(self.confirmar_cerrar_sesion)

        # Control barra de títulos
        self.ui.btn_minimize.clicked.connect(self.control_bt_minimizar)
        self.ui.btn_maximize.clicked.connect(self.control_bt_maximizar)
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # Menu lateral
        self.ui.btn_menu.clicked.connect(self.mover_menu)

        # Configuración desplegable
        self.ui.btn_settings.clicked.connect(self.mover_configuracion)

        # Variable para controlar si la ventana está en modo arrastrando
        self.is_dragging = False
        self.was_maximized = False

        # Reemplazar el botón estándar con el botón personalizado
        self.custom_button = SearchButton("img/prueba/buscar.png")
        self.ui.horizontalLayout_4.replaceWidget(self.ui.pushButton, self.custom_button)
        self.ui.pushButton.deleteLater()  # Eliminar el widget antiguo
        self.custom_button.clicked.connect(self.on_search_button_clicked)

        # Reemplazar el lineEdit con la barra de búsqueda personalizada
        self.search_bar = SearchBar()
        self.ui.horizontalLayout_4.replaceWidget(self.ui.lineEdit, self.search_bar)
        self.ui.lineEdit.deleteLater()  # Eliminar el widget antiguo
        self.search_bar.search_submitted.connect(self.on_search)
        
        # Boton volver
        self.custom_buttonBack = BackButton("img/prueba/back.png")
        self.ui.horizontalLayout_4.replaceWidget(self.ui.pushButton_2, self.custom_buttonBack)
        self.ui.pushButton_2.deleteLater()  # Eliminar el widget antiguo
        self.custom_buttonBack.clicked.connect(self.on_back_button_clicked)
 
        

        print("vamos a cargar los libros")
        # Inicializar la lista de libros en listView_libros
        self.cargar_libros()
        
        
            
    def confirmar_cerrar_sesion(self):
        """Muestra un mensaje de confirmación antes de cerrar sesión."""
        respuesta = QMessageBox.question(
            self,
            "Confirmar Cerrar Sesión",
            "¿Estás seguro de que deseas cerrar sesión?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            self.cerrar_sesion()  # Llama al método para cerrar sesión

    def cerrar_sesion(self):
        """Cierra la sesión y vuelve a la ventana de login."""
        # Guardar la posición actual de HomeWindow
        if self.login_window:
            self.login_window.last_position = self.pos()

        self.close()  # Cerrar HomeWindow

        if self.login_window:
            self.login_window.show()  # Mostrar de nuevo la ventana de login

    def on_button_clicked(self):
        print("Botón con imagen presionado")

    def on_search(self, query):
        print(f"Búsqueda realizada: {query}")

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

    def mover_menu(self):
        width = self.ui.frame_menu.width()
        new_width = 175 if width == 42 else 42
        self.animacion = QPropertyAnimation(self.ui.frame_menu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(new_width)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

    def mover_configuracion(self):
        width = self.ui.frame_config.width()
        new_width = 120 if width == 0 else 0
        self.animacion_config = QPropertyAnimation(self.ui.frame_config, b'minimumWidth')
        self.animacion_config.setDuration(300)
        self.animacion_config.setStartValue(width)
        self.animacion_config.setEndValue(new_width)
        self.animacion_config.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion_config.start()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()
        # Detecta si la ventana estaba maximizada antes de mover
        if self.isMaximized():
            self.was_maximized = True
            self.showNormal()  # Minimiza cuando comienza el movimiento

        # Verificar si el clic fue en uno de los botones de la barra de título
        if self.ui.btn_minimize.underMouse() or self.ui.btn_maximize.underMouse() or self.ui.btn_close.underMouse():
            self.is_dragging = False  # No mover la ventana si es sobre un botón
        else:
            self.is_dragging = True  # Permitir mover la ventana si no es sobre un botón

    def mover_ventana(self, event):
        if self.is_dragging:
            # Si la ventana está siendo arrastrada, moverla con el ratón
            if self.isMaximized():
                if not self.is_dragging:
                    # Cuando el movimiento comienza mientras está maximizada, minimizamos la ventana
                    self.is_dragging = True
                self.move(event.globalPosition().toPoint() - self.clickPosition)
                event.accept()
            else:
                if event.buttons() == QtCore.Qt.LeftButton:
                    # Si la ventana no está maximizada, simplemente moverla
                    self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                    self.clickPosition = event.globalPosition().toPoint()
                    event.accept()

        # Condición para restaurar la ventana si se mueve cerca de la parte superior
        if event.globalPosition().toPoint().y() <= 20 and self.was_maximized:
            self.showMaximized()
            self.is_dragging = False

        # Cuando se suelta el ratón, restaurar la ventana al tamaño original
        if not event.buttons() & QtCore.Qt.LeftButton:
            if self.is_dragging:
                self.is_dragging = False
                self.was_maximized = False
                self.showNormal()
                
    
    def cargar_libros(self):
        """Obtiene los libros de la base de datos y los muestra en el listView."""
        
        print("He llegado a cargar libro.")  # Mensaje de error
        
        try:

        # Crear y configurar el modelo
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["Isbn", "Título", "Autor", "Género", "Publicación"])
            self.libro_controller = LibroController()
            libros = self.libro_controller.obtener_libros()
             
            ######
            # Configurar el modelo en el QTableView
            self.ui.tableView.setModel(model)

            # Configurar para que las filas se adapten al espacio disponible
            vertical_header = self.ui.tableView.verticalHeader()
            vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Las filas se estiran proporcionalmente

            # Ajustar columnas
            header = self.ui.tableView.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            # Ajustar filas
            vertical_header = self.ui.tableView.verticalHeader()
            vertical_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            # Ajustar columnas al contenido inicial
            self.ui.tableView.resizeColumnsToContents()

            # Configurar para que las columnas se adapten al espacio disponible
            header = self.ui.tableView.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Todas las columnas se estiran proporcionalmente   
            ############# 
            
            for libro in libros:
                fila = [
                    QStandardItem(str(libro.isbn)),
                    QStandardItem(libro.titulo),
                    QStandardItem(libro.autor),
                    QStandardItem(str(libro.genero)),
                    QStandardItem(str(libro.publicacion))
                ]
                for item in fila:
                    item.setTextAlignment(Qt.AlignCenter)  # Alinear contenido
                model.appendRow(fila)            

            # Configurar el modelo en listView_libros
            self.ui.tableView.setModel(model)
          
        finally:
            print("ERROR AL OBTENER LOS LIBROS")
 

    def on_search(self, search_text):
        """
        Filtra los libros en la tabla en función del texto ingresado en la barra de búsqueda.
        """
        print(f"Buscando: {search_text}")

        # Obtener todos los libros desde el controlador
        libros = self.libro_controller.obtener_libros()

        # Filtrar los libros por el texto ingresado
        libros_filtrados = [
            libro for libro in libros
            if search_text.lower() in libro.titulo.lower()  # Coincidencia insensible a mayúsculas
        ]

        # Actualizar la tabla con los libros filtrados
        self.mostrar_libros(libros_filtrados)

    def on_search_button_clicked(self):
        """
        Llamado cuando el botón de búsqueda es clickeado.
        """
        search_text = self.search_bar.search_input.text().strip()  # Acceder al QLineEdit dentro de SearchBar

        self.on_search(search_text)  # Llamar al método de búsqueda

    def mostrar_libros(self, libros):
        """
        Muestra una lista de libros en el QTableView.
        """
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Isbn", "Título", "Autor", "Género", "Publicación"])

        for libro in libros:
            fila = [
                QStandardItem(str(libro.isbn)),
                QStandardItem(libro.titulo),
                QStandardItem(libro.autor),
                QStandardItem(libro.genero),
                QStandardItem(str(libro.publicacion))
            ]
            for item in fila:
                item.setTextAlignment(Qt.AlignCenter)  # Alinear contenido al centro
            model.appendRow(fila)

        # Configurar el modelo en la tabla
        self.ui.tableView.setModel(model)

        # Ajustar las columnas automáticamente
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Ajustar la altura de las filas al contenido del texto
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) 
        

    def on_back_button_clicked(self):
        """
        Recarga la lista completa de libros cuando se hace clic en el botón "Volver".
        """
        self.cargar_libros()  # Recargar todos los libros
