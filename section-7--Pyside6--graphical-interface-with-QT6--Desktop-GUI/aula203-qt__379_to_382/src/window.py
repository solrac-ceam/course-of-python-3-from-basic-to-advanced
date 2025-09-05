# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 681, 130))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelResult = QLabel(self.verticalLayoutWidget)
        self.labelResult.setObjectName(u"labelResult")
        font = QFont()
        font.setPointSize(40)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelResult)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelName = QLabel(self.verticalLayoutWidget)
        self.labelName.setObjectName(u"labelName")
        font1 = QFont()
        font1.setPointSize(30)
        self.labelName.setFont(font1)

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setFont(font1)

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.sendButton = QPushButton(self.verticalLayoutWidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setFont(font1)

        self.gridLayout.addWidget(self.sendButton, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o tem nada aqui", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Seu Nome:", None))
        self.nameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

