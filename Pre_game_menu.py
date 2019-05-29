'''!@brief Файл вызова окна с вводом никнеймов
'''

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
        self.label.setPixmap(QtGui.QPixmap("Before_the_game_png.png"))
        self.label.setObjectName("label")
        self.Play_the_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_the_game_button.setGeometry(QtCore.QRect(370, 680, 700, 181))
        self.Play_the_game_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Play_button_after_play_was_pressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_the_game_button.setIcon(icon)
        self.Play_the_game_button.setIconSize(QtCore.QSize(700, 181))
        self.Play_the_game_button.setFlat(True)
        self.Play_the_game_button.setObjectName("Play_the_game_button")
        self.First_player_nickname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.First_player_nickname_text.setGeometry(QtCore.QRect(920, 188, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.First_player_nickname_text.setFont(font)
        self.First_player_nickname_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.First_player_nickname_text.setObjectName("First_player_nickname_text")
        self.Second_player_nickname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Second_player_nickname_text.setGeometry(QtCore.QRect(920, 350, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Second_player_nickname_text.setFont(font)
        self.Second_player_nickname_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Second_player_nickname_text.setObjectName("Second_player_nickname_text")
        self.Current_word_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Current_word_text.setGeometry(QtCore.QRect(770, 500, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Current_word_text.setFont(font)
        self.Current_word_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Current_word_text.setObjectName("Current_word_text")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(0, 0, 356, 91))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon1)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(381, 91))
        self.Back_to_main_menu_button.setFlat(True)
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


