from randomizer1 import*
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import main_menu
import game_process_menu
import settings
import rules_menu
import Pre_game_menu
from cards import clean
from interpret import interpretation

# В этом классе мы описываем параметры и функции кнопок главного меню
class Main_Window(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
        # Описываем функции каждой кнопки, используя ее objectName(Play_button, etc.)
        self.Play_button.clicked.connect(self.Game)
        self.Settings_button.clicked.connect(self.Settings)
        self.Rules_button.clicked.connect(self.Rules)
        self.dialog_game_process = Pre_game_Window(self)
        self.dialog_settings = Settings_Window(self)
        self.dialog_rules = Rules_Window(self)

    #Функции, вызова новых окон в соответствии с каждой кнопкой
    def Game(self):
        self.dialog_game_process.show()

    def Settings(self):
        self.dialog_settings.show()

    def Rules(self):
        self.dialog_rules.show()

class Pre_game_Window(QtWidgets.QMainWindow, Pre_game_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.Comeback)
        self.Play_the_game_button.clicked.connect(self.Game)
        self.dialog_game_process = Play_Window(self)
 
    def Game(self):
        self.dialog_game_process.show()
 
    def Comeback(self):
        self.hide()
        
# Описаниее окна игрового процесса,здесь есть кнопка Next_turn_button, ну собственно здесь начинается работа девелоперов
class Play_Window(QtWidgets.QMainWindow, game_process_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.Comeback)
        self.Refresh_button.clicked.connect(self.Cards_generate)
        
        # Выбор карточки:
        self.Card0.clicked.connect(self.Card_0_add)
        self.Card1.clicked.connect(self.Card_1_add)
        self.Card2.clicked.connect(self.Card_2_add)
        self.Card3.clicked.connect(self.Card_3_add)
        self.Card4.clicked.connect(self.Card_4_add)
        self.Card5.clicked.connect(self.Card_5_add)
        self.Card6.clicked.connect(self.Card_6_add)
        self.Card7.clicked.connect(self.Card_7_add)

        self.Turn = 0

        self.First_player_label_text = ''
        self.Second_player_label_text = ''
        
        self.First_player_label.setText('')
        self.Second_player_label.setText('')
        
        self.Card0.setText('')
        self.Card1.setText('')
        self.Card2.setText('')
        self.Card3.setText('')
        self.Card4.setText('')
        self.Card5.setText('')
        self.Card6.setText('')
        self.Card7.setText('')

        self.First_player_stack = []
        self.Second_player_stack = []
        
        self.word = "FOOK"

        self.Current_word.setText(self.word)
        self.First_player_nickname.setText('CONOR')
        self.Second_player_nickname.setText('KHABIB')
        
        self.winner = 0

        self.data = pd.DataFrame()  # Информация о переменных (для невменяемых)
        self.cards_array = []  # Массив карточек 
        self.num = 8  # Количество карточек
            
    def Cards_generate(self):  # Получение 8 новых типов карточек (новая партия)
        
        self.data, self.cards_array = generate_draft(self.num, self.data, self.word)

        self.data_card = []
        self.data_card_text = []

        for i in range(len(self.cards_array)):
            self.data_card.append(self.cards_array[i])
            self.data_card_text.append(self.cards_array[i].view())
              
        self.Card0.setText(self.data_card_text[0])
        self.Card1.setText(self.data_card_text[1])
        self.Card2.setText(self.data_card_text[2])
        self.Card3.setText(self.data_card_text[3])
        self.Card4.setText(self.data_card_text[4])
        self.Card5.setText(self.data_card_text[5])
        self.Card6.setText(self.data_card_text[6])
        self.Card7.setText(self.data_card_text[7])

    def Next_turn(self):
        self.Turn += 1
        if (self.Turn % 2 == 0):
            clean()
            self.winner = interpretation(self.First_player_stack, self.Second_player_stack, self.word)
            if (self.winner):
                print("Player " + str(self.winner) + " победил")
        
    def Card_0_add(self):
        self.Next_turn()
        self.Output_label.setText("0")
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[0] + "\n"
            self.First_player_stack.append(self.data_card[0])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card0.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[0] + "\n"
            self.Second_player_stack.append(self.data_card[0])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card0.setText('')

    def Card_1_add(self):
        self.Output_label.setText("1")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[1] + "\n"
            self.First_player_stack.append(self.data_card[1])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card1.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[1] + "\n"
            self.Second_player_stack.append(self.data_card[1])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card1.setText('')

    def Card_2_add(self):
        self.Output_label.setText("2")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[2] + "\n"
            self.First_player_stack.append(self.data_card[2])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card2.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[2] + "\n"
            self.Second_player_stack.append(self.data_card[2])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card2.setText('')

    def Card_3_add(self):
        self.Output_label.setText("3")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[3] + "\n"
            self.First_player_stack.append(self.data_card[3])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card3.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[3] + "\n"
            self.Second_player_stack.append(self.data_card[3])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card3.setText('')

    def Card_4_add(self):
        self.Output_label.setText("4")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[4] + "\n"
            self.First_player_stack.append(self.data_card[4])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card4.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[4] + "\n"
            self.Second_player_stack.append(self.data_card[4])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card4.setText('')

    def Card_5_add(self):
        self.Output_label.setText("5")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[5] + "\n"
            self.First_player_stack.append(self.data_card[5])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card5.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[5] + "\n"
            self.Second_player_stack.append(self.data_card[5])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card5.setText('')

    def Card_6_add(self):
        self.Output_label.setText("6")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[6] + "\n"
            self.First_player_stack.append(self.data_card[6])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card6.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[6] + "\n"
            self.Second_player_stack.append(self.data_card[6])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card6.setText('')

    def Card_7_add(self):
        self.Output_label.setText("7")
        self.Next_turn()
        if (self.Turn % 2 == 0):
            self.First_player_label_text += self.data_card_text[7] + "\n"
            self.First_player_stack.append(self.data_card[7])
            self.First_player_label.setText(self.First_player_label_text)
            self.Card7.setText('')
        if (self.Turn % 2 == 1):
            self.Second_player_label_text += self.data_card_text[7] + "\n"
            self.Second_player_stack.append(self.data_card[7])
            self.Second_player_label.setText(self.Second_player_label_text)
            self.Card7.setText('')
                  
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
