from randomizer import *
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import main_menu
import game_process_menu
import settings
import rules_menu

# В этом классе мы описываем параметры и функции кнопок главного меню
class Main_Window(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
        # Описываем функции каждой кнопки, используя ее objectName(Play_button, etc.)
        self.Play_button.clicked.connect(self.Game)
        self.Settings_button.clicked.connect(self.Settings)
        self.Rules_button.clicked.connect(self.Rules)
        self.dialog_game_process = Play_Window(self)
        self.dialog_settings = Settings_Window(self)
        self.dialog_rules = Rules_Window(self)

    #Функции, вызова новых окон в соответствии с каждой кнопкой
    def Game(self):
        self.dialog_game_process.show()

    def Settings(self):
        self.dialog_settings.show()

    def Rules(self):
        self.dialog_rules.show()
        
# Описаниее окна игрового процесса,здесь есть кнопка Next_turn_button, ну собственно здесь начинается работа девелоперов
class Play_Window(QtWidgets.QMainWindow, game_process_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.Comeback)
        self.Next_turn_button.clicked.connect(self.Next_turn)
        self.Refresh_button.clicked.connect(self.Card_generate)
        
        # Функции при нажатии на карту
        self.Card1.clicked.connect(self.Card1_add)

        # Переменные и карточки
        self.data = pd.DataFrame()  # Информация о переменных (для невменяемых)
        self.cards_array = []  # Массив карточек 
        self.num = 8  # Количество карточек
            
    def Refresh(self):  # Получение 8 новых типов карточек (новая партия) 
        self.data, self.cards_array = generate_draft(self.num, self.data, "dick")

        self.data_card_text = []

        for i in range(len(self.cards_array)):
            self.data_card_text.append(self.cards_array[i].view())

        print(self.data_card_text)
        print('\n\n')
        return self.data_card_text

    def Card_generate(self):
        self.types_array = []  # Массив виджетов (карт)
        global Card_text0
        global Card_text1
        global Card_text2
        global Card_text3
        global Card_text4
        global Card_text5
        global Card_text6
        global Card_text7
        global First_player_label_text
        global Second_player_label_text

        First_player_label_text = ''
        Second_player_label_text = ''
        self.First_player_label.setText(First_player_label_text)
        self.Second_player_label.setText(First_player_label_text)
        
        self.data_card_text = self.Refresh()

        Card_text0 = self.data_card_text[0]
        self.Card0.setText(Card_text0)

        Card_text1 = self.data_card_text[1]
        self.Card1.setText(Card_text1)

        Card_text2 = self.data_card_text[2]
        self.Card2.setText(Card_text2)

        Card_text3 = self.data_card_text[3]
        self.Card3.setText(Card_text3)

        Card_text4 = self.data_card_text[4]
        self.Card4.setText(Card_text4)

        Card_text5 = self.data_card_text[5]
        self.Card5.setText(Card_text5)

        Card_text6 = self.data_card_text[6]
        self.Card6.setText(Card_text6)

        Card_text7 = self.data_card_text[7]
        self.Card7.setText(Card_text7)

    def Next_turn(self):
        global Turn
        
        Turn += 1
        
    def Card1_add(self):
        global Card1_text
        global First_player_label_text
        global Second_player_label_text

        First_player_label_text += Card1_text + "\n"         
        self.First_player_label.setText(First_player_label_text)
        Card1_text = ""
        self.Card1.setText(Card_text)
                  
    def Comeback(self):
        self.hide()
        
class Settings_Window(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        self.hide()
        
# Окно правил        
class Rules_Window(QtWidgets.QMainWindow, rules_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        self.hide()

# main function    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
>>>>>>> GUI
