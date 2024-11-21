# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(410, 450))
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
"    background-color: rgba(255, 255, 255, 1);  \n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(220, 180, 150, 0.9);\n"
"    border: 2px solid rgba(0, 0, 0, 0.3); \n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #ffffff; \n"
"    font-family: \"Arial\"; \n"
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
""
                        "    font-size: 13px;\n"
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
        self.password_editline = QLineEdit(self.widget)
        self.password_editline.setObjectName(u"password_editline")
        self.password_editline.setMaximumSize(QSize(16777215, 16777215))
        self.password_editline.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_editline.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.password_editline, 2, 1, 1, 3)

        self.hs_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.hs_1, 0, 0, 1, 1)

        self.password_icon = QLabel(self.widget)
        self.password_icon.setObjectName(u"password_icon")
        self.password_icon.setMaximumSize(QSize(25, 25))
        self.password_icon.setStyleSheet(u"border-image: url(:/cct/candado.png);")

        self.gridLayout_3.addWidget(self.password_icon, 2, 4, 1, 1)

        self.hs_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.hs_2, 2, 5, 1, 1)

        self.email_editline = QLineEdit(self.widget)
        self.email_editline.setObjectName(u"email_editline")
        self.email_editline.setMaximumSize(QSize(16777215, 16777215))
        self.email_editline.setStyleSheet(u"")
        self.email_editline.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.email_editline, 1, 1, 1, 3)

        self.remember_checkbox = QCheckBox(self.widget)
        self.remember_checkbox.setObjectName(u"remember_checkbox")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.remember_checkbox.setFont(font)
        self.remember_checkbox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.remember_checkbox.setTristate(False)

        self.gridLayout_3.addWidget(self.remember_checkbox, 4, 1, 1, 1)

        self.correo_icon = QLabel(self.widget)
        self.correo_icon.setObjectName(u"correo_icon")
        self.correo_icon.setMaximumSize(QSize(30, 30))
        self.correo_icon.setStyleSheet(u"border-image: url(:/cct/carta.png);\n"
"")

        self.gridLayout_3.addWidget(self.correo_icon, 1, 4, 1, 1)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.login_button.setFont(font1)

        self.gridLayout_3.addWidget(self.login_button, 5, 1, 1, 4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"font-size: 30px;\n"
"font-weight: bold;\n"
"color: #4E342E;\n"
"text-align: center;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 4)

        self.forgot_password_label = QLabel(self.widget)
        self.forgot_password_label.setObjectName(u"forgot_password_label")
        self.forgot_password_label.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setUnderline(True)
        self.forgot_password_label.setFont(font3)
        self.forgot_password_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #A0522D;\n"
"}")

        self.gridLayout_3.addWidget(self.forgot_password_label, 4, 3, 1, 2)

        self.register_button = QPushButton(self.widget)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setFont(font1)

        self.gridLayout_3.addWidget(self.register_button, 6, 1, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)

        self.hs_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_3, 2, 2, 1, 1)

        self.hs_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.hs_4, 2, 0, 1, 1)

        self.vs2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs2, 1, 1, 1, 1)

        self.vs1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs1, 3, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"background-color: rgb(165, 125, 91);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(974, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.email_editline.setPlaceholderText("Escriba su correo electrónico")
        self.password_editline.setPlaceholderText("Escriba su contraseña")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.password_icon.setText("")
        self.remember_checkbox.setText(QCoreApplication.translate("MainWindow", u"Recu\u00e9rdame", None))
        self.correo_icon.setText("")
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.forgot_password_label.setText(QCoreApplication.translate("MainWindow", u"\u00bfOlvidaste tu contrase\u00f1a?", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
    # retranslateUi

