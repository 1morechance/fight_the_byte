'''!@brief Файл с главным меню игры

'''

# Файлы с префиксом T адаптированы под машину пользователя

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import tkinter

# Никнеймы + ключевое слово
First_player_nickname = ''
Second_player_nickname = ''
Word = ''

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)

    resized_image = original_image.resize(size)

    resized_image.save(output_image_path)

r = tkinter.Tk()
width = r.winfo_screenwidth()
height = r.winfo_screenheight()

# Коэффициенты масштабирования
width_k = width / 1440
height_k = height / 900

class Ui_MainWindow(object):
    '''!@brief Класс главного окна игры, содержащий все необходимые виджеты
        
    '''
    def setupUi(self, MainWindow):
        '''!@brief Фукнция, расставляющая виджеты по экрану

        '''
        try:
            self.centralwidget.deleteLater()
        except AttributeError:
            pass    
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

        self.retranslateMain(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # -------------Main window Backend--------
    def setup_actions_main(self):
        self.Play_button.clicked.connect(self.to_pregame)
        self.Settings_button.clicked.connect(self.to_settings)
        self.Rules_button.clicked.connect(self.to_rules)

    def to_pregame(self):
        '''!@brief Функция вызова начала игры
        '''
        self.setup_Pre_Game(self)
        self.setup_actions_pregame()

    def to_settings(self):
        '''!@brief Функция вызова настроек игры
        '''
        self.dialog_settings.show()

    def to_rules(self):
        '''!@brief Функция вызова правил игры
        '''
        self.dialog_rules.show()

    # ------------------------------------------

    def setup_Pre_Game(self, MainWindow):

        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setText("")

        resize_image("Before_the_game_png.png" , "T_Before_the_game_png.png", (width, height))

        self.label.setPixmap(QtGui.QPixmap("T_Before_the_game_png.png"))
        self.label.setObjectName("label")

        self.Play_the_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_the_game_button.setGeometry(QtCore.QRect(width_k * 370, height_k * 680, width_k * 700, height_k * 181))
        self.Play_the_game_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Play_the_game_button.setText("")
        icon = QtGui.QIcon()

        resize_image("Play_button_after_play_was_pressed.png", "T_Play_button_after_play_was_pressed.png", (int(width_k * 700), int(height_k * 181)))

        icon.addPixmap(QtGui.QPixmap("T_Play_button_after_play_was_pressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_the_game_button.setIcon(icon)
        self.Play_the_game_button.setIconSize(QtCore.QSize(int(width_k * 700), int(height_k * 181)))
        self.Play_the_game_button.setFlat(True)
        self.Play_the_game_button.setObjectName("Play_the_game_button")

        self.First_player_nickname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.First_player_nickname_text.setGeometry(QtCore.QRect(width_k * 920, height_k * 188, width_k * 271, height_k * 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.First_player_nickname_text.setFont(font)
        self.First_player_nickname_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.First_player_nickname_text.setObjectName("First_player_nickname_text")
        self.Second_player_nickname_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Second_player_nickname_text.setGeometry(QtCore.QRect(width_k * 920, height_k * 350, width_k * 271, height_k * 61))
        font = QtGui.QFont()
        font.setPointSize(40)

        self.Second_player_nickname_text.setFont(font)
        self.Second_player_nickname_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Second_player_nickname_text.setObjectName("Second_player_nickname_text")
        self.Current_word_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Current_word_text.setGeometry(QtCore.QRect(width_k * 770, height_k * 500, width_k * 241, height_k * 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Current_word_text.setFont(font)
        self.Current_word_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Current_word_text.setObjectName("Current_word_text")

        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(width_k * 5, height_k * 10, width_k * 356, height_k * 91))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon1 = QtGui.QIcon()

        resize_image("Back_to_main_menu_button_png.png", "T_Back_to_main_menu_button_png.png", (int(width_k * 356), int(height_k * 91)))

        icon1.addPixmap(QtGui.QPixmap("T_Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon1)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(width_k * 356, height_k * 91))
        self.Back_to_main_menu_button.setFlat(True)
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslatePre(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_actions_pregame(self):
        # Кнопки предигрового меню
        self.Back_to_main_menu_button.clicked.connect(self.to_main)
        self.Play_the_game_button.clicked.connect(self.setup_game)

    def setup_game(self):
        '''@!brief Функция присваивания никнеймов
        '''
        global First_player_nickname
        First_player_nickname = self.First_player_nickname_text.toPlainText()
        global Second_player_nickname
        Second_player_nickname = self.Second_player_nickname_text.toPlainText()
        global Word
        Word = self.Current_word_text.toPlainText()
 
    def to_main(self):
        '''@!brief Функция закрытия Пре-окна
        '''
        self.setupUi(self)
        self.setup_actions_main()


    def retranslatePre(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def retranslateMain(self, MainWindow):
        '''!@biref ретранслирует интерфейс

        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


