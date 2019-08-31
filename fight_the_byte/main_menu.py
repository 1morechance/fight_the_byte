'''!@brief Файл с главным меню игры

'''

# Файлы с префиксом T адаптированы под машину пользователя

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from randomizer1 import*
from interpret import interpretation
import tkinter
import vlc

class Action_function():
    def __init__(self, i, object):
        self.index = i
        self.info = object

    def card_add(self):
        self.info.sound_play()
        if (self.info.Turn % 2 == 0):
            self.info.First_player_label_text += self.info.data_card_text[self.index] + "\n"
            self.info.First_player_stack.append(self.info.data_card[self.index])
            self.info.First_player_label.setText(self.info.First_player_label_text)
            self.info.card_obj_list[self.index].setText('')
        if (self.info.Turn % 2 == 1):
            self.info.Second_player_label_text += self.info.data_card_text[self.index] + "\n"
            self.info.Second_player_stack.append(self.info.data_card[self.index])
            self.info.Second_player_label.setText(self.info.Second_player_label_text)
            self.info.card_obj_list[self.index].setText('')
        self.info.next_turn()
        self.info.Output_label.setText(get_output())

    def back_function(self):
        return self.card_add

    def update_situation(self):
        return self.info    

HAND_SIZE = 8

sound = vlc.MediaPlayer("music/button_click.mp3")
melody = vlc.MediaPlayer("music/tyla_yaweh.mp3")

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
        self.sound_play()
        self.setup_Pre_Game(self)
        self.setup_actions_pregame()

    def to_settings(self):
        '''!@brief Функция вызова настроек игры
        '''
        self.sound_play()
        self.setup_settings(self)
        self.setup_actions_settings()

    def to_rules(self):
        '''!@brief Функция вызова правил игры
        '''
        self.sound_play()
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
        self.pushButton.setObjectName("pushButton")
        if (self.sounds_control):
            self.pushButton.setChecked(True)
        else:
            self.pushButton.setChecked(False)
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
        self.pushButton.clicked.connect(self.sounds_check)
        self.pushButton_2.clicked.connect(self.music_check)

    def sounds_check(self):
        self.sound_play()
        if (self.pushButton.isChecked()):
            self.sounds_control = True
        else:
            self.sounds_control = False

    def music_check(self):
        self.sound_play()
        if (self.pushButton_2.isChecked()):
            melody.play()
        else:
            melody.pause()
    
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
        self.sound_play()
        self.First_player_name = self.First_player_nickname_text.toPlainText()
        self.Second_player_name = self.Second_player_nickname_text.toPlainText()
        self.players_dict = {1 : self.First_player_name, 2 : self.Second_player_name}
        self.Word = self.Current_word_text.toPlainText()
        self.setup_game_process(self)
        self.setup_actions_game_process()
 
    def to_main(self):
        self.sound_play()
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
        self.centralwidget.deleteLater()
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

        self.card_obj_list = []

        self.button_x = 321 * width_k
        self.button_y = 51 * height_k
        self.button_orientation_hor = 560 * width_k
        self.button_orientation_vert = 220

        font = QtGui.QFont()
        font.setPointSize(23)

        for i in range(HAND_SIZE): # Создание кнопок
            self.card_obj_list.append(QtWidgets.QPushButton(self.centralwidget))
            self.card_obj_list[i].setGeometry(QtCore.QRect(self.button_orientation_hor, self.button_orientation_vert * height_k, self.button_x, self.button_y))
            self.card_obj_list[i].setFont(font)
            self.card_obj_list[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.card_obj_list[i].setFlat(True)
            self.button_orientation_vert += 60
    
        self.First_player_label = QtWidgets.QLabel(self.centralwidget)
        self.First_player_label.setGeometry(QtCore.QRect(width_k * 110, height_k * 160, width_k * 351, height_k * 591))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.First_player_label.setFont(font)
        self.First_player_label.setText("")
        self.First_player_label.setObjectName("First_player_label")

        self.Second_player_label = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_label.setGeometry(QtCore.QRect(width_k * 1040, height_k * 160, width_k * 351, height_k * 601))
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
        self.First_player_nickname.setGeometry(QtCore.QRect(width_k * 90, height_k * 108, width_k * 291, height_k * 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.First_player_nickname.setFont(font)
        self.First_player_nickname.setText(self.First_player_name)
        self.First_player_nickname.setObjectName("First_player_nickname")

        self.Second_player_nickname = QtWidgets.QLabel(self.centralwidget)
        self.Second_player_nickname.setGeometry(QtCore.QRect(width_k * 1015, height_k * 108, width_k * 291, height_k * 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Second_player_nickname.setFont(font)
        self.Second_player_nickname.setText(self.Second_player_name)
        self.Second_player_nickname.setObjectName("Second_player_nickname")

        self.Current_word = QtWidgets.QLabel(self.centralwidget)
        self.Current_word.setGeometry(QtCore.QRect(width_k * 700, height_k * 13, width_k * 231, height_k * 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Current_word.setFont(font)
        self.Current_word.setText("")
        self.Current_word.setObjectName("Current_word")

        self.Output_label = QtWidgets.QLabel(self.centralwidget)
        self.Output_label.setGeometry(QtCore.QRect(width_k * 460, height_k * 790, width_k * 541, height_k * 81))
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
        self.Refresh_button.clicked.connect(self.Cards_generate)

        self.data_card = []
        self.data_card_text = []

        for i in range(HAND_SIZE):
            self.data_card.append(i)
            self.data_card_text.append("")

        self.Turn = 0

        self.First_player_label_text = ''
        self.Second_player_label_text = ''
        
        self.First_player_label.setText('')
        self.Second_player_label.setText('')

        self.First_player_stack = []
        self.Second_player_stack = []
    
        self.Current_word.setText(self.Word)
        
        self.winner = 0

        self.data = pd.DataFrame()  # Информация о переменных (для невменяемых)
        self.cards_array = []  # Массив карточек 
        self.num = 8  # Количество карточек

        self.obj_array = []
        for i in range(HAND_SIZE):
            self.obj_array.append(Action_function(i ,self))  # создание объекта с функцией активации кнопки
            self.card_obj_list[i].clicked.connect(self.obj_array[i].back_function()) # данный метод возвратит функцию активации кнопки
            
    def next_turn(self):
        self.Turn += 1
        if (self.Turn % 2 == 0):
            clean()
            self.winner = interpretation(self.First_player_stack, self.Second_player_stack, self.Word, self)
            if (self.winner):
                self.setup_results()
                self.output_window.setText("Player '" + self.players_dict[self.winner] + "' is the winner!!!")

    def Cards_generate(self):
        self.sound_play() 
        self.data, self.cards_array = generate_draft(self.num, self.data, self.Word)

        for i in range(HAND_SIZE):
            self.data_card[i] = self.cards_array[i]
            self.data_card_text[i] = self.cards_array[i].view()

        for i in range(HAND_SIZE):
            self.card_obj_list[i].setText(self.data_card_text[i])
    # -----------------------------------------------------------------

    def setup_results(self):
        self.setup_results_gui(self)
        self.setup_results_actions()

    # ------------------------results window frontend -----------------
    def setup_results_gui(self, MainWindow):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")

        resize_image("graphics/winner.png", "graphics/T_winner.png", (width, height))
        self.label.setPixmap(QtGui.QPixmap("graphics/T_winner.png")) # для фона

        self.output_window = QtWidgets.QLabel(self.centralwidget)
        self.output_window.setGeometry(QtCore.QRect(width / 2 - 335 * width_k, height / 2 - 100 * height_k, width_k  * 1000, height_k * 200))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.output_window.setFont(font)
        self.output_window.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
    # -----------------------------------------------------------------

    # ------------------------results window backend ------------------
    def setup_results_actions(self):
        pass
    # -----------------------------------------------------------------
    def sound_play(self):
        if (self.sounds_control):
            sound.stop()
            sound.play()

    # Атрибуты класса---------------------------------------------------        
    sounds_control = False