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
        self.Refresh_button.clicked.connect(self.Refresh)
        # Функции при нажатии на карту
        self.First_card.clicked.connect(self.First_card_add)
        self.Second_card.clicked.connect(self.Second_card_add)
        self.Third_card.clicked.connect(self.Third_card_add)
        self.Fourth_card.clicked.connect(self.Fourth_card_add)
        self.Fith_card.clicked.connect(self.Fith_card_add)
        self.Sixth_card.clicked.connect(self.Sixth_card_add)
        self.Seventh_card.clicked.connect(self.Seventh_card_add)
        self.Eith_card.clicked.connect(self.Eith_card_add)
        
        global First_card_text
        global Second_card_text
        global Third_card_text
        global Fourth_card_text
        global Fith_card_text
        global Sixth_card_text
        global Seventh_card_text
        global Eith_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn

        Turn = 1
        First_player_label_text = ""
        Second_player_label_text = ""
        First_card_text = "putchar(a);"
        self.First_card.setText(First_card_text)
        Second_card_text = "char a;"
        self.Second_card.setText(Second_card_text)
        Third_card_text = "a = 'k';"
        self.Third_card.setText(Third_card_text)
        Fourth_card_text = "putchar(b);"
        self.Fourth_card.setText(Fourth_card_text)
        Fith_card_text = "putchar(c);"
        self.Fith_card.setText(Fith_card_text)
        Sixth_card_text = "char c;"
        self.Sixth_card.setText(Sixth_card_text)
        Seventh_card_text = "char b;"
        self.Seventh_card.setText(Seventh_card_text)
        Eith_card_text = "b = 'o';"
        self.Eith_card.setText(Eith_card_text)     
            
    def Refresh(self):
        print("Keep working!")

    def Next_turn(self):
        global Turn
        
        Turn += 1

    def First_card_add(self):
        global First_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += First_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            First_card_text = ""
            self.First_card.setText(First_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += First_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            First_card_text = ""
            self.First_card.setText(First_card_text)

    def Second_card_add(self):
        global Second_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Second_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Second_card_text = ""
            self.Second_card.setText(Second_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Second_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Second_card_text = ""
            self.Second_card.setText(Second_card_text)

    def Third_card_add(self):
        global Third_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Third_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Third_card_text = ""
            self.Third_card.setText(Third_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Third_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Third_card_text = ""
            self.Third_card.setText(Third_card_text)

    def Fourth_card_add(self):
        global Fourth_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Fourth_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Fourth_card_text = ""
            self.Fourth_card.setText(Fourth_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Fourth_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Fourth_card_text = ""
            self.Fourth_card.setText(Fourth_card_text)

    def Fith_card_add(self):
        global Fith_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Fith_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Fith_card_text = ""
            self.Fith_card.setText(Fith_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Fith_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Fith_card_text = ""
            self.Fith_card.setText(Fith_card_text)

    def Sixth_card_add(self):
        global Sixth_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Sixth_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Sixth_card_text = ""
            self.Sixth_card.setText(Sixth_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Sixth_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Sixth_card_text = ""
            self.Sixth_card.setText(Sixth_card_text)

    def Seventh_card_add(self):
        global Seventh_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Seventh_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Seventh_card_text = ""
            self.Seventh_card.setText(Seventh_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Seventh_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Seventh_card_text = ""
            self.Seventh_card.setText(Seventh_card_text)

    def Eith_card_add(self):
        global Eith_card_text
        global First_player_label_text
        global Second_player_label_text
        global Turn
        
        if Turn == 1 or Turn == 3:
            First_player_label_text += Eith_card_text + "\n"         
            self.First_player_label.setText(First_player_label_text)
            Eith_card_text = ""
            self.Eith_card.setText(Eith_card_text)
        elif Turn == 2 or Turn == 4:
            Second_player_label_text += Eith_card_text + "\n"         
            self.Second_player_label.setText(Second_player_label_text)
            Eith_card_text = ""
            self.Eith_card.setText(Eith_card_text)
                  
    def Comeback(self):
        self.hide()
        
# Описание окна настроек, которое ни на что не влияет потому что никто не удосужился заняться звуком)
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
