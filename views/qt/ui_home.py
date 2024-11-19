# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 30))
        self.frame_superior.setMaximumSize(QSize(16777215, 30))
        self.frame_superior.setStyleSheet(u"background-color: rgb(165, 125, 91);")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(533, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_settings = QPushButton(self.frame_superior)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(20, 20))
        font = QFont()
        font.setKerning(True)
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/prueba/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_settings)

        self.btn_minimize = QPushButton(self.frame_superior)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/prueba/minus-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_superior)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(20, 20))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"img/prueba/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_superior)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"img/prueba/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_principal)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_principal)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(42, 0))
        self.frame_menu.setMaximumSize(QSize(42, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        self.frame_menu.setFont(font1)
        self.frame_menu.setStyleSheet(u"background-color: rgb(212, 190, 157);")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_menu.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(30, 30))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(11)
        self.btn_menu.setFont(font2)
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 129, 99);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"img/prueba/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon4)
        self.btn_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_menu)

        self.btn_home = QPushButton(self.frame_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(30, 30))
        self.btn_home.setFont(font2)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 129, 99);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"img/prueba/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon5)
        self.btn_home.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_gestion_libros = QPushButton(self.frame_menu)
        self.btn_gestion_libros.setObjectName(u"btn_gestion_libros")
        self.btn_gestion_libros.setMinimumSize(QSize(30, 30))
        self.btn_gestion_libros.setFont(font2)
        self.btn_gestion_libros.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 129, 99);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"img/prueba/libro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_gestion_libros.setIcon(icon6)
        self.btn_gestion_libros.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_gestion_libros)

        self.verticalSpacer = QSpacerItem(20, 322, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_cerrar_sesion = QPushButton(self.frame_menu)
        self.btn_cerrar_sesion.setObjectName(u"btn_cerrar_sesion")
        self.btn_cerrar_sesion.setMinimumSize(QSize(30, 30))
        self.btn_cerrar_sesion.setFont(font2)
        self.btn_cerrar_sesion.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 129, 99);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"img/prueba/cerrarSesion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar_sesion.setIcon(icon7)
        self.btn_cerrar_sesion.setIconSize(QSize(22, 22))

        self.verticalLayout_2.addWidget(self.btn_cerrar_sesion)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_posterior = QFrame(self.frame_principal)
        self.frame_posterior.setObjectName(u"frame_posterior")
        self.frame_posterior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_posterior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_posterior)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_contenido = QFrame(self.frame_posterior)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenido)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_2 = QPushButton(self.page_home)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setStyleSheet(u"background-color: rgb(170, 255, 127);")

        self.verticalLayout_6.addWidget(self.btn_2)

        self.stackedWidget.addWidget(self.page_home)
        self.page_gestion_libros = QWidget()
        self.page_gestion_libros.setObjectName(u"page_gestion_libros")
        self.verticalLayout_5 = QVBoxLayout(self.page_gestion_libros)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_contenido_libros = QFrame(self.page_gestion_libros)
        self.frame_contenido_libros.setObjectName(u"frame_contenido_libros")
        self.frame_contenido_libros.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido_libros.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_contenido_libros)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_buscador = QFrame(self.frame_contenido_libros)
        self.frame_buscador.setObjectName(u"frame_buscador")
        self.frame_buscador.setMaximumSize(QSize(16777215, 70))
        self.frame_buscador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buscador.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_buscador)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 30, -1, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame_buscador)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_buscador)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    padding: 4px;\n"
"    font-family: \"Arial\";\n"
"    font-size: 9px;\n"
"    color: #4A3D2D;\n"
"	border: 1px solid rgba(0, 0, 0, 0.5);\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #C69C8D;\n"
"    background-color: rgba(255, 255, 255, 1);  \n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_buscador)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"img/prueba/buscar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_buscador)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(25, 25))
        self.pushButton_2.setMaximumSize(QSize(25, 25))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"img/prueba/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.frame_buscador)

        self.frame_listView = QFrame(self.frame_contenido_libros)
        self.frame_listView.setObjectName(u"frame_listView")
        self.frame_listView.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_listView.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_listView)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(31, 30, 30, 30)
        self.label_libros_almacenados = QLabel(self.frame_listView)
        self.label_libros_almacenados.setObjectName(u"label_libros_almacenados")
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_libros_almacenados.setFont(font4)
        self.label_libros_almacenados.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_libros_almacenados.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_libros_almacenados)

        self.frame_separador = QFrame(self.frame_listView)
        self.frame_separador.setObjectName(u"frame_separador")
        self.frame_separador.setMinimumSize(QSize(0, 0))
        self.frame_separador.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_separador.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_separador)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.line_2 = QFrame(self.frame_separador)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.horizontalSpacer_5 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.frame_separador)

        self.tableView = QTableView(self.frame_listView)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.tableView)


        self.verticalLayout_7.addWidget(self.frame_listView)


        self.verticalLayout_5.addWidget(self.frame_contenido_libros)

        self.stackedWidget.addWidget(self.page_gestion_libros)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_contenido)

        self.frame_config = QFrame(self.frame_posterior)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setMinimumSize(QSize(0, 0))
        self.frame_config.setMaximumSize(QSize(0, 16777215))
        self.frame_config.setStyleSheet(u"background-color: rgb(212, 190, 157);")
        self.frame_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_config)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.label_config = QLabel(self.frame_config)
        self.label_config.setObjectName(u"label_config")
        font5 = QFont()
        font5.setFamilies([u"Tahoma"])
        font5.setPointSize(12)
        self.label_config.setFont(font5)
        self.label_config.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_config.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_config)

        self.line = QFrame(self.frame_config)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.btn_idioma = QPushButton(self.frame_config)
        self.btn_idioma.setObjectName(u"btn_idioma")
        self.btn_idioma.setMinimumSize(QSize(30, 30))
        self.btn_idioma.setFont(font2)
        self.btn_idioma.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"	text-align: left;\n"
"    padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 129, 99);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"img/prueba/idioma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_idioma.setIcon(icon10)
        self.btn_idioma.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_idioma)

        self.verticalSpacer_2 = QSpacerItem(20, 343, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_config)


        self.horizontalLayout.addWidget(self.frame_posterior)


        self.verticalLayout.addWidget(self.frame_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_settings.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"   Ocultar Men\u00fa", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"   P\u00e1gina de Inicio", None))
        self.btn_gestion_libros.setText(QCoreApplication.translate("MainWindow", u"   Gesti\u00f3n de Libros", None))
        self.btn_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"   Cerrar Sesi\u00f3n", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"Ventana Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00bfQuieres algo en especial?", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label_libros_almacenados.setText(QCoreApplication.translate("MainWindow", u"Libros almacenados en la Base de Datos", None))
        self.label_config.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btn_idioma.setText(QCoreApplication.translate("MainWindow", u"   Idioma", None))
    # retranslateUi

