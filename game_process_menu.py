# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktop/work/develop/iu7-bachelors-2022-practice-2019-hungry-developers-develop/game_process_menu.ui'
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
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Game_process_png.png"))
        self.label.setObjectName("label")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(291, 81))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        self.Card0 = QtWidgets.QPushButton(self.centralwidget)
        self.Card0.setGeometry(QtCore.QRect(560, 220, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card0.setFont(font)
        self.Card0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card0.setFlat(True)
        self.Card0.setObjectName("Card0")
        self.Card1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card1.setGeometry(QtCore.QRect(560, 280, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card1.setFont(font)
        self.Card1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card1.setFlat(True)
        self.Card1.setObjectName("Card1")
        self.Card2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card2.setGeometry(QtCore.QRect(560, 340, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card2.setFont(font)
        self.Card2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card2.setFlat(True)
        self.Card2.setObjectName("Card2")
        self.Card3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card3.setGeometry(QtCore.QRect(560, 400, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card3.setFont(font)
        self.Card3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card3.setFlat(True)
        self.Card3.setObjectName("Card3")
        self.Card4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4.setGeometry(QtCore.QRect(560, 460, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card4.setFont(font)
        self.Card4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card4.setFlat(True)
        self.Card4.setObjectName("Card4")
        self.Card5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5.setGeometry(QtCore.QRect(560, 520, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card5.setFont(font)
        self.Card5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card5.setFlat(True)
        self.Card5.setObjectName("Card5")
        self.Card6 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6.setGeometry(QtCore.QRect(560, 580, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card6.setFont(font)
        self.Card6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card6.setFlat(True)
        self.Card6.setObjectName("Card6")
        self.Card7 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7.setGeometry(QtCore.QRect(560, 640, 321, 51))  # placement 
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Card7.setFont(font)
        self.Card7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card7.setFlat(True)
        self.Card7.setObjectName("Card7")
        self.First_player_label = QtWidgets.QLabel(self.centralwidget)
        self.First_player_label.setGeometry(QtCore.QRect(110, 160, 351, 591))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.First_player_label.setFont(font)
        self.First_player_label.setText("")
        self.First_player_label.setObjectName("First_player_label")
        self.Second_player_label = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_label.setGeometry(QtCore.QRect(1040, 160, 351, 601))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Second_player_label.setFont(font)
        self.Second_player_label.setText("")
        self.Second_player_label.setObjectName("Second_player_label")
        self.Refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh_button.setGeometry(QtCore.QRect(1070, 10, 281, 81))
        self.Refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Refresh_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Refresh_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_button.setIcon(icon1)
        self.Refresh_button.setIconSize(QtCore.QSize(281, 81))
        self.Refresh_button.setObjectName("Refresh_button")
        self.First_player_nickname = QtWidgets.QLabel(self.centralwidget)
        self.First_player_nickname.setGeometry(QtCore.QRect(130, 80, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.First_player_nickname.setFont(font)
        self.First_player_nickname.setText("")
        self.First_player_nickname.setObjectName("First_player_nickname")
        self.Second_player_nickname = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_nickname.setGeometry(QtCore.QRect(1090, 90, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Second_player_nickname.setFont(font)
        self.Second_player_nickname.setText("")
        self.Second_player_nickname.setObjectName("Second_player_nickname")
        self.Current_word = QtWidgets.QLabel(self.centralwidget)
        self.Current_word.setGeometry(QtCore.QRect(710, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.Current_word.setFont(font)
        self.Current_word.setText("")
        self.Current_word.setObjectName("Current_word")
        self.Output_label = QtWidgets.QLabel(self.centralwidget)
        self.Output_label.setGeometry(QtCore.QRect(460, 810, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Output_label.setFont(font)
        self.Output_label.setText("")
        self.Output_label.setObjectName("Output_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


