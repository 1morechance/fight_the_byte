# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/Work/GUI/game_process_menu.ui'
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
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Game_process_png.png"))
        self.label.setObjectName("label")
        self.Next_turn_button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_turn_button.setGeometry(QtCore.QRect(580, 40, 281, 81))
        self.Next_turn_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_turn_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Next_turn_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_turn_button.setIcon(icon)
        self.Next_turn_button.setIconSize(QtCore.QSize(571, 111))
        self.Next_turn_button.setCheckable(True)
        self.Next_turn_button.setChecked(True)
        self.Next_turn_button.setFlat(False)
        self.Next_turn_button.setObjectName("Next_turn_button")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon1)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(291, 81))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        self.First_card = QtWidgets.QPushButton(self.centralwidget)
        self.First_card.setGeometry(QtCore.QRect(560, 300, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.First_card.setFont(font)
        self.First_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.First_card.setText("")
        self.First_card.setIconSize(QtCore.QSize(321, 51))
        self.First_card.setFlat(True)
        self.First_card.setObjectName("First_card")
        self.Second_card = QtWidgets.QPushButton(self.centralwidget)
        self.Second_card.setGeometry(QtCore.QRect(560, 360, 321, 51))
        self.Second_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Second_card.setFlat(True)
        self.Second_card.setObjectName("Second_card")
        self.Third_card = QtWidgets.QPushButton(self.centralwidget)
        self.Third_card.setGeometry(QtCore.QRect(560, 420, 321, 51))
        self.Third_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Third_card.setFlat(True)
        self.Third_card.setObjectName("Third_card")
        self.Fourth_card = QtWidgets.QPushButton(self.centralwidget)
        self.Fourth_card.setGeometry(QtCore.QRect(560, 480, 321, 51))
        self.Fourth_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Fourth_card.setFlat(True)
        self.Fourth_card.setObjectName("Fourth_card")
        self.Fith_card = QtWidgets.QPushButton(self.centralwidget)
        self.Fith_card.setGeometry(QtCore.QRect(560, 540, 321, 51))
        self.Fith_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Fith_card.setFlat(True)
        self.Fith_card.setObjectName("Fith_card")
        self.Sixth_card = QtWidgets.QPushButton(self.centralwidget)
        self.Sixth_card.setGeometry(QtCore.QRect(560, 600, 321, 51))
        self.Sixth_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sixth_card.setFlat(True)
        self.Sixth_card.setObjectName("Sixth_card")
        self.Seventh_card = QtWidgets.QPushButton(self.centralwidget)
        self.Seventh_card.setGeometry(QtCore.QRect(560, 660, 321, 51))
        self.Seventh_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Seventh_card.setFlat(True)
        self.Seventh_card.setObjectName("Seventh_card")
        self.Eith_card = QtWidgets.QPushButton(self.centralwidget)
        self.Eith_card.setGeometry(QtCore.QRect(560, 720, 321, 51))
        self.Eith_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Eith_card.setFlat(True)
        self.Eith_card.setObjectName("Eith_card")
        self.First_player_label = QtWidgets.QLabel(self.centralwidget)
        self.First_player_label.setGeometry(QtCore.QRect(110, 220, 351, 591))
        self.First_player_label.setText("")
        self.First_player_label.setObjectName("First_player_label")
        self.Second_player_label = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_label.setGeometry(QtCore.QRect(1039, 215, 351, 601))
        self.Second_player_label.setText("")
        self.Second_player_label.setObjectName("Second_player_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


