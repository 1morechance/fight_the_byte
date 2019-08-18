'''!@brief Главный мозг программы, отсюда происходит управление всеми файлами

'''

from randomizer1 import*
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import main_menu
import game_process_menu
import settings
import rules_menu
from cards import clean, get_output, set_output
from interpret import interpretation


'''global First_player_nickname
First_player_nickname = ''
global Second_player_nickname
Second_player_nickname = ''
global Word
Word = ''
'''

class Main_Window(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    '''!@brief Класс описания параметров и функций кнопок главного меню
    '''
    def __init__(self, parent=None):
        super().__init__()
        self.setup_main(self)
        self.setup_actions_main()       
        
class Play_Window(QtWidgets.QMainWindow, game_process_menu.Ui_MainWindow):
    '''!@brief Описание окна игрового процесса,здесь есть кнопка Next_turn_button, ну собственно здесь начинается работа девелоперов
    '''
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
        
        self.word = "..."
    
        self.Current_word.setText(self.word)
        self.First_player_nickname.setText('')
        self.Second_player_nickname.setText('')
        
        self.winner = 0

        self.data = pd.DataFrame()  # Информация о переменных (для невменяемых)
        self.cards_array = []  # Массив карточек 
        self.num = 8  # Количество карточек
            
    def Cards_generate(self): 
        '''!@brief Получение 8 новых типов карточек (новая партия)
        '''

        global First_player_nickname
        global Second_player_nickname
        global Word
    
        self.First_player_nickname.setText(First_player_nickname)
        self.Second_player_nickname.setText(Second_player_nickname)
        self.Current_word.setText(Word)
        
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
        '''!@ Функция переключения хода
        '''
        self.Turn += 1
        if (self.Turn % 2 == 0):
            clean()
            self.winner = interpretation(self.First_player_stack, self.Second_player_stack, self.word)
            if (self.winner):
                print("Player " + str(self.winner) + " победил")
        
    def Card_0_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_1_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_2_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_3_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_4_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_5_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_6_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())

    def Card_7_add(self):
        '''!@brief Функция добавления карты в код игрока
        '''
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
        self.Next_turn()
        self.Output_label.setText(get_output())
                  
    def Comeback(self):
        '''!@brief Фукнция возвратa
        '''
        self.hide()
        
class Settings_Window(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    '''!@brief Класс вызова окна настроек
    '''
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        '''!@brief Функция возврата
        '''
        self.hide()
        
       
class Rules_Window(QtWidgets.QMainWindow, rules_menu.Ui_MainWindow):
    '''!@brief Класс вызова правил игры
    '''
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Back_to_main_menu_button.clicked.connect(self.comeback)

    def comeback(self):
        '''!@brief Функция возврата
        '''
        self.hide()

   
def main():
    '''!@brief основная функция работы файла
    '''
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
