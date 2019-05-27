# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktop/The_winner_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("The_winner_png.png"))
        self.label.setObjectName("label")
        self.Nickname_of_the_winner = QtWidgets.QLabel(self.centralwidget)
        self.Nickname_of_the_winner.setGeometry(QtCore.QRect(340, 330, 541, 121))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.Nickname_of_the_winner.setFont(font)
        self.Nickname_of_the_winner.setText("")
        self.Nickname_of_the_winner.setObjectName("Nickname_of_the_winner")
        self.Back_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_button.setGeometry(QtCore.QRect(420, 730, 572, 144))
        self.Back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Back_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_button.setIcon(icon)
        self.Back_button.setIconSize(QtCore.QSize(572, 144))
        self.Back_button.setFlat(True)
        self.Back_button.setObjectName("Back_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


