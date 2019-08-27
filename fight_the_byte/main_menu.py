'''!@brief Файл с главным меню игры

'''

# Файлы с префиксом T адаптированы под машину пользователя

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import tkinter
import vlc

melody = vlc.MediaPlayer("music/jose-gonzalez-crosses.mp3")

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

class Startup(object):

    # -----------------Main window frontend-------------------
    def setup_main(self, MainWindow):
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

        resize_image("graphics/Menu_png.png", "graphics/T_Menu_png.png", (width, height))
        new_button_width = (width / 1440) * 571 # Изменение ширины кнопки
        new_button_height = (height / 900) * 111 # Изменение высоты кнопки
        
        self.label.setPixmap(QtGui.QPixmap("graphics/T_Menu_png.png"))
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

        resize_image("graphics/Play_button_png.png", "graphics/T_Play_button_png.png", (int(new_button_width), int(new_button_height)))

        icon.addPixmap(QtGui.QPixmap("graphics/T_Play_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_button.setIcon(icon)
        self.Play_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Play_button.setCheckable(False)
        self.Play_button.setChecked(False)
        self.Play_button.setAutoRepeat(False)
        self.Play_button.setAutoExclusive(False)
        self.Play_button.setFlat(False)
        self.Play_button.setObjectName("Play_button")

        resize_image("graphics/Settings_button_png.png", "graphics/T_Settings_button_png.png", (int(new_button_width), int(new_button_height)))

        self.Settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_button.setGeometry(QtCore.QRect((width - new_button_width) / 2, 460 * (height / 900), new_button_width, new_button_height))
        self.Settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/T_Settings_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings_button.setIcon(icon1)
        self.Settings_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Settings_button.setFlat(False)
        self.Settings_button.setObjectName("Settings_button")

        resize_image("graphics/Rules_button_png.png", "graphics/T_Rules_button_png.png", (int(new_button_width), int(new_button_height)))

        self.Rules_button = QtWidgets.QPushButton(self.centralwidget)
        self.Rules_button.setGeometry(QtCore.QRect((width - new_button_width) / 2, 690 * (height / 900), new_button_width, new_button_height))
        self.Rules_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rules_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphics/T_Rules_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rules_button.setIcon(icon2)
        self.Rules_button.setIconSize(QtCore.QSize(new_button_width, new_button_height))
        self.Rules_button.setFlat(False)
        self.Rules_button.setObjectName("Rules_button")
        MainWindow.setCentralWidget(self.centralwidget)

    # -----------------------------------------------------


    # -------------Main window Backend---------------------
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
        self.setup_settings(self)
        self.setup_actions_settings()

    def to_rules(self):
        '''!@brief Функция вызова правил игры
        '''
        self.setup_rules(self)
        self.setup_actions_rules()

    # ----------------------------------------------------------------


    # -------------------Settings window frontend--------------------- 
    def setup_settings(self, MainWindow):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setText("")

        resize_image("graphics/Settings_png.png", "graphics/T_Settings_png.png", (width, height))

        self.label.setPixmap(QtGui.QPixmap("graphics/T_Settings_png.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(width_k * 890, height_k * 190, width_k * 100, height_k * 100))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()

        resize_image("graphics/Off_button_png.png", "graphics/T_Off_button_png.png", (int(width_k * 100), int(height_k * 100)))
        resize_image("graphics/On_button_png.png", "graphics/T_On_button_png.png", (int(width_k * 100), int(height_k * 100)))

        icon.addPixmap(QtGui.QPixmap("graphics/T_Off_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("graphics/T_On_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(width_k * 100, height_k * 100))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        '''
        try:
            if (not self.melody.is_playing()):
                self.pushButton.setChecked(False)
            else:
                self.pushButton.setChecked(True)
        except AttributeError:
            pass
        '''
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(width_k * 890, height_k * 410, width_k * 100, height_k * 100))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(width_k * 100, height_k * 100))
        self.pushButton_2.setCheckable(True)
        if (melody.is_playing()):
            self.pushButton_2.setChecked(True)
        else:
            self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(width_k * 20, height_k * 30, width_k * 361, height_k * 91))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon1 = QtGui.QIcon()

        resize_image("graphics/Back_to_main_menu_button_png.png", "graphics/T_Back_to_main_menu_button_png.png", (int(width_k * 361), int(height_k * 91)))

        icon1.addPixmap(QtGui.QPixmap("graphics/T_Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon1)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(width_k * 361, height_k * 91))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(width_k * 810, height_k * 670, width_k * 191, height_k * 51))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
    # ---------------------------------------------------------

    # ----------------Settings Window Backend------------------
    def setup_actions_settings(self):
        self.Back_to_main_menu_button.clicked.connect(self.to_main)
        self.pushButton_2.clicked.connect(self.music_check)
        self.pushButton.clicked.connect(self.clicks)

    def music_check(self):
        if (self.pushButton_2.isChecked()):
            melody.play()
        else:
            melody.pause()

    def clicks(self):
        pass
    
    # Возврат в главное меню - метод to_main общий для нескольких кнопок
    # ------------------------------------------------------------


    # ---------------Pre Game menu frontend-----------------------
    def setup_Pre_Game(self, MainWindow):

        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setText("")

        resize_image("graphics/Before_the_game_png.png" , "graphics/T_Before_the_game_png.png", (width, height))

        self.label.setPixmap(QtGui.QPixmap("graphics/T_Before_the_game_png.png"))
        self.label.setObjectName("label")

        self.Play_the_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.Play_the_game_button.setGeometry(QtCore.QRect(width_k * 370, height_k * 680, width_k * 700, height_k * 181))
        self.Play_the_game_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Play_the_game_button.setText("")
        icon = QtGui.QIcon()

        resize_image("graphics/Play_button_after_play_was_pressed.png", "graphics/T_Play_button_after_play_was_pressed.png", (int(width_k * 700), int(height_k * 181)))

        icon.addPixmap(QtGui.QPixmap("graphics/T_Play_button_after_play_was_pressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        resize_image("graphics/Back_to_main_menu_button_png.png", "graphics/T_Back_to_main_menu_button_png.png", (int(width_k * 356), int(height_k * 91)))

        icon1.addPixmap(QtGui.QPixmap("graphics/T_Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon1)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(width_k * 356, height_k * 91))
        self.Back_to_main_menu_button.setFlat(True)
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)
    # ---------------------------------------------------

    # ---------------Pregame window Backend--------------    
    def setup_actions_pregame(self):
        # Кнопки предигрового меню
        self.Back_to_main_menu_button.clicked.connect(self.to_main)
        self.Play_the_game_button.clicked.connect(self.setup_game)

    def setup_game(self):
        self.First_player_nickname = self.First_player_nickname_text.toPlainText()
        self.Second_player_nickname = self.Second_player_nickname_text.toPlainText()
        self.Word = self.Current_word_text.toPlainText()
        self.setup_game_process(self)
        self.setup_actions_game_process()
 
    def to_main(self):
        self.setup_main(self)
        self.setup_actions_main()
    # -----------------------------------------------------

    # --------------Rules window frontend------------------
    def setup_rules(self, MainWindow):
        self.centralwidget.deleteLater()

        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setText("")

        resize_image("graphics/Rules_png.png", "graphics/T_Rules_png.png", (width, height))

        self.label.setPixmap(QtGui.QPixmap("graphics/T_Rules_png.png"))
        self.label.setObjectName("label")

        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(20 * width_k, 30 * height_k, 356 * width_k, 91 * height_k))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")
        icon = QtGui.QIcon()

        resize_image("graphics/Back_to_main_menu_button_png.png", "graphics/T_Back_to_main_menu_button_png.png", (int(356 * width_k), int(91 * height_k)))

        icon.addPixmap(QtGui.QPixmap("graphics/T_Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(356 * width_k, 91 * height_k))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        MainWindow.setCentralWidget(self.centralwidget)

    # ----------------------------------------------------------------

    # ------------------------Rules window backend--------------------
    def setup_actions_rules(self):
        self.Back_to_main_menu_button.clicked.connect(self.to_main)
    # ----------------------------------------------------------------

    # -----------------------Game window frontend---------------------
    def setup_game_process(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")

        resize_image("graphics/Game_process_png.png", "graphics/T_Game_process_png.png", (width, height))

        self.label.setPixmap(QtGui.QPixmap("graphics/T_Game_process_png.png"))
        self.label.setObjectName("label")
        self.Back_to_main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_to_main_menu_button.setGeometry(QtCore.QRect(5 * width_k, 5 * height_k, width_k * 291, height_k * 81))
        self.Back_to_main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Back_to_main_menu_button.setText("")

        resize_image("graphics/Back_to_main_menu_button_png.png", "graphics/T_Back_to_main_menu_button_png.png", (int(width_k * 291), int(height_k * 81)))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/T_Back_to_main_menu_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_to_main_menu_button.setIcon(icon)
        self.Back_to_main_menu_button.setIconSize(QtCore.QSize(width_k * 291, height_k * 81))
        self.Back_to_main_menu_button.setObjectName("Back_to_main_menu_button")
        self.Card0 = QtWidgets.QPushButton(self.centralwidget)
        self.Card0.setGeometry(QtCore.QRect(560, 220, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card0.setFont(font)
        self.Card0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card0.setFlat(True)
        self.Card0.setObjectName("Card0")
        self.Card1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card1.setGeometry(QtCore.QRect(560, 280, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card1.setFont(font)
        self.Card1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card1.setFlat(True)
        self.Card1.setObjectName("Card1")
        self.Card2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card2.setGeometry(QtCore.QRect(560, 340, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card2.setFont(font)
        self.Card2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card2.setFlat(True)
        self.Card2.setObjectName("Card2")
        self.Card3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card3.setGeometry(QtCore.QRect(560, 400, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card3.setFont(font)
        self.Card3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card3.setFlat(True)
        self.Card3.setObjectName("Card3")
        self.Card4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4.setGeometry(QtCore.QRect(560, 460, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card4.setFont(font)
        self.Card4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card4.setFlat(True)
        self.Card4.setObjectName("Card4")
        self.Card5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5.setGeometry(QtCore.QRect(560, 520, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card5.setFont(font)
        self.Card5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card5.setFlat(True)
        self.Card5.setObjectName("Card5")
        self.Card6 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6.setGeometry(QtCore.QRect(560, 580, 321, 51))  # placement
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Card6.setFont(font)
        self.Card6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Card6.setFlat(True)
        self.Card6.setObjectName("Card6")
        self.Card7 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7.setGeometry(QtCore.QRect(560, 640, 321, 51))  # placement 
        font = QtGui.QFont()
        font.setPointSize(23)
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
        self.Refresh_button.setGeometry(QtCore.QRect(width_k * 1070, height_k * 10, width_k * 281, height_k * 81))
        self.Refresh_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Refresh_button.setText("")

        resize_image("graphics/Refresh_button_png.png", "graphics/T_Refresh_button_png.png", (int(width_k * 281), int(height_k * 81)))

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphics/T_Refresh_button_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_button.setIcon(icon1)
        self.Refresh_button.setIconSize(QtCore.QSize(width_k * 281, height_k * 81))
        self.Refresh_button.setObjectName("Refresh_button")

        self.First_player_nickname = QtWidgets.QLabel(self.centralwidget)
        self.First_player_nickname.setGeometry(QtCore.QRect(90, 108, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.First_player_nickname.setFont(font)
        self.First_player_nickname.setText("")
        self.First_player_nickname.setObjectName("First_player_nickname")
        self.Second_player_nickname = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_nickname.setGeometry(QtCore.QRect(1015, 108, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Second_player_nickname.setFont(font)
        self.Second_player_nickname.setText("")
        self.Second_player_nickname.setObjectName("Second_player_nickname")
        self.Current_word = QtWidgets.QLabel(self.centralwidget)
        self.Current_word.setGeometry(QtCore.QRect(700, 13, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Current_word.setFont(font)
        self.Current_word.setText("")
        self.Current_word.setObjectName("Current_word")
        self.Output_label = QtWidgets.QLabel(self.centralwidget)
        self.Output_label.setGeometry(QtCore.QRect(460, 790, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Output_label.setFont(font)
        self.Output_label.setText("")
        self.Output_label.setObjectName("Output_label")
        MainWindow.setCentralWidget(self.centralwidget)
    # ------------------------------------------------------------------

    # -----------------------Game window backend------------------------
    def setup_actions_game_process(self):
        self.Back_to_main_menu_button.clicked.connect(self.to_main)
    # -----------------------------------------------------------------