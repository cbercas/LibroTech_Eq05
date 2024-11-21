# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import img.background_rc
import img.candado_rc
import img.correo_rc
import img.usuario_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	border-image: url(:/cct/background.jpg);\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.vs_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs_1, 3, 1, 1, 1)

        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_2, 2, 2, 1, 1)

        self.vs_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs_2, 1, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(420, 450))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"    background-color: rgba(245, 232, 208, 0.9);\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 5px;\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    color: #4A3D2D;\n"
"	border: 1px solid rgba(0, 0, 0, 0.5);\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 0.7);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #C69C8D;\n"
"    background-color: rgba(255, 255, 255, 1);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(220, 180, 150, 0.9);\n"
"    border: 2px solid rgba(0, 0, 0, 0.3);\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    color: #ffffff;\n"
"    font-family: \"Arial\";\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 160, 130, 1);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 140, 100, 1);\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    fon"
                        "t-size: 13px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6D4C41;\n"
"	border: 1px solid black;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.hs_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.hs_3, 0, 0, 1, 1)

        self.password_label = QLabel(self.widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(25, 25))
        self.password_label.setStyleSheet(u"border-image: url(:/cct/candado.png);")

        self.gridLayout_3.addWidget(self.password_label, 3, 3, 1, 1)

        self.terms_checkbox = QCheckBox(self.widget)
        self.terms_checkbox.setObjectName(u"terms_checkbox")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setUnderline(False)
        self.terms_checkbox.setFont(font)
        self.terms_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.terms_checkbox.setAutoFillBackground(False)
        self.terms_checkbox.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(0, 0, 0);\n"
"	height: 15px;\n"
"	padding: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6D4C41;\n"
"	border: 1px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.terms_checkbox, 5, 1, 1, 3)

        self.user_icon = QLabel(self.widget)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setMaximumSize(QSize(25, 25))
        self.user_icon.setStyleSheet(u"border-image: url(:/cct/usuario.png);\n"
"")

        self.gridLayout_3.addWidget(self.user_icon, 1, 3, 1, 1)

        self.register_button = QPushButton(self.widget)
        self.register_button.setObjectName(u"register_button")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.register_button.setFont(font1)
        self.register_button.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.register_button, 6, 1, 1, 3)

        self.user_editline = QLineEdit(self.widget)
        self.user_editline.setObjectName(u"user_editline")
        self.user_editline.setMaximumSize(QSize(16777215, 16777215))
        self.user_editline.setStyleSheet(u"")
        self.user_editline.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.user_editline, 1, 1, 1, 2)

        self.tittle_label = QLabel(self.widget)
        self.tittle_label.setObjectName(u"tittle_label")
        self.tittle_label.setMinimumSize(QSize(0, 0))
        self.tittle_label.setMaximumSize(QSize(16777215, 80))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setBold(True)
        self.tittle_label.setFont(font2)
        self.tittle_label.setStyleSheet(u"font-size: 30px;\n"
"font-weight: bold;\n"
"color: #4E342E;\n"
"text-align: center;\n"
"")
        self.tittle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.tittle_label, 0, 1, 1, 3)

        self.password_editline = QLineEdit(self.widget)
        self.password_editline.setObjectName(u"password_editline")
        self.password_editline.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.password_editline, 3, 1, 1, 2)

        self.email_icon = QLabel(self.widget)
        self.email_icon.setObjectName(u"email_icon")
        self.email_icon.setStyleSheet(u"border-image: url(:/cct/carta.png);")

        self.gridLayout_3.addWidget(self.email_icon, 2, 3, 1, 1)

        self.email_editline = QLineEdit(self.widget)
        self.email_editline.setObjectName(u"email_editline")
        self.email_editline.setMaximumSize(QSize(16777215, 16777215))
        self.email_editline.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.email_editline, 2, 1, 1, 2)

        self.hs_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.hs_4, 2, 4, 1, 1)

        self.password_confirm_editline = QLineEdit(self.widget)
        self.password_confirm_editline.setObjectName(u"password_confirm_editline")
        self.password_confirm_editline.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.password_confirm_editline, 4, 1, 1, 2)

        self.password_confirm_label = QLabel(self.widget)
        self.password_confirm_label.setObjectName(u"password_confirm_label")
        self.password_confirm_label.setMaximumSize(QSize(25, 25))
        self.password_confirm_label.setStyleSheet(u"border-image: url(:/cct/candado.png);")

        self.gridLayout_3.addWidget(self.password_confirm_label, 4, 3, 1, 1)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setFont(font1)

        self.gridLayout_3.addWidget(self.login_button, 7, 1, 1, 3)


        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_1, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setStyleSheet(u"background-color: rgb(165, 125, 91);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(1004, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(20, 20))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/prueba/minus-sign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(20, 20))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/prueba/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(193, 161, 136);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"img/prueba/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.password_editline.setPlaceholderText("Escriba su contraseña") 
        self.user_editline.setPlaceholderText("Escriba su nombre de usuario")
        self.password_confirm_editline.setPlaceholderText("Confirme su contraseña")
        self.email_editline.setPlaceholderText("Escriba su correo electrónico")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.password_label.setText("")
        self.terms_checkbox.setText(QCoreApplication.translate("MainWindow", u"Acepto los t\u00e9rminos y condiciones", None))
        self.user_icon.setText("")
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.tittle_label.setText(QCoreApplication.translate("MainWindow", u"Crear una cuenta", None))
        self.email_icon.setText("")
        self.password_confirm_label.setText("")
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
    # retranslateUi

