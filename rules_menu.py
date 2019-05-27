'''!@brief Файл с выводом правил игры
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    '''!@brief Открывает правила игры

    '''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Rules_png.png"))
        self.label.setObjectName("label")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(20, 30, 371, 91))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(561, 91))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


