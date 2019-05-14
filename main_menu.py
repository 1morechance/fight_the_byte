# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/Work/GUI/main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Menu_png.png"))
        self.label.setObjectName("label")
        self.Play_button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_button.setGeometry(QtCore.QRect(450, 240, 571, 111))
        font = QtGui.QFont()
        font.setPointSize(47)
        self.Play_button.setFont(font)
        self.Play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Play_button.setMouseTracking(False)
        self.Play_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Play_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_button.setIcon(icon)
        self.Play_button.setIconSize(QtCore.QSize(571, 111))
        self.Play_button.setCheckable(False)
        self.Play_button.setChecked(False)
        self.Play_button.setAutoRepeat(False)
        self.Play_button.setAutoExclusive(False)
        self.Play_button.setFlat(False)
        self.Play_button.setObjectName("Play_button")
        self.Settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_button.setGeometry(QtCore.QRect(450, 460, 571, 111))
        self.Settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Settings_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_button.setIcon(icon1)
        self.Settings_button.setIconSize(QtCore.QSize(571, 111))
        self.Settings_button.setFlat(False)
        self.Settings_button.setObjectName("Settings_button")
        self.Rules_button = QtWidgets.QPushButton(self.centralwidget)
        self.Rules_button.setGeometry(QtCore.QRect(450, 690, 571, 111))
        self.Rules_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rules_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Rules_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rules_button.setIcon(icon2)
        self.Rules_button.setIconSize(QtCore.QSize(571, 111))
        self.Rules_button.setFlat(False)
        self.Rules_button.setObjectName("Rules_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


