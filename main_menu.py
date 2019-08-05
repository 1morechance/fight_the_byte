'''!@brief Файл с главным меню игры

'''

# Файлы с префиксом T адаптированы под машину пользователя

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import tkinter


def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    # width, height = original_image.size
 
    resized_image = original_image.resize(size)
    # width, height = resized_image.size

    resized_image.save(output_image_path)


r = tkinter.Tk()
width = r.winfo_screenwidth()
height = r.winfo_screenheight()

class Ui_MainWindow(object):
    '''!@brief Класс главного окна игры, содержащий все необходимые виджеты
        
    '''
    def setupUi(self, MainWindow):
        '''!@brief Фукнция, расставляющая виджеты по экрану

        '''
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(width, height)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setText("")

        resize_image("Menu_png.png", "T_Menu_png.png", (width, height))
        new_button_width = (width / 1440) * 571 # Изменение ширины кнопки
        new_button_height = (height / 900) * 111 # Изменение высоты кнопки
        

        self.label.setPixmap(QtGui.QPixmap("T_Menu_png.png"))
        self.label.setObjectName("label")

        self.Play_button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_button.setGeometry(QtCore.QRect((width - new_button_width) / 2, 240 * (height / 900), new_button_width, new_button_height))
        font = QtGui.QFont()
        font.setPointSize(47)
        self.Play_button.setFont(font)
        self.Play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Play_button.setMouseTracking(False)
        self.Play_button.setText("")
        icon = QtGui.QIcon()

        resize_image("Play_button_png.png", "T_Play_button_png.png", (int(new_button_width), int(new_button_height)))

        icon.addPixmap(QtGui.QPixmap("T_Play_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_button.setIcon(icon)
        self.Play_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Play_button.setCheckable(False)
        self.Play_button.setChecked(False)
        self.Play_button.setAutoRepeat(False)
        self.Play_button.setAutoExclusive(False)
        self.Play_button.setFlat(False)
        self.Play_button.setObjectName("Play_button")

        resize_image("Settings_button_png.png", "T_Settings_button_png.png", (int(new_button_width), int(new_button_height)))

        self.Settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_button.setGeometry(QtCore.QRect((width - new_button_width) / 2, 460 * (height / 900), new_button_width, new_button_height))
        self.Settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("T_Settings_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_button.setIcon(icon1)
        self.Settings_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Settings_button.setFlat(False)
        self.Settings_button.setObjectName("Settings_button")

        resize_image("Rules_button_png.png", "T_Rules_button_png.png", (int(new_button_width), int(new_button_height)))

        self.Rules_button = QtWidgets.QPushButton(self.centralwidget)
        self.Rules_button.setGeometry(QtCore.QRect((width - new_button_width) / 2, 690 * (height / 900), new_button_width, new_button_height))
        self.Rules_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rules_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("T_Rules_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rules_button.setIcon(icon2)
        self.Rules_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Rules_button.setFlat(False)
        self.Rules_button.setObjectName("Rules_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''!@biref ретранслирует интерфейс

        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


